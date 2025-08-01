# Mental Health Tracker

An AI-powered web application for tracking mental health, providing personalized insights, and accessing mental health resources.

## 🌟 Features

- **Daily Mood Tracking**: Simple, intuitive mood logging with trend analysis
- **AI-Powered Journal**: Intelligent journaling with sentiment analysis and personalized insights
- **Analytics Dashboard**: Visual representation of mental health patterns and progress
- **Mental Health Resources**: Curated collection of articles, exercises, and crisis support
- **Privacy-First**: All data encrypted and under user control
- **Responsive Design**: Mobile-first, accessible interface

## 🏗️ Tech Stack

- **Frontend**: Next.js 14+ with React 18+ and TypeScript
- **Styling**: Tailwind CSS with custom design system
- **Authentication**: Supabase Auth (Magic Link email login)
- **Database**: MongoDB with Mongoose ODM
- **AI Integration**: OpenAI GPT-4 via n8n workflows
- **Deployment**: Vercel with MongoDB Atlas

## 🚀 Quick Start

### Prerequisites

- Node.js 18+ and npm
- MongoDB instance (local or MongoDB Atlas)
- Supabase account for authentication
- OpenAI API key for AI features

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/sheikh357/mental-health-tracker.git
   cd mental-health-tracker
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Set up environment variables**
   ```bash
   cp .env.example .env.local
   ```
   
   Fill in your environment variables in `.env.local`:
   - MongoDB connection string
   - Supabase configuration
   - OpenAI API key
   - JWT secret

4. **Run the development server**
   ```bash
   npm run dev
   ```

5. **Open your browser**
   Navigate to [http://localhost:3000](http://localhost:3000)

## 📁 Project Structure

```
mental-health-tracker/
├── docs/                          # Project documentation
│   ├── PRD.md                     # Product Requirements Document
│   ├── wireframes.md              # UI/UX wireframes and design
│   └── project-plan.md            # Detailed implementation plan
├── src/
│   ├── app/                       # Next.js 13+ app directory
│   │   ├── api/                   # API routes
│   │   │   ├── auth/              # Authentication endpoints
│   │   │   ├── mood/              # Mood tracking endpoints
│   │   │   ├── journal/           # Journal entry endpoints
│   │   │   ├── analytics/         # Analytics data endpoints
│   │   │   └── insights/          # AI insights endpoints
│   │   ├── auth/                  # Authentication pages
│   │   ├── dashboard/             # Main dashboard
│   │   ├── journal/               # Journal pages
│   │   ├── analytics/             # Analytics and charts
│   │   ├── resources/             # Mental health resources
│   │   ├── profile/               # User profile and settings
│   │   ├── globals.css            # Global styles
│   │   ├── layout.tsx             # Root layout component
│   │   └── page.tsx               # Home page
│   ├── components/                # Reusable React components
│   ├── lib/                       # Utility functions and helpers
│   ├── types/                     # TypeScript type definitions
│   └── config/                    # Configuration files
├── database/
│   ├── models/                    # MongoDB/Mongoose models
│   │   ├── User.ts               # User data model
│   │   ├── MoodEntry.ts          # Mood tracking model
│   │   └── JournalEntry.ts       # Journal entry model
│   └── migrations/                # Database migrations
├── n8n-workflows/                 # AI workflow configurations
├── public/                        # Static assets
├── .env.example                   # Environment variables template
├── .gitignore                     # Git ignore rules
├── next.config.js                 # Next.js configuration
├── tailwind.config.ts             # Tailwind CSS configuration
├── tsconfig.json                  # TypeScript configuration
└── package.json                   # Project dependencies
```

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `MONGODB_URI` | MongoDB connection string | Yes |
| `NEXT_PUBLIC_SUPABASE_URL` | Supabase project URL | Yes |
| `NEXT_PUBLIC_SUPABASE_ANON_KEY` | Supabase anonymous key | Yes |
| `SUPABASE_SERVICE_ROLE_KEY` | Supabase service role key | Yes |
| `OPENAI_API_KEY` | OpenAI API key for AI features | Yes |
| `JWT_SECRET` | Secret key for JWT tokens | Yes |
| `N8N_WEBHOOK_URL` | n8n webhook URL for AI workflows | Optional |
| `N8N_API_KEY` | n8n API key | Optional |

### Database Schema

The application uses MongoDB with the following main collections:

- **Users**: User accounts and preferences
- **MoodEntries**: Daily mood check-ins and tracking
- **JournalEntries**: Journal entries with AI analysis
- **UserAnalytics**: Generated insights and analytics data

## 🤖 AI Features

### Mood Pattern Analysis
- Identifies trends and patterns in mood data
- Detects correlations between activities and mood
- Provides personalized recommendations

### Journal Sentiment Analysis
- Real-time sentiment analysis of journal entries
- Emotion detection and classification
- Theme and keyword extraction

### Personalized Insights
- Weekly AI-generated insights and recommendations
- Progress tracking and goal setting
- Crisis detection and support recommendations

## 📊 API Endpoints

### Authentication
- `POST /api/auth/login` - Send magic link
- `GET /api/auth/callback` - Handle magic link callback
- `POST /api/auth/logout` - User logout
- `GET /api/auth/user` - Get current user

### Mood Tracking
- `GET /api/mood` - Get user's mood entries
- `POST /api/mood` - Create new mood entry
- `PUT /api/mood/:id` - Update mood entry
- `DELETE /api/mood/:id` - Delete mood entry

### Journal
- `GET /api/journal` - Get user's journal entries
- `POST /api/journal` - Create new journal entry
- `PUT /api/journal/:id` - Update journal entry
- `DELETE /api/journal/:id` - Delete journal entry
- `POST /api/journal/:id/analyze` - Request AI analysis

### Analytics
- `GET /api/analytics` - Get user analytics data
- `GET /api/insights` - Get personalized insights

## 🎨 Design System

### Colors
- **Primary**: Calming blue (#4A90E2) - Trust and stability
- **Secondary**: Soft green (#7ED321) - Growth and healing
- **Accent**: Warm purple (#9013FE) - Creativity and mindfulness
- **Neutral**: Soft grays - Clean, minimal interface

### Typography
- **Font**: Inter - Clean, modern, highly readable
- **Hierarchy**: Clear heading levels and readable body text
- **Accessibility**: WCAG 2.1 AA compliant contrast ratios

## 🔒 Privacy & Security

- **Data Encryption**: All sensitive data encrypted at rest and in transit
- **Privacy by Design**: Minimal data collection and user control
- **GDPR Compliant**: Data export and deletion capabilities
- **Secure Authentication**: Passwordless magic link login
- **User Control**: Granular privacy settings and data management

## 🧪 Testing

```bash
# Run type checking
npm run type-check

# Run linting
npm run lint

# Build the application
npm run build
```

## 🚀 Deployment

### Vercel Deployment

1. **Connect your repository to Vercel**
2. **Set environment variables in Vercel dashboard**
3. **Deploy automatically on push to main branch**

### Environment Setup
- **Database**: MongoDB Atlas for production
- **Authentication**: Supabase for user management
- **AI Processing**: n8n Cloud for workflow automation
- **Monitoring**: Built-in Vercel analytics

## 📈 Roadmap

### Phase 1 (Current)
- ✅ Basic mood tracking
- ✅ Journal entries
- ✅ User authentication
- ✅ Dashboard interface

### Phase 2
- [ ] AI sentiment analysis
- [ ] Advanced analytics charts
- [ ] Personalized insights
- [ ] Mobile app (React Native)

### Phase 3
- [ ] Social features (anonymous community)
- [ ] Wearable device integration
- [ ] Professional therapist tools
- [ ] Advanced AI predictions

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

- **Crisis Support**: If you're in crisis, please contact:
  - National Suicide Prevention Lifeline: 988
  - Crisis Text Line: Text HOME to 741741
  - Emergency Services: 911

- **Technical Support**: Create an issue on GitHub or contact the development team.

## 🙏 Acknowledgments

- Mental health professionals who provided guidance on best practices
- Open source community for the amazing tools and libraries
- All users who trust us with their mental health journey

---

**Disclaimer**: This application is designed to support mental health tracking and awareness. It is not a substitute for professional mental health care. If you're experiencing a mental health crisis, please seek immediate professional help.