import { Schema, model, models } from 'mongoose'
import type { MoodEntry } from '@/types'

const MoodEntrySchema = new Schema<MoodEntry>({
  id: { type: String, required: true, unique: true, index: true },
  user_id: { type: String, required: true, index: true },
  mood_value: { 
    type: Number, 
    required: true, 
    min: 1, 
    max: 10,
    validate: {
      validator: Number.isInteger,
      message: 'Mood value must be an integer between 1 and 10'
    }
  },
  mood_label: { 
    type: String, 
    required: true,
    enum: ['great', 'good', 'okay', 'sad', 'angry', 'anxious', 'excited', 'tired', 'content', 'frustrated'],
    lowercase: true
  },
  notes: { type: String, maxlength: 500 },
  created_at: { type: Date, default: Date.now, index: true },
  updated_at: { type: Date, default: Date.now },
})

// Middleware to update the updated_at field
MoodEntrySchema.pre('save', function(next) {
  this.updated_at = new Date()
  next()
})

// Create compound indexes for better query performance
MoodEntrySchema.index({ user_id: 1, created_at: -1 })
MoodEntrySchema.index({ user_id: 1, mood_value: 1 })
MoodEntrySchema.index({ user_id: 1, mood_label: 1 })

// Virtual for mood category based on value
MoodEntrySchema.virtual('mood_category').get(function() {
  if (this.mood_value >= 8) return 'positive'
  if (this.mood_value >= 6) return 'neutral'
  if (this.mood_value >= 4) return 'low'
  return 'negative'
})

export const MoodEntryModel = models.MoodEntry || model<MoodEntry>('MoodEntry', MoodEntrySchema)