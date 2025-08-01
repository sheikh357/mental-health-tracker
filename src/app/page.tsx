import Link from 'next/link'

export default function HomePage() {
  return (
    <main className="min-h-screen flex flex-col items-center justify-center p-4">
      <div className="max-w-4xl mx-auto text-center">
        {/* Hero Section */}
        <div className="mb-12">
          <h1 className="text-4xl md:text-6xl font-bold text-gray-900 mb-6">
            Mental Health
            <span className="block text-primary-500">Tracker</span>
          </h1>
          <p className="text-lg md:text-xl text-gray-600 mb-8 max-w-2xl mx-auto">
            Your AI-powered companion for mental health tracking, personalized insights, 
            and guided wellness journey.
          </p>
          
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <Link 
              href="/auth/login" 
              className="btn-primary text-lg px-8 py-3 inline-block"
            >
              Get Started
            </Link>
            <Link 
              href="/resources" 
              className="btn-secondary text-lg px-8 py-3 inline-block"
            >
              Learn More
            </Link>
          </div>
        </div>

        {/* Features Grid */}
        <div className="grid md:grid-cols-3 gap-8 mb-12">
          <div className="card text-center">
            <div className="text-4xl mb-4">📊</div>
            <h3 className="text-xl font-semibold mb-2">Mood Tracking</h3>
            <p className="text-gray-600">
              Simple daily mood check-ins with detailed analytics and trend visualization.
            </p>
          </div>
          
          <div className="card text-center">
            <div className="text-4xl mb-4">📝</div>
            <h3 className="text-xl font-semibold mb-2">AI Journal</h3>
            <p className="text-gray-600">
              Intelligent journaling with AI-powered insights and personalized recommendations.
            </p>
          </div>
          
          <div className="card text-center">
            <div className="text-4xl mb-4">🧠</div>
            <h3 className="text-xl font-semibold mb-2">Mental Wellness</h3>
            <p className="text-gray-600">
              Curated resources, guided exercises, and professional support when you need it.
            </p>
          </div>
        </div>

        {/* Call to Action */}
        <div className="bg-white rounded-lg shadow-sm border border-gray-200 p-8">
          <h2 className="text-2xl font-semibold mb-4">Ready to start your wellness journey?</h2>
          <p className="text-gray-600 mb-6">
            Join thousands of users who have improved their mental health with our AI-powered tracking and insights.
          </p>
          <Link 
            href="/auth/login" 
            className="btn-primary text-lg px-8 py-3 inline-block"
          >
            Sign Up Free
          </Link>
        </div>
      </div>
    </main>
  )
}