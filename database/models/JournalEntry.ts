import { Schema, model, models } from 'mongoose'
import type { JournalEntry, AIAnalysis } from '@/types'

const EmotionScoresSchema = new Schema({
  joy: { type: Number, min: 0, max: 1, default: 0 },
  sadness: { type: Number, min: 0, max: 1, default: 0 },
  anger: { type: Number, min: 0, max: 1, default: 0 },
  fear: { type: Number, min: 0, max: 1, default: 0 },
  surprise: { type: Number, min: 0, max: 1, default: 0 },
  disgust: { type: Number, min: 0, max: 1, default: 0 },
}, { _id: false })

const AIAnalysisSchema = new Schema<AIAnalysis>({
  sentiment: { 
    type: Number, 
    min: -1, 
    max: 1,
    validate: {
      validator: (v: number) => v >= -1 && v <= 1,
      message: 'Sentiment score must be between -1 and 1'
    }
  },
  themes: [{ type: String, maxlength: 50 }],
  insights: [{ type: String, maxlength: 200 }],
  keywords: [{ type: String, maxlength: 30 }],
  emotion_scores: { type: EmotionScoresSchema, default: () => ({}) },
}, { _id: false })

const JournalEntrySchema = new Schema<JournalEntry>({
  id: { type: String, required: true, unique: true, index: true },
  user_id: { type: String, required: true, index: true },
  title: { type: String, maxlength: 100, trim: true },
  content: { 
    type: String, 
    required: true, 
    minlength: 10,
    maxlength: 10000,
    validate: {
      validator: (v: string) => v.trim().length >= 10,
      message: 'Content must be at least 10 characters long'
    }
  },
  mood_id: { type: String, index: true },
  ai_analysis: { type: AIAnalysisSchema },
  is_private: { type: Boolean, default: true },
  created_at: { type: Date, default: Date.now, index: true },
  updated_at: { type: Date, default: Date.now },
})

// Middleware to update the updated_at field
JournalEntrySchema.pre('save', function(next) {
  this.updated_at = new Date()
  next()
})

// Create compound indexes for better query performance
JournalEntrySchema.index({ user_id: 1, created_at: -1 })
JournalEntrySchema.index({ user_id: 1, is_private: 1 })
JournalEntrySchema.index({ user_id: 1, 'ai_analysis.sentiment': 1 })

// Text index for search functionality
JournalEntrySchema.index({ 
  title: 'text', 
  content: 'text', 
  'ai_analysis.themes': 'text',
  'ai_analysis.keywords': 'text'
})

// Virtual for word count
JournalEntrySchema.virtual('word_count').get(function() {
  return this.content.trim().split(/\s+/).length
})

// Virtual for reading time (assumes 200 words per minute)
JournalEntrySchema.virtual('reading_time_minutes').get(function() {
  const wordCount = this.content.trim().split(/\s+/).length
  return Math.ceil(wordCount / 200)
})

export const JournalEntryModel = models.JournalEntry || model<JournalEntry>('JournalEntry', JournalEntrySchema)