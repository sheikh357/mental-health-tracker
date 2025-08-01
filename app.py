from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
import json
import os
from ai_analysis.mood_analyzer import mood_analyzer

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mental-health-tracker-secret-key-2024'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mental_health.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Database Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    mood_entries = db.relationship('MoodEntry', backref='user', lazy=True)

class MoodEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    mood_score = db.Column(db.Integer, nullable=False)  # 1-10 scale
    emotions = db.Column(db.Text)  # JSON string of emotions
    notes = db.Column(db.Text)
    energy_level = db.Column(db.Integer)  # 1-10 scale
    sleep_hours = db.Column(db.Float)
    stress_level = db.Column(db.Integer)  # 1-10 scale
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        # Check if user exists
        if User.query.filter_by(username=username).first():
            flash('Username already exists')
            return render_template('register.html')
        
        if User.query.filter_by(email=email).first():
            flash('Email already registered')
            return render_template('register.html')
        
        # Create new user
        user = User(
            username=username,
            email=email,
            password_hash=generate_password_hash(password)
        )
        db.session.add(user)
        db.session.commit()
        
        login_user(user)
        return redirect(url_for('dashboard'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password')
    
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    # Get recent mood entries
    recent_entries = MoodEntry.query.filter_by(user_id=current_user.id)\
                                   .order_by(MoodEntry.created_at.desc())\
                                   .limit(7).all()
    
    return render_template('dashboard.html', recent_entries=recent_entries)

@app.route('/log-mood', methods=['GET', 'POST'])
@login_required
def log_mood():
    if request.method == 'POST':
        data = request.get_json()
        
        mood_entry = MoodEntry(
            user_id=current_user.id,
            mood_score=data['mood_score'],
            emotions=json.dumps(data.get('emotions', [])),
            notes=data.get('notes', ''),
            energy_level=data.get('energy_level'),
            sleep_hours=data.get('sleep_hours'),
            stress_level=data.get('stress_level')
        )
        
        db.session.add(mood_entry)
        db.session.commit()
        
        return jsonify({'success': True, 'message': 'Mood logged successfully'})
    
    return render_template('log_mood.html')

@app.route('/api/mood-data')
@login_required
def mood_data():
    days = request.args.get('days', 30, type=int)
    start_date = datetime.utcnow() - timedelta(days=days)
    
    entries = MoodEntry.query.filter_by(user_id=current_user.id)\
                            .filter(MoodEntry.created_at >= start_date)\
                            .order_by(MoodEntry.created_at).all()
    
    data = []
    for entry in entries:
        data.append({
            'date': entry.created_at.strftime('%Y-%m-%d'),
            'mood_score': entry.mood_score,
            'energy_level': entry.energy_level,
            'stress_level': entry.stress_level,
            'sleep_hours': entry.sleep_hours,
            'emotions': json.loads(entry.emotions) if entry.emotions else [],
            'notes': entry.notes
        })
    
    return jsonify(data)

@app.route('/analytics')
@login_required
def analytics():
    return render_template('analytics.html')

@app.route('/api/ai-insights')
@login_required
def ai_insights():
    # Get user's mood entries
    entries = MoodEntry.query.filter_by(user_id=current_user.id)\
                            .order_by(MoodEntry.created_at).all()
    
    if len(entries) < 3:
        return jsonify({
            'patterns': [],
            'insights': [{
                'type': 'info',
                'category': 'general',
                'description': 'Keep logging your mood for personalized AI insights!'
            }],
            'recommendations': [{
                'category': 'general',
                'title': 'Keep Tracking',
                'description': 'Continue logging your mood daily to get personalized insights.',
                'priority': 'medium'
            }]
        })
    
    # Analyze patterns and generate insights
    analysis = mood_analyzer.find_mood_patterns(entries)
    recommendations = mood_analyzer.generate_recommendations(entries)
    
    return jsonify({
        'patterns': analysis['patterns'],
        'insights': analysis['insights'],
        'recommendations': recommendations
    })

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0', port=5000)