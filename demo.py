#!/usr/bin/env python3
"""
Simple Mental Health Tracker Demo
This is a basic implementation that shows the application structure
without external dependencies for demonstration purposes.
"""

import json
import sqlite3
import hashlib
from datetime import datetime, timedelta


class SimpleDB:
    """Simple SQLite database wrapper"""
    
    def __init__(self, db_path='mental_health_demo.db'):
        self.db_path = db_path
        self.init_db()
    
    def init_db(self):
        """Initialize database tables"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS mood_entries (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                mood_score INTEGER NOT NULL,
                emotions TEXT,
                notes TEXT,
                energy_level INTEGER,
                sleep_hours REAL,
                stress_level INTEGER,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def create_user(self, username, email, password):
        """Create a new user"""
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        try:
            cursor.execute(
                'INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)',
                (username, email, password_hash)
            )
            conn.commit()
            return cursor.lastrowid
        except sqlite3.IntegrityError:
            return None
        finally:
            conn.close()
    
    def authenticate_user(self, username, password):
        """Authenticate user"""
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute(
            'SELECT id FROM users WHERE username = ? AND password_hash = ?',
            (username, password_hash)
        )
        
        result = cursor.fetchone()
        conn.close()
        
        return result[0] if result else None
    
    def add_mood_entry(self, user_id, mood_score, emotions=None, notes='', 
                      energy_level=None, sleep_hours=None, stress_level=None):
        """Add a mood entry"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO mood_entries 
            (user_id, mood_score, emotions, notes, energy_level, sleep_hours, stress_level)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (user_id, mood_score, json.dumps(emotions) if emotions else '[]', 
              notes, energy_level, sleep_hours, stress_level))
        
        conn.commit()
        conn.close()
        
        return cursor.lastrowid
    
    def get_mood_entries(self, user_id, days=30):
        """Get mood entries for a user"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT mood_score, emotions, notes, energy_level, sleep_hours, stress_level, created_at
            FROM mood_entries 
            WHERE user_id = ? 
            AND created_at >= datetime('now', '-{} days')
            ORDER BY created_at DESC
        '''.format(days), (user_id,))
        
        entries = cursor.fetchall()
        conn.close()
        
        return entries


class MentalHealthTracker:
    """Main application class"""
    
    def __init__(self):
        self.db = SimpleDB()
        self.current_user_id = None
        self.current_username = None
    
    def run_demo(self):
        """Run a command-line demo of the application"""
        print("=" * 60)
        print("🧠 MENTAL HEALTH TRACKER - DEMO")
        print("=" * 60)
        print()
        
        while True:
            if not self.current_user_id:
                self.show_login_menu()
            else:
                self.show_main_menu()
    
    def show_login_menu(self):
        """Show login/register menu"""
        print("Welcome! Please choose an option:")
        print("1. Register new account")
        print("2. Login")
        print("3. View demo data")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == '1':
            self.register()
        elif choice == '2':
            self.login()
        elif choice == '3':
            self.show_demo_data()
        elif choice == '4':
            print("Goodbye! Take care of your mental health! 💚")
            exit()
        else:
            print("Invalid choice. Please try again.\n")
    
    def register(self):
        """Handle user registration"""
        print("\n--- USER REGISTRATION ---")
        username = input("Username: ").strip()
        email = input("Email: ").strip()
        password = input("Password: ").strip()
        
        user_id = self.db.create_user(username, email, password)
        
        if user_id:
            print(f"✅ Account created successfully! Welcome, {username}!")
            self.current_user_id = user_id
            self.current_username = username
        else:
            print("❌ Username or email already exists. Please try again.")
        
        print()
    
    def login(self):
        """Handle user login"""
        print("\n--- USER LOGIN ---")
        username = input("Username: ").strip()
        password = input("Password: ").strip()
        
        user_id = self.db.authenticate_user(username, password)
        
        if user_id:
            print(f"✅ Welcome back, {username}!")
            self.current_user_id = user_id
            self.current_username = username
        else:
            print("❌ Invalid username or password.")
        
        print()
    
    def show_main_menu(self):
        """Show main application menu"""
        print(f"--- WELCOME, {self.current_username.upper()}! ---")
        print("1. Log mood entry")
        print("2. View mood history")
        print("3. View analytics")
        print("4. Get AI insights")
        print("5. Logout")
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == '1':
            self.log_mood()
        elif choice == '2':
            self.view_history()
        elif choice == '3':
            self.view_analytics()
        elif choice == '4':
            self.show_ai_insights()
        elif choice == '5':
            self.logout()
        else:
            print("Invalid choice. Please try again.\n")
    
    def log_mood(self):
        """Log a mood entry"""
        print("\n--- LOG YOUR MOOD ---")
        
        print("Rate your overall mood (1-10, where 1=very poor, 10=excellent):")
        mood_score = int(input("Mood score: "))
        
        print("\nSelect emotions (comma-separated):")
        emotions_str = input("Options: happy, sad, anxious, excited, calm, angry, grateful, stressed: ")
        emotions = [e.strip() for e in emotions_str.split(',') if e.strip()]
        
        energy_level = int(input("Energy level (1-10): "))
        sleep_hours = float(input("Sleep hours last night: "))
        stress_level = int(input("Stress level (1-10): "))
        notes = input("Notes (optional): ")
        
        entry_id = self.db.add_mood_entry(
            self.current_user_id, mood_score, emotions, notes,
            energy_level, sleep_hours, stress_level
        )
        
        print(f"✅ Mood entry logged successfully! (ID: {entry_id})")
        self.show_quick_insight(mood_score, emotions, energy_level, stress_level)
        print()
    
    def show_quick_insight(self, mood_score, emotions, energy_level, stress_level):
        """Show a quick insight based on the entry"""
        print("\n💡 Quick Insight:")
        
        if mood_score >= 8:
            print("🌟 Great to see you're feeling excellent! Keep up whatever you're doing.")
        elif mood_score >= 6:
            print("😊 You're doing well! Consider what's contributing to your positive mood.")
        elif mood_score >= 4:
            print("😐 You're managing okay. Consider some self-care activities.")
        else:
            print("💙 It sounds like you're having a tough time. Remember it's okay to seek support.")
        
        if stress_level >= 8:
            print("⚠️ Your stress levels are high. Consider relaxation techniques or talking to someone.")
        
        if 'grateful' in emotions:
            print("🙏 Gratitude is powerful for mental wellbeing. Great job recognizing it!")
    
    def view_history(self):
        """View mood history"""
        print("\n--- MOOD HISTORY ---")
        entries = self.db.get_mood_entries(self.current_user_id, 30)
        
        if not entries:
            print("No mood entries found. Start by logging your first mood!")
            print()
            return
        
        print(f"Showing last {len(entries)} entries:")
        print("-" * 80)
        
        for entry in entries[:10]:  # Show last 10
            mood_score, emotions, notes, energy, sleep, stress, created_at = entry
            emotions_list = json.loads(emotions) if emotions else []
            
            print(f"📅 {created_at}")
            print(f"   Mood: {mood_score}/10 | Energy: {energy}/10 | Stress: {stress}/10 | Sleep: {sleep}h")
            if emotions_list:
                print(f"   Emotions: {', '.join(emotions_list)}")
            if notes:
                print(f"   Notes: {notes}")
            print()
        
        input("Press Enter to continue...")
        print()
    
    def view_analytics(self):
        """View mood analytics"""
        print("\n--- MOOD ANALYTICS ---")
        entries = self.db.get_mood_entries(self.current_user_id, 30)
        
        if len(entries) < 3:
            print("Not enough data for analytics. Log more mood entries!")
            print()
            return
        
        # Calculate averages
        mood_scores = [entry[0] for entry in entries]
        energy_levels = [entry[3] for entry in entries if entry[3]]
        sleep_hours = [entry[4] for entry in entries if entry[4]]
        stress_levels = [entry[5] for entry in entries if entry[5]]
        
        print(f"📊 ANALYTICS FOR LAST {len(entries)} ENTRIES:")
        print("-" * 50)
        print(f"Average Mood Score: {sum(mood_scores)/len(mood_scores):.1f}/10")
        
        if energy_levels:
            print(f"Average Energy Level: {sum(energy_levels)/len(energy_levels):.1f}/10")
        
        if sleep_hours:
            print(f"Average Sleep: {sum(sleep_hours)/len(sleep_hours):.1f} hours")
        
        if stress_levels:
            print(f"Average Stress Level: {sum(stress_levels)/len(stress_levels):.1f}/10")
        
        # Mood trend
        if len(mood_scores) >= 7:
            recent_avg = sum(mood_scores[:7]) / 7
            older_avg = sum(mood_scores[7:14]) / min(7, len(mood_scores[7:]))
            
            if recent_avg > older_avg + 0.5:
                print("📈 Trend: Your mood is IMPROVING!")
            elif recent_avg < older_avg - 0.5:
                print("📉 Trend: Your mood has been declining. Consider seeking support.")
            else:
                print("📊 Trend: Your mood is relatively STABLE.")
        
        print()
        input("Press Enter to continue...")
        print()
    
    def show_ai_insights(self):
        """Show AI insights and recommendations"""
        print("\n--- AI INSIGHTS & RECOMMENDATIONS ---")
        entries = self.db.get_mood_entries(self.current_user_id, 30)
        
        if len(entries) < 3:
            print("🤖 AI: Keep logging your mood daily to get personalized insights!")
            print()
            return
        
        print("🤖 AI Analysis:")
        print("-" * 40)
        
        # Analyze recent data
        recent_entries = entries[:7]
        mood_scores = [entry[0] for entry in recent_entries]
        sleep_hours = [entry[4] for entry in recent_entries if entry[4]]
        stress_levels = [entry[5] for entry in recent_entries if entry[5]]
        
        avg_mood = sum(mood_scores) / len(mood_scores)
        avg_sleep = sum(sleep_hours) / len(sleep_hours) if sleep_hours else 7.5
        avg_stress = sum(stress_levels) / len(stress_levels) if stress_levels else 5
        
        # Generate insights
        if avg_mood >= 7:
            print("✨ You've been maintaining good mental health! Keep it up!")
        elif avg_mood >= 5:
            print("💛 Your mood is in the moderate range. Consider mood-boosting activities.")
        else:
            print("💙 Your mood has been low. Please consider reaching out for support.")
        
        # Sleep insights
        if avg_sleep < 7:
            print(f"😴 You're averaging {avg_sleep:.1f}h sleep. Aim for 7-9h for better mood.")
        elif avg_sleep >= 8:
            print(f"🌙 Great sleep habits! {avg_sleep:.1f}h average supports good mental health.")
        
        # Stress insights
        if avg_stress >= 7:
            print("⚠️ High stress detected. Try meditation, exercise, or talking to someone.")
        
        # Recommendations
        print("\n💡 RECOMMENDATIONS:")
        print("• Continue daily mood tracking")
        print("• Maintain consistent sleep schedule")
        print("• Practice stress management techniques")
        print("• Engage in physical activity")
        print("• Connect with supportive people")
        print("• Consider professional help if mood stays low")
        
        print()
        input("Press Enter to continue...")
        print()
    
    def show_demo_data(self):
        """Show demo data without login"""
        print("\n--- DEMO DATA SHOWCASE ---")
        print("This is what the Mental Health Tracker can do:")
        print()
        
        demo_entries = [
            (8, ['happy', 'grateful'], 'Great day at work!', 7, 8.0, 3),
            (6, ['calm', 'content'], 'Relaxing weekend', 6, 7.5, 4),
            (4, ['anxious', 'stressed'], 'Busy day with deadlines', 4, 6.0, 8),
            (7, ['excited', 'happy'], 'Celebrated with friends', 8, 7.0, 2),
            (5, ['sad', 'tired'], 'Long week, feeling drained', 3, 5.5, 7),
        ]
        
        print("📊 SAMPLE MOOD ENTRIES:")
        print("-" * 60)
        
        for i, (mood, emotions, notes, energy, sleep, stress) in enumerate(demo_entries, 1):
            print(f"Day {i}: Mood {mood}/10 | Energy {energy}/10 | Stress {stress}/10 | Sleep {sleep}h")
            print(f"       Emotions: {', '.join(emotions)}")
            print(f"       Notes: {notes}")
            print()
        
        # Calculate demo analytics
        avg_mood = sum(entry[0] for entry in demo_entries) / len(demo_entries)
        avg_sleep = sum(entry[4] for entry in demo_entries) / len(demo_entries)
        avg_stress = sum(entry[5] for entry in demo_entries) / len(demo_entries)
        
        print("📈 DEMO ANALYTICS:")
        print(f"Average Mood: {avg_mood:.1f}/10")
        print(f"Average Sleep: {avg_sleep:.1f} hours")
        print(f"Average Stress: {avg_stress:.1f}/10")
        
        print("\n🤖 AI DEMO INSIGHTS:")
        print("• Your mood varies with sleep quality")
        print("• High stress days correlate with lower mood")
        print("• Social activities boost your mood")
        print("• Consider stress management on busy days")
        
        print()
        input("Press Enter to continue...")
        print()
    
    def logout(self):
        """Logout current user"""
        print(f"Goodbye, {self.current_username}! Take care! 💚\n")
        self.current_user_id = None
        self.current_username = None


if __name__ == "__main__":
    app = MentalHealthTracker()
    try:
        app.run_demo()
    except KeyboardInterrupt:
        print("\n\nThanks for using Mental Health Tracker! 💚")
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Don't worry, this is just a demo! The full web app would handle this gracefully.")