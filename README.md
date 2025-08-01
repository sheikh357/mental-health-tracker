# Mental Health Tracker

An AI-powered mental health tracking web application that helps users monitor their mental wellbeing through mood logging, pattern analysis, and personalized insights.

## 🌟 Features

### Core Functionality
- **Mood Logging**: Track daily mood, emotions, energy levels, sleep, and stress
- **Interactive Dashboard**: Visualize mood trends and statistics
- **AI-Powered Analytics**: Get personalized insights and pattern recognition
- **Data Visualization**: Charts and graphs showing mood trends over time
- **User Authentication**: Secure user accounts and data privacy
- **Responsive Design**: Works on desktop and mobile devices

### AI Analysis Features
- Sentiment analysis of mood notes
- Weekly pattern detection (best/worst days)
- Sleep-mood correlation analysis
- Stress level impact assessment
- Mood trend analysis (improving/declining)
- Personalized recommendations based on data

### User Interface
- Clean, modern design with Bootstrap 5
- Intuitive mood logging with sliders and emotion buttons
- Interactive charts using Chart.js
- Real-time feedback and insights
- Mobile-responsive layout

## 🛠 Technology Stack

### Backend
- **Python Flask**: Web framework
- **SQLAlchemy**: Database ORM
- **Flask-Login**: User session management
- **SQLite**: Database (easily upgradable to PostgreSQL)

### Frontend
- **HTML5/CSS3**: Modern web standards
- **JavaScript**: Interactive functionality
- **Bootstrap 5**: Responsive UI framework
- **Chart.js**: Data visualization
- **Font Awesome**: Icons

### AI/Analytics
- **TextBlob**: Sentiment analysis (optional)
- **Custom algorithms**: Pattern recognition and correlation analysis
- **Statistical analysis**: Trend detection and insights

## 📁 Project Structure

```
mental-health-tracker/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── demo.py               # Standalone demo version
├── templates/            # HTML templates
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── log_mood.html
│   └── analytics.html
├── static/               # Static assets
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── app.js
│   └── assets/
├── ai_analysis/          # AI analysis module
│   ├── __init__.py
│   └── mood_analyzer.py  # Mood analysis algorithms
└── tests/                # Unit tests
    ├── __init__.py
    ├── test_app.py
    └── test_ai_analysis.py
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/sheikh357/mental-health-tracker.git
   cd mental-health-tracker
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Access the application**
   Open your browser and navigate to `http://localhost:5000`

### Demo Version

For a quick demonstration without setting up the full web application:

```bash
python demo.py
```

This runs a command-line version showcasing all the core features.

## 📊 Usage

### Getting Started
1. **Register**: Create a new account or log in
2. **Log Your First Mood**: Rate your mood, select emotions, and add notes
3. **Track Daily**: Build a habit of daily mood logging
4. **Analyze Patterns**: View analytics and AI insights after a few entries

### Mood Logging
- **Mood Score**: Rate overall mood from 1-10
- **Emotions**: Select from predefined emotions or add custom ones
- **Energy Level**: Track physical and mental energy
- **Sleep Hours**: Log sleep quality and duration
- **Stress Level**: Monitor stress levels
- **Notes**: Add context and details about your day

### Analytics Dashboard
- **Trend Charts**: Visualize mood changes over time
- **Correlation Analysis**: See how sleep, stress affect mood
- **Pattern Recognition**: Identify weekly patterns and triggers
- **AI Insights**: Get personalized recommendations

## 🤖 AI Features

### Pattern Recognition
- **Weekly Patterns**: Identifies best and worst days of the week
- **Correlation Analysis**: Finds relationships between sleep, stress, and mood
- **Trend Detection**: Tracks mood improvements or declines
- **Emotion Patterns**: Analyzes frequent emotions and their impact

### Personalized Recommendations
- Sleep hygiene suggestions
- Stress management techniques
- Activity recommendations
- Support-seeking guidance
- Positive reinforcement for good trends

### Data Privacy
- All AI analysis is performed locally
- No personal data is shared with external services
- Users maintain full control of their data

## 🧪 Testing

Run the test suite:

```bash
python -m pytest tests/
```

Or run individual test files:

```bash
python tests/test_app.py
python tests/test_ai_analysis.py
```

## 🔧 Configuration

### Database
- Default: SQLite (mental_health.db)
- Production: Easily configurable for PostgreSQL or MySQL

### Security
- Session management with Flask-Login
- Password hashing with Werkzeug
- CSRF protection (can be added)
- Optional: OAuth integration

### Deployment
Ready for deployment on:
- Heroku
- Docker containers
- Traditional web servers
- Cloud platforms (AWS, GCP, Azure)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

If you're experiencing mental health difficulties, please reach out to:

- **Crisis Text Line**: Text HOME to 741741
- **National Suicide Prevention Lifeline**: 988
- **SAMHSA National Helpline**: 1-800-662-4357

Remember: This app is a tool for self-reflection and not a replacement for professional mental health care.

## 🔮 Future Enhancements

- Export data to CSV/PDF
- Integration with wearable devices
- Medication tracking
- Therapist sharing features
- Mobile app (React Native)
- Advanced ML models for prediction
- Community features (optional)
- Integration with calendar apps

## 👥 Team

Built with ❤️ for mental health awareness and support.

---

**Disclaimer**: This application is for informational and self-tracking purposes only. It is not intended as a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of qualified health providers with questions about mental health conditions.
