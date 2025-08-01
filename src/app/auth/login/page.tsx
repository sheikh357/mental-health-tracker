'use client'

import { useState } from 'react'
import Link from 'next/link'

export default function LoginPage() {
  const [email, setEmail] = useState('')
  const [isLoading, setIsLoading] = useState(false)
  const [isSubmitted, setIsSubmitted] = useState(false)

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setIsLoading(true)
    
    // Simulate API call for now
    await new Promise(resolve => setTimeout(resolve, 1500))
    
    setIsLoading(false)
    setIsSubmitted(true)
  }

  if (isSubmitted) {
    return (
      <main className="min-h-screen flex items-center justify-center p-4">
        <div className="max-w-md w-full">
          <div className="card text-center">
            <div className="text-4xl mb-4">📧</div>
            <h1 className="text-2xl font-bold mb-4">Check Your Email</h1>
            <p className="text-gray-600 mb-6">
              We've sent a secure login link to <strong>{email}</strong>
            </p>
            <p className="text-sm text-gray-500 mb-6">
              Click the link in your email to complete your login. The link will expire in 15 minutes.
            </p>
            <button 
              onClick={() => setIsSubmitted(false)}
              className="text-primary-500 hover:text-primary-600 font-medium"
            >
              Try a different email
            </button>
          </div>
        </div>
      </main>
    )
  }

  return (
    <main className="min-h-screen flex items-center justify-center p-4">
      <div className="max-w-md w-full">
        <div className="text-center mb-8">
          <Link href="/" className="text-2xl font-bold text-primary-500">
            Mental Health Tracker
          </Link>
        </div>
        
        <div className="card">
          <h1 className="text-2xl font-bold text-center mb-2">Welcome Back</h1>
          <p className="text-gray-600 text-center mb-8">
            Continue your mental health journey
          </p>
          
          <form onSubmit={handleSubmit} className="space-y-6">
            <div>
              <label htmlFor="email" className="block text-sm font-medium text-gray-700 mb-2">
                Email Address
              </label>
              <input
                type="email"
                id="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                className="input-field"
                placeholder="your.email@example.com"
                required
                disabled={isLoading}
              />
            </div>
            
            <button
              type="submit"
              disabled={isLoading || !email}
              className="w-full btn-primary py-3 disabled:opacity-50 disabled:cursor-not-allowed"
            >
              {isLoading ? (
                <span className="flex items-center justify-center">
                  <svg className="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                    <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                    <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                  </svg>
                  Sending Magic Link...
                </span>
              ) : (
                'Send Magic Link'
              )}
            </button>
          </form>
          
          <div className="mt-6 text-center">
            <p className="text-sm text-gray-500">
              We'll send a secure login link to your email.
              <br />
              No passwords required.
            </p>
          </div>
          
          <div className="mt-8 pt-6 border-t border-gray-200">
            <p className="text-center text-sm text-gray-500">
              Don't have an account? 
              <Link href="/auth/signup" className="text-primary-500 hover:text-primary-600 font-medium ml-1">
                Sign up
              </Link>
            </p>
          </div>
        </div>
        
        <div className="mt-6 text-center text-xs text-gray-500">
          <Link href="/privacy" className="hover:text-gray-700">Privacy Policy</Link>
          <span className="mx-2">•</span>
          <Link href="/terms" className="hover:text-gray-700">Terms of Service</Link>
        </div>
      </div>
    </main>
  )
}