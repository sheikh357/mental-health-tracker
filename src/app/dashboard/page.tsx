'use client'

import { useState } from 'react'
import Link from 'next/link'

const MOOD_OPTIONS = [
  { emoji: '😊', label: 'Great', value: 9, color: 'text-green-500' },
  { emoji: '🙂', label: 'Good', value: 7, color: 'text-blue-500' },
  { emoji: '😐', label: 'Okay', value: 5, color: 'text-yellow-500' },
  { emoji: '😔', label: 'Sad', value: 3, color: 'text-orange-500' },
  { emoji: '😢', label: 'Down', value: 1, color: 'text-red-500' },
]

export default function DashboardPage() {
  const [selectedMood, setSelectedMood] = useState<number | null>(null)
  const [moodSubmitted, setMoodSubmitted] = useState(false)

  const handleMoodSelect = async (moodValue: number) => {
    setSelectedMood(moodValue)
    // Simulate API call
    await new Promise(resolve => setTimeout(resolve, 500))
    setMoodSubmitted(true)
  }

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Navigation */}
      <nav className="bg-white shadow-sm border-b">
        <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between h-16">
            <div className="flex items-center">
              <Link href="/" className="text-xl font-bold text-primary-500">
                Mental Health Tracker
              </Link>
            </div>
            
            <div className="hidden md:flex items-center space-x-8">
              <Link href="/dashboard" className="text-primary-500 font-medium">Dashboard</Link>
              <Link href="/journal" className="text-gray-600 hover:text-gray-900">Journal</Link>
              <Link href="/analytics" className="text-gray-600 hover:text-gray-900">Analytics</Link>
              <Link href="/resources" className="text-gray-600 hover:text-gray-900">Resources</Link>
              <Link href="/profile" className="text-gray-600 hover:text-gray-900">Profile</Link>
            </div>
            
            <div className="flex items-center">
              <button className="text-gray-600 hover:text-gray-900">
                <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1" />
                </svg>
              </button>
            </div>
          </div>
        </div>
      </nav>

      {/* Main Content */}
      <main className="max-w-6xl mx-auto py-8 px-4 sm:px-6 lg:px-8">
        {/* Welcome Section */}
        <div className="mb-8">
          <h1 className="text-3xl font-bold text-gray-900 mb-2">
            Good morning, Alex! 👋
          </h1>
          <p className="text-gray-600">How are you feeling today?</p>
        </div>

        {/* Mood Check-in */}
        <div className="card mb-8">
          <h2 className="text-xl font-semibold mb-6">Daily Mood Check-in</h2>
          
          {!moodSubmitted ? (
            <div className="grid grid-cols-2 md:grid-cols-5 gap-4">
              {MOOD_OPTIONS.map((mood) => (
                <button
                  key={mood.value}
                  onClick={() => handleMoodSelect(mood.value)}
                  className={`p-4 rounded-lg border-2 hover:border-primary-300 transition-all ${
                    selectedMood === mood.value ? 'border-primary-500 bg-primary-50' : 'border-gray-200'
                  }`}
                  disabled={selectedMood !== null}
                >
                  <div className="text-3xl mb-2">{mood.emoji}</div>
                  <div className="font-medium">{mood.label}</div>
                  <div className={`text-sm ${mood.color}`}>({mood.value})</div>
                </button>
              ))}
            </div>
          ) : (
            <div className="text-center py-8">
              <div className="text-4xl mb-4">✅</div>
              <h3 className="text-xl font-semibold mb-2">Mood logged successfully!</h3>
              <p className="text-gray-600">Thank you for checking in today.</p>
            </div>
          )}
        </div>

        <div className="grid md:grid-cols-3 gap-6 mb-8">
          {/* Quick Actions */}
          <div className="card">
            <h3 className="text-lg font-semibold mb-4">Quick Actions</h3>
            <div className="space-y-3">
              <Link href="/journal/new" className="block w-full text-left p-3 rounded-lg bg-gray-50 hover:bg-gray-100 transition-colors">
                <div className="flex items-center">
                  <span className="text-xl mr-3">📝</span>
                  <span>New Journal Entry</span>
                </div>
              </Link>
              <Link href="/analytics" className="block w-full text-left p-3 rounded-lg bg-gray-50 hover:bg-gray-100 transition-colors">
                <div className="flex items-center">
                  <span className="text-xl mr-3">📊</span>
                  <span>View Analytics</span>
                </div>
              </Link>
              <Link href="/resources" className="block w-full text-left p-3 rounded-lg bg-gray-50 hover:bg-gray-100 transition-colors">
                <div className="flex items-center">
                  <span className="text-xl mr-3">📚</span>
                  <span>Browse Resources</span>
                </div>
              </Link>
            </div>
          </div>

          {/* Today's Insights */}
          <div className="md:col-span-2 card">
            <h3 className="text-lg font-semibold mb-4">Today's AI Insights</h3>
            <div className="bg-blue-50 border border-blue-200 rounded-lg p-4">
              <p className="text-blue-800 mb-3">
                "You've been consistently logging positive moods this week. Consider reflecting on 
                what's contributing to this positive trend in your journal."
              </p>
              <button className="text-blue-600 hover:text-blue-700 font-medium">
                View Full Analysis →
              </button>
            </div>
          </div>
        </div>

        <div className="grid md:grid-cols-2 gap-6">
          {/* Mood Trends */}
          <div className="card">
            <h3 className="text-lg font-semibold mb-4">Mood Trends (Last 7 Days)</h3>
            <div className="bg-gray-100 rounded-lg p-8 text-center">
              <div className="text-4xl mb-2">📈</div>
              <p className="text-gray-600">Mood chart visualization would go here</p>
              <p className="text-sm text-gray-500 mt-2">Average mood: 6.8/10</p>
            </div>
            <button className="mt-4 text-primary-500 hover:text-primary-600 font-medium">
              View Detailed Charts →
            </button>
          </div>

          {/* Recent Journal Entries */}
          <div className="card">
            <h3 className="text-lg font-semibold mb-4">Recent Journal Entries</h3>
            <div className="space-y-3">
              <div className="bg-gray-50 rounded-lg p-3">
                <p className="text-sm text-gray-600 mb-1">2 days ago</p>
                <p className="font-medium">"Today was better than expected..."</p>
              </div>
              <div className="bg-gray-50 rounded-lg p-3">
                <p className="text-sm text-gray-600 mb-1">3 days ago</p>
                <p className="font-medium">"I'm grateful for the support..."</p>
              </div>
              <div className="bg-gray-50 rounded-lg p-3">
                <p className="text-sm text-gray-600 mb-1">5 days ago</p>
                <p className="font-medium">"Feeling anxious about work..."</p>
              </div>
            </div>
            <Link href="/journal" className="mt-4 inline-block text-primary-500 hover:text-primary-600 font-medium">
              View All Entries →
            </Link>
          </div>
        </div>
      </main>
    </div>
  )
}