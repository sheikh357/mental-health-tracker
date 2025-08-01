import unittest
from datetime import datetime, timedelta
from ai_analysis.mood_analyzer import MoodAnalyzer
from app import MoodEntry, User
import json


class MockMoodEntry:
    """Mock mood entry for testing"""
    def __init__(self, created_at, mood_score, energy_level=5, stress_level=5, 
                 sleep_hours=7.5, emotions=None, notes=''):
        self.created_at = created_at
        self.mood_score = mood_score
        self.energy_level = energy_level
        self.stress_level = stress_level
        self.sleep_hours = sleep_hours
        self.emotions = json.dumps(emotions) if emotions else '[]'
        self.notes = notes


class MoodAnalyzerTestCase(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures"""
        self.analyzer = MoodAnalyzer()
    
    def test_sentiment_analysis(self):
        """Test sentiment analysis functionality"""
        # Positive text
        result = self.analyzer.analyze_sentiment("I had a wonderful day today!")
        self.assertGreater(result['polarity'], 0)
        
        # Negative text
        result = self.analyzer.analyze_sentiment("I feel terrible and sad.")
        self.assertLess(result['polarity'], 0)
        
        # Neutral text
        result = self.analyzer.analyze_sentiment("I went to the store.")
        self.assertAlmostEqual(result['polarity'], 0, delta=0.3)
        
        # Empty text
        result = self.analyzer.analyze_sentiment("")
        self.assertEqual(result['polarity'], 0)
    
    def test_emotion_score_calculation(self):
        """Test emotion score calculation"""
        # Positive emotions
        score = self.analyzer.calculate_emotion_score(['happy', 'excited'])
        self.assertGreater(score, 0)
        
        # Negative emotions
        score = self.analyzer.calculate_emotion_score(['sad', 'angry'])
        self.assertLess(score, 0)
        
        # Mixed emotions
        score = self.analyzer.calculate_emotion_score(['happy', 'sad'])
        self.assertEqual(score, 0)
        
        # Empty emotions
        score = self.analyzer.calculate_emotion_score([])
        self.assertEqual(score, 0)
    
    def test_mood_patterns_insufficient_data(self):
        """Test pattern analysis with insufficient data"""
        # Less than 7 entries
        entries = [
            MockMoodEntry(datetime.now() - timedelta(days=i), 7)
            for i in range(3)
        ]
        
        result = self.analyzer.find_mood_patterns(entries)
        self.assertEqual(len(result['patterns']), 0)
        self.assertEqual(len(result['insights']), 0)
    
    def test_mood_patterns_weekly(self):
        """Test weekly pattern detection"""
        # Create entries for different days of the week
        entries = []
        base_date = datetime(2024, 1, 1)  # Monday
        
        # Mondays (good mood)
        for week in range(3):
            entries.append(MockMoodEntry(
                base_date + timedelta(weeks=week), 9
            ))
        
        # Fridays (bad mood)
        for week in range(3):
            entries.append(MockMoodEntry(
                base_date + timedelta(days=4, weeks=week), 3
            ))
        
        # Add some other days with average mood
        for i in range(5):
            entries.append(MockMoodEntry(
                base_date + timedelta(days=1 + i), 6
            ))
        
        result = self.analyzer.find_mood_patterns(entries)
        # Should detect weekly pattern
        self.assertGreater(len(result['patterns']), 0)
    
    def test_sleep_correlation(self):
        """Test sleep-mood correlation detection"""
        entries = []
        base_date = datetime.now()
        
        # Good sleep, good mood
        for i in range(5):
            entries.append(MockMoodEntry(
                base_date - timedelta(days=i),
                mood_score=8,
                sleep_hours=8.5
            ))
        
        # Poor sleep, poor mood
        for i in range(5, 10):
            entries.append(MockMoodEntry(
                base_date - timedelta(days=i),
                mood_score=4,
                sleep_hours=5.0
            ))
        
        result = self.analyzer.find_mood_patterns(entries)
        
        # Should detect positive correlation between sleep and mood
        sleep_insights = [i for i in result['insights'] if i['category'] == 'sleep']
        self.assertGreater(len(sleep_insights), 0)
    
    def test_trend_analysis(self):
        """Test mood trend analysis"""
        entries = []
        base_date = datetime.now()
        
        # Declining trend
        for i in range(14):
            mood_score = 8 - (i * 0.3)  # Gradually declining
            entries.append(MockMoodEntry(
                base_date - timedelta(days=13-i),
                max(1, int(mood_score))
            ))
        
        result = self.analyzer.find_mood_patterns(entries)
        
        # Should detect declining trend
        trend_insights = [i for i in result['insights'] if i['category'] == 'trend']
        self.assertGreater(len(trend_insights), 0)
    
    def test_recommendations_low_mood(self):
        """Test recommendations for low mood"""
        entries = []
        base_date = datetime.now()
        
        # Create entries with consistently low mood
        for i in range(7):
            entries.append(MockMoodEntry(
                base_date - timedelta(days=i),
                mood_score=3,
                stress_level=8,
                sleep_hours=5.0
            ))
        
        recommendations = self.analyzer.generate_recommendations(entries)
        
        # Should include recommendations for sleep, stress, and support
        categories = [r['category'] for r in recommendations]
        self.assertIn('sleep', categories)
        self.assertIn('stress', categories)
        self.assertIn('support', categories)
    
    def test_recommendations_good_mood(self):
        """Test recommendations for good mood"""
        entries = []
        base_date = datetime.now()
        
        # Create entries with consistently good mood
        for i in range(7):
            entries.append(MockMoodEntry(
                base_date - timedelta(days=i),
                mood_score=8,
                stress_level=3,
                sleep_hours=8.0
            ))
        
        recommendations = self.analyzer.generate_recommendations(entries)
        
        # Should include positive reinforcement
        categories = [r['category'] for r in recommendations]
        self.assertIn('positive', categories)
    
    def test_recommendations_insufficient_data(self):
        """Test recommendations with insufficient data"""
        entries = [MockMoodEntry(datetime.now(), 6)]
        
        recommendations = self.analyzer.generate_recommendations(entries)
        
        # Should return general recommendation to keep tracking
        self.assertEqual(len(recommendations), 1)
        self.assertEqual(recommendations[0]['category'], 'general')


if __name__ == '__main__':
    unittest.main()