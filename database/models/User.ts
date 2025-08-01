import { Schema, model, models } from 'mongoose'
import type { User, UserPreferences } from '@/types'

const UserPreferencesSchema = new Schema<UserPreferences>({
  notifications: { type: Boolean, default: true },
  reminder_time: { type: String, default: '20:00' },
  theme: { type: String, enum: ['light', 'dark', 'auto'], default: 'light' },
  ai_insights: { type: Boolean, default: true },
  insight_frequency: { type: String, enum: ['daily', 'weekly', 'monthly'], default: 'weekly' },
  privacy_level: { type: String, enum: ['minimal', 'standard', 'enhanced'], default: 'standard' },
})

const UserSchema = new Schema<User>({
  id: { type: String, required: true, unique: true, index: true },
  email: { type: String, required: true, unique: true, lowercase: true },
  name: { type: String, trim: true },
  preferences: { type: UserPreferencesSchema, default: () => ({}) },
  created_at: { type: Date, default: Date.now },
  updated_at: { type: Date, default: Date.now },
})

// Middleware to update the updated_at field
UserSchema.pre('save', function(next) {
  this.updated_at = new Date()
  next()
})

// Create indexes for better query performance
UserSchema.index({ email: 1 })
UserSchema.index({ created_at: -1 })

export const UserModel = models.User || model<User>('User', UserSchema)