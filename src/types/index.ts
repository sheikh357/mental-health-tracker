// User Types
export interface User {
  id: string;
  email: string;
  name?: string;
  created_at: Date;
  updated_at: Date;
  preferences: UserPreferences;
}

export interface UserPreferences {
  notifications: boolean;
  reminder_time: string;
  theme: 'light' | 'dark' | 'auto';
  ai_insights: boolean;
  insight_frequency: 'daily' | 'weekly' | 'monthly';
  privacy_level: 'minimal' | 'standard' | 'enhanced';
}

// Mood Types
export interface MoodEntry {
  id: string;
  user_id: string;
  mood_value: number; // 1-10 scale
  mood_label: string; // 'happy', 'sad', 'anxious', etc.
  notes?: string;
  created_at: Date;
  updated_at: Date;
}

export interface MoodTrend {
  date: string;
  mood_value: number;
  mood_label: string;
}

// Journal Types
export interface JournalEntry {
  id: string;
  user_id: string;
  title?: string;
  content: string;
  mood_id?: string; // Optional linked mood
  ai_analysis?: AIAnalysis;
  is_private: boolean;
  created_at: Date;
  updated_at: Date;
}

export interface AIAnalysis {
  sentiment: number; // -1 to 1 scale
  themes: string[];
  insights: string[];
  keywords: string[];
  emotion_scores: {
    joy: number;
    sadness: number;
    anger: number;
    fear: number;
    surprise: number;
    disgust: number;
  };
}

// Analytics Types
export interface UserAnalytics {
  user_id: string;
  mood_average: number;
  mood_trend: 'improving' | 'stable' | 'declining';
  journal_frequency: number; // entries per week
  most_common_mood: string;
  most_common_themes: string[];
  streak_days: number;
  total_entries: number;
  generated_at: Date;
}

export interface InsightData {
  id: string;
  user_id: string;
  type: 'pattern' | 'recommendation' | 'achievement' | 'concern';
  title: string;
  description: string;
  confidence: number; // 0-1 scale
  data_points: string[]; // References to supporting data
  created_at: Date;
  is_read: boolean;
}

// API Response Types
export interface ApiResponse<T> {
  success: boolean;
  data?: T;
  error?: string;
  message?: string;
}

export interface PaginatedResponse<T> {
  data: T[];
  pagination: {
    current_page: number;
    total_pages: number;
    total_items: number;
    items_per_page: number;
  };
}

// Form Types
export interface MoodCheckInForm {
  mood_value: number;
  mood_label: string;
  notes?: string;
}

export interface JournalEntryForm {
  title?: string;
  content: string;
  mood_id?: string;
  is_private: boolean;
}

export interface UserPreferencesForm {
  notifications: boolean;
  reminder_time: string;
  theme: 'light' | 'dark' | 'auto';
  ai_insights: boolean;
  insight_frequency: 'daily' | 'weekly' | 'monthly';
  privacy_level: 'minimal' | 'standard' | 'enhanced';
}

// Chart Data Types
export interface ChartDataPoint {
  date: string;
  value: number;
  label?: string;
}

export interface MoodChartData {
  labels: string[];
  datasets: {
    label: string;
    data: number[];
    borderColor: string;
    backgroundColor: string;
  }[];
}

// n8n Workflow Types
export interface WorkflowTrigger {
  user_id: string;
  journal_entry_id?: string;
  mood_entry_id?: string;
  trigger_type: 'journal_analysis' | 'mood_pattern' | 'weekly_insight';
  data: Record<string, any>;
}

export interface WorkflowResponse {
  success: boolean;
  insights?: string[];
  recommendations?: string[];
  sentiment_score?: number;
  themes?: string[];
  error?: string;
}

// Resource Types
export interface MentalHealthResource {
  id: string;
  title: string;
  description: string;
  type: 'article' | 'video' | 'exercise' | 'tool' | 'crisis';
  category: 'anxiety' | 'depression' | 'stress' | 'sleep' | 'general';
  url?: string;
  content?: string;
  duration?: number; // in minutes
  difficulty: 'beginner' | 'intermediate' | 'advanced';
  is_crisis: boolean;
  created_at: Date;
  updated_at: Date;
}