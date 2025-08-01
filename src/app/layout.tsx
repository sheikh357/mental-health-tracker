import './globals.css'
import type { Metadata } from 'next'

export const metadata: Metadata = {
  title: 'Mental Health Tracker',
  description: 'AI-powered mental health tracker web app for personal wellness and insights',
  keywords: ['mental health', 'AI', 'wellness', 'mood tracking', 'journal'],
  authors: [{ name: 'Mental Health Tracker Team' }],
  viewport: 'width=device-width, initial-scale=1',
  themeColor: '#4A90E2',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <head>
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="anonymous" />
        <link 
          href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" 
          rel="stylesheet" 
        />
      </head>
      <body className="font-sans">
        <div className="min-h-screen bg-gradient-to-br from-gray-50 to-gray-100">
          {children}
        </div>
      </body>
    </html>
  )
}