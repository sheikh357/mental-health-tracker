"""
AI Analysis Module for Mental Health Tracker
Provides basic sentiment analysis and pattern recognition for mood data
"""

import json
from collections import defaultdict, Counter
from datetime import datetime, timedelta


class MoodAnalyzer:
    """Analyzes mood patterns and provides insights"""
    
    def __init__(self):
        self.emotion_weights = {
            'happy': 2,
            'excited': 2,
            'grateful': 2,
            'calm': 1,
            'sad': -2,
            'angry': -2,
            'anxious': -1,
            'stressed': -1
        }
        
        # Simple sentiment word lists for basic analysis
        self.positive_words = {'good', 'great', 'excellent', 'happy', 'wonderful', 'amazing', 'fantastic', 'love', 'joy', 'perfect'}
        self.negative_words = {'bad', 'terrible', 'awful', 'horrible', 'hate', 'worst', 'sad', 'depressed', 'angry', 'frustrated'}
    
    def analyze_sentiment(self, text):
        """Basic sentiment analysis of text notes"""
        if not text:
            return {'polarity': 0, 'subjectivity': 0}
        
        text_lower = text.lower()
        words = text_lower.split()
        
        positive_count = sum(1 for word in words if word in self.positive_words)
        negative_count = sum(1 for word in words if word in self.negative_words)
        
        total_sentiment_words = positive_count + negative_count
        if total_sentiment_words == 0:
            polarity = 0
            subjectivity = 0
        else:
            polarity = (positive_count - negative_count) / len(words)
            subjectivity = total_sentiment_words / len(words)
        
        return {
            'polarity': max(-1, min(1, polarity)),  # Clamp to [-1, 1]
            'subjectivity': max(0, min(1, subjectivity))  # Clamp to [0, 1]
        }
    
    def calculate_emotion_score(self, emotions):
        """Calculate weighted emotion score"""
        if not emotions:
            return 0
        
        total_weight = 0
        for emotion in emotions:
            total_weight += self.emotion_weights.get(emotion, 0)
        
        return total_weight / len(emotions) if emotions else 0
    
    def find_mood_patterns(self, mood_entries):
        """Find patterns in mood data"""
        if len(mood_entries) < 7:
            return {'patterns': [], 'insights': []}
        
        # Convert to simple data structure
        data = []
        for entry in mood_entries:
            emotions_list = json.loads(entry.emotions) if entry.emotions else []
            data.append({
                'date': entry.created_at,
                'mood_score': entry.mood_score,
                'energy_level': entry.energy_level or 5,
                'stress_level': entry.stress_level or 5,
                'sleep_hours': entry.sleep_hours or 7.5,
                'emotions': emotions_list,
                'notes': entry.notes or ''
            })
        
        patterns = []
        insights = []
        
        # Weekly patterns
        day_mood_data = defaultdict(list)
        for item in data:
            day_of_week = item['date'].strftime('%A')
            day_mood_data[day_of_week].append(item['mood_score'])
        
        # Calculate averages for each day
        day_averages = {}
        for day, moods in day_mood_data.items():
            if len(moods) >= 2:  # At least 2 data points
                day_averages[day] = sum(moods) / len(moods)
        
        if len(day_averages) >= 3:
            best_day = max(day_averages, key=day_averages.get)
            worst_day = min(day_averages, key=day_averages.get)
            
            if day_averages[best_day] - day_averages[worst_day] > 1:
                patterns.append({
                    'type': 'weekly',
                    'description': f'You tend to feel best on {best_day}s (avg: {day_averages[best_day]:.1f}) and worst on {worst_day}s (avg: {day_averages[worst_day]:.1f})'
                })
        
        # Sleep correlation analysis
        sleep_mood_pairs = [(item['sleep_hours'], item['mood_score']) 
                           for item in data if item['sleep_hours'] is not None]
        
        if len(sleep_mood_pairs) > 5:
            # Simple correlation calculation
            sleep_values = [pair[0] for pair in sleep_mood_pairs]
            mood_values = [pair[1] for pair in sleep_mood_pairs]
            
            sleep_mean = sum(sleep_values) / len(sleep_values)
            mood_mean = sum(mood_values) / len(mood_values)
            
            numerator = sum((s - sleep_mean) * (m - mood_mean) 
                          for s, m in zip(sleep_values, mood_values))
            sleep_var = sum((s - sleep_mean)**2 for s in sleep_values)
            mood_var = sum((m - mood_mean)**2 for m in mood_values)
            
            if sleep_var > 0 and mood_var > 0:
                correlation = numerator / (sleep_var * mood_var)**0.5
                
                if abs(correlation) > 0.3:
                    if correlation > 0:
                        insights.append({
                            'type': 'positive',
                            'category': 'sleep',
                            'description': f'Better sleep is correlated with better mood (correlation: {correlation:.2f})'
                        })
                    else:
                        insights.append({
                            'type': 'neutral',
                            'category': 'sleep',
                            'description': f'Sleep patterns may be affecting your mood (correlation: {correlation:.2f})'
                        })
        
        # Stress correlation
        stress_mood_pairs = [(item['stress_level'], item['mood_score']) 
                            for item in data if item['stress_level'] is not None]
        
        if len(stress_mood_pairs) > 5:
            stress_values = [pair[0] for pair in stress_mood_pairs]
            mood_values = [pair[1] for pair in stress_mood_pairs]
            
            stress_mean = sum(stress_values) / len(stress_values)
            mood_mean = sum(mood_values) / len(mood_values)
            
            numerator = sum((s - stress_mean) * (m - mood_mean) 
                          for s, m in zip(stress_values, mood_values))
            stress_var = sum((s - stress_mean)**2 for s in stress_values)
            mood_var = sum((m - mood_mean)**2 for m in mood_values)
            
            if stress_var > 0 and mood_var > 0:
                correlation = numerator / (stress_var * mood_var)**0.5
                
                if correlation < -0.3:
                    insights.append({
                        'type': 'warning',
                        'category': 'stress',
                        'description': f'High stress levels are negatively impacting your mood (correlation: {correlation:.2f})'
                    })
        
        # Trend analysis
        if len(data) >= 14:
            recent_data = data[-7:]
            older_data = data[:-7][-7:]  # Previous 7 days
            
            recent_avg = sum(item['mood_score'] for item in recent_data) / len(recent_data)
            older_avg = sum(item['mood_score'] for item in older_data) / len(older_data)
            trend = recent_avg - older_avg
            
            if trend > 0.5:
                insights.append({
                    'type': 'positive',
                    'category': 'trend',
                    'description': f'Your mood is improving! Recent average: {recent_avg:.1f} vs previous: {older_avg:.1f}'
                })
            elif trend < -0.5:
                insights.append({
                    'type': 'warning',
                    'category': 'trend',
                    'description': f'Your mood has been declining recently. Consider seeking support or trying stress management techniques.'
                })
        
        # Emotion patterns
        all_emotions = []
        for item in data:
            all_emotions.extend(item['emotions'])
        
        if all_emotions:
            emotion_counts = Counter(all_emotions)
            most_common = emotion_counts.most_common(1)[0]
            emotion_name, count = most_common
            
            if emotion_name in ['sad', 'anxious', 'stressed', 'angry'] and count > len(data) * 0.3:
                insights.append({
                    'type': 'warning',
                    'category': 'emotion',
                    'description': f'You\'ve been feeling {emotion_name} frequently. Consider talking to someone or practicing self-care.'
                })
            elif emotion_name in ['happy', 'grateful', 'excited', 'calm']:
                insights.append({
                    'type': 'positive',
                    'category': 'emotion',
                    'description': f'Great to see you\'re feeling {emotion_name} often! Keep up whatever you\'re doing.'
                })
        
        return {
            'patterns': patterns,
            'insights': insights
        }
    
    def generate_recommendations(self, mood_entries, user_data=None):
        """Generate personalized recommendations based on mood data"""
        recommendations = []
        
        if len(mood_entries) < 3:
            return [
                {
                    'category': 'general',
                    'title': 'Keep Tracking',
                    'description': 'Continue logging your mood daily to get personalized insights and recommendations.',
                    'priority': 'medium'
                }
            ]
        
        # Analyze recent mood data
        recent_entries = mood_entries[-7:]
        recent_moods = [entry.mood_score for entry in recent_entries]
        avg_recent_mood = sum(recent_moods) / len(recent_moods)
        
        recent_sleep = [entry.sleep_hours for entry in recent_entries if entry.sleep_hours]
        avg_sleep = sum(recent_sleep) / len(recent_sleep) if recent_sleep else 7.5
        
        recent_stress = [entry.stress_level for entry in recent_entries if entry.stress_level]
        avg_stress = sum(recent_stress) / len(recent_stress) if recent_stress else 5
        
        # Sleep recommendations
        if avg_sleep < 7:
            recommendations.append({
                'category': 'sleep',
                'title': 'Improve Sleep Quality',
                'description': f'You\'re averaging {avg_sleep:.1f} hours of sleep. Try to aim for 7-9 hours for better mood and energy.',
                'priority': 'high'
            })
        
        # Stress management
        if avg_stress > 7:
            recommendations.append({
                'category': 'stress',
                'title': 'Manage Stress Levels',
                'description': 'Your stress levels have been high. Consider meditation, deep breathing, or talking to someone.',
                'priority': 'high'
            })
        
        # Low mood support
        if avg_recent_mood < 5:
            recommendations.append({
                'category': 'support',
                'title': 'Seek Support',
                'description': 'Your mood has been low recently. Consider reaching out to friends, family, or a mental health professional.',
                'priority': 'high'
            })
        
        # Activity recommendations
        if avg_recent_mood < 7:
            recommendations.append({
                'category': 'activity',
                'title': 'Try Mood-Boosting Activities',
                'description': 'Consider activities like exercise, spending time in nature, or pursuing hobbies you enjoy.',
                'priority': 'medium'
            })
        
        # Positive reinforcement
        if avg_recent_mood > 7:
            recommendations.append({
                'category': 'positive',
                'title': 'Keep It Up!',
                'description': 'You\'re doing great! Continue with whatever strategies are working for you.',
                'priority': 'low'
            })
        
        return recommendations


# Singleton instance
mood_analyzer = MoodAnalyzer()