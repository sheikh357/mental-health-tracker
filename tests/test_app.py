import unittest
import json
from app import app, db, User, MoodEntry
from werkzeug.security import generate_password_hash


class MentalHealthTrackerTestCase(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures"""
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()
        
        db.create_all()
        
        # Create test user
        self.test_user = User(
            username='testuser',
            email='test@example.com',
            password_hash=generate_password_hash('testpass123')
        )
        db.session.add(self.test_user)
        db.session.commit()
    
    def tearDown(self):
        """Clean up test fixtures"""
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
    
    def login(self):
        """Helper method to log in test user"""
        return self.app.post('/login', data={
            'username': 'testuser',
            'password': 'testpass123'
        }, follow_redirects=True)
    
    def test_index_page(self):
        """Test the index page loads correctly"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Mental Health Tracker', response.data)
    
    def test_user_registration(self):
        """Test user registration"""
        response = self.app.post('/register', data={
            'username': 'newuser',
            'email': 'new@example.com',
            'password': 'newpass123'
        }, follow_redirects=True)
        
        self.assertEqual(response.status_code, 200)
        # Check if user was created
        user = User.query.filter_by(username='newuser').first()
        self.assertIsNotNone(user)
    
    def test_duplicate_user_registration(self):
        """Test registration with existing username"""
        response = self.app.post('/register', data={
            'username': 'testuser',  # Already exists
            'email': 'another@example.com',
            'password': 'anotherpass123'
        })
        
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Username already exists', response.data)
    
    def test_user_login(self):
        """Test user login"""
        response = self.login()
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome back', response.data)
    
    def test_invalid_login(self):
        """Test login with invalid credentials"""
        response = self.app.post('/login', data={
            'username': 'testuser',
            'password': 'wrongpassword'
        })
        
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Invalid username or password', response.data)
    
    def test_mood_logging_requires_login(self):
        """Test that mood logging requires authentication"""
        response = self.app.get('/log-mood')
        self.assertEqual(response.status_code, 302)  # Redirect to login
    
    def test_mood_logging_page(self):
        """Test mood logging page loads when authenticated"""
        self.login()
        response = self.app.get('/log-mood')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Log Your Mood', response.data)
    
    def test_mood_entry_creation(self):
        """Test creating a mood entry"""
        self.login()
        
        mood_data = {
            'mood_score': 8,
            'energy_level': 7,
            'stress_level': 3,
            'sleep_hours': 8.0,
            'emotions': ['happy', 'calm'],
            'notes': 'Had a great day!'
        }
        
        response = self.app.post('/log-mood', 
                                data=json.dumps(mood_data),
                                content_type='application/json')
        
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data['success'])
        
        # Check if mood entry was created
        entry = MoodEntry.query.filter_by(user_id=self.test_user.id).first()
        self.assertIsNotNone(entry)
        self.assertEqual(entry.mood_score, 8)
        self.assertEqual(entry.energy_level, 7)
    
    def test_dashboard_requires_login(self):
        """Test that dashboard requires authentication"""
        response = self.app.get('/dashboard')
        self.assertEqual(response.status_code, 302)  # Redirect to login
    
    def test_dashboard_loads(self):
        """Test dashboard loads when authenticated"""
        self.login()
        response = self.app.get('/dashboard')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome back', response.data)
    
    def test_mood_data_api(self):
        """Test mood data API endpoint"""
        self.login()
        
        # Create test mood entry
        entry = MoodEntry(
            user_id=self.test_user.id,
            mood_score=7,
            energy_level=6,
            stress_level=4,
            emotions=json.dumps(['happy']),
            notes='Test entry'
        )
        db.session.add(entry)
        db.session.commit()
        
        response = self.app.get('/api/mood-data?days=7')
        self.assertEqual(response.status_code, 200)
        
        data = json.loads(response.data)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['mood_score'], 7)
    
    def test_analytics_page(self):
        """Test analytics page loads when authenticated"""
        self.login()
        response = self.app.get('/analytics')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Analytics', response.data)
    
    def test_logout(self):
        """Test user logout"""
        self.login()
        response = self.app.get('/logout', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        
        # Try to access protected page
        response = self.app.get('/dashboard')
        self.assertEqual(response.status_code, 302)  # Should redirect to login


if __name__ == '__main__':
    unittest.main()