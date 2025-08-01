# Mental Health Tracker - Wireframes & UI Design

## 1. Design System Overview

### 1.1 Color Palette
- **Primary**: Calming blue (#4A90E2) - Trust, stability, mental clarity
- **Secondary**: Soft green (#7ED321) - Growth, healing, wellness
- **Accent**: Warm purple (#9013FE) - Creativity, mindfulness
- **Neutral**: Soft grays (#F5F5F7, #8E8E93) - Clean, minimal
- **Background**: Off-white (#FAFAFA) - Gentle, non-straining
- **Text**: Dark gray (#1D1D1F) - Readable, professional

### 1.2 Typography
- **Primary Font**: Inter - Clean, modern, highly readable
- **Headings**: Inter Bold (24px, 20px, 18px, 16px)
- **Body Text**: Inter Regular (16px, 14px)
- **Captions**: Inter Medium (12px)

### 1.3 Spacing & Layout
- **Grid**: 12-column responsive grid
- **Margins**: 16px (mobile), 24px (tablet), 32px (desktop)
- **Component Spacing**: 8px, 16px, 24px, 32px, 48px
- **Border Radius**: 8px (cards), 16px (buttons), 24px (modals)

## 2. Page Wireframes

### 2.1 Authentication Pages

#### Login Page
```
┌─────────────────────────────────────┐
│  [Logo] Mental Health Tracker       │
│                                     │
│  ┌─────────────────────────────────┐ │
│  │                                 │ │
│  │    Welcome Back to Your         │ │
│  │    Mental Health Journey        │ │
│  │                                 │ │
│  │  ┌─────────────────────────────┐ │ │
│  │  │ email@example.com           │ │ │
│  │  └─────────────────────────────┘ │ │
│  │                                 │ │
│  │  [Send Magic Link Button]       │ │
│  │                                 │ │
│  │  "We'll send a secure login     │ │
│  │   link to your email"          │ │
│  │                                 │ │
│  └─────────────────────────────────┘ │
│                                     │
│  [Privacy Policy] [Terms of Service] │
└─────────────────────────────────────┘
```

### 2.2 Dashboard (Main Page)

#### Desktop Dashboard
```
┌─────────────────────────────────────────────────────────────┐
│ [Logo] Mental Health Tracker    [Profile] [Settings] [Logout] │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ Good morning, Alex! How are you feeling today?             │
│                                                             │
│ ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐ │
│ │    😊   │ │    😐   │ │    😔   │ │    😡   │ │    😴   │ │
│ │ Great   │ │ Okay    │ │  Sad    │ │ Angry   │ │ Tired   │ │
│ │   (9)   │ │   (5)   │ │   (3)   │ │   (2)   │ │   (4)   │ │
│ └─────────┘ └─────────┘ └─────────┘ └─────────┘ └─────────┘ │
│                                                             │
│ ┌─────────────────────┐ ┌─────────────────────────────────┐ │
│ │   Quick Actions     │ │        Today's Insights         │ │
│ │                     │ │                                 │ │
│ │ [📝 New Journal]    │ │ "You've been consistently       │ │
│ │ [📊 View Analytics] │ │  logging positive moods this    │ │
│ │ [🎯 Set Goal]       │ │  week. Consider reflecting on   │ │
│ │ [📚 Resources]      │ │  what's contributing to this    │ │
│ │                     │ │  positive trend."               │ │
│ └─────────────────────┘ │                                 │ │
│                         │ [View Full Analysis]            │ │
│ ┌─────────────────────┐ └─────────────────────────────────┘ │
│ │   Mood Trends       │                                   │ │
│ │                     │ ┌─────────────────────────────────┐ │
│ │     📈 Chart        │ │      Recent Journal Entries     │ │
│ │   (Last 7 days)     │ │                                 │ │
│ │                     │ │ "Today was better than..."      │ │
│ │ [View Full Chart]   │ │ "I'm grateful for..."           │ │
│ └─────────────────────┘ │ "Feeling anxious about..."      │ │
│                         │                                 │ │
│                         │ [Write New Entry]               │ │
│                         └─────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

#### Mobile Dashboard
```
┌─────────────────┐
│ [☰] MHT [🔔][👤] │
├─────────────────┤
│                 │
│ Good morning!   │
│ How are you     │
│ feeling today?  │
│                 │
│ ┌─────┐ ┌─────┐ │
│ │ 😊  │ │ 😐  │ │
│ │Great│ │Okay │ │
│ └─────┘ └─────┘ │
│ ┌─────┐ ┌─────┐ │
│ │ 😔  │ │ 😡  │ │
│ │ Sad │ │Angry│ │
│ └─────┘ └─────┘ │
│                 │
│ ┌─────────────┐ │
│ │Today's      │ │
│ │Insights     │ │
│ │             │ │
│ │"Your mood   │ │
│ │ has been... │ │
│ │             │ │
│ │[View More]  │ │
│ └─────────────┘ │
│                 │
│ [📝 Journal]    │
│ [📊 Analytics]  │
│ [📚 Resources]  │
└─────────────────┘
```

### 2.3 Journal Entry Page

#### Desktop Journal
```
┌─────────────────────────────────────────────────────────────┐
│ ← Back to Dashboard                        [Save] [Publish] │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ New Journal Entry - August 1, 2025                         │
│                                                             │
│ How are you feeling? (Optional)                            │
│ ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐             │
│ │    😊   │ │    😐   │ │    😔   │ │    😡   │ [Selected]  │
│ │ Great   │ │ Okay    │ │  Sad    │ │ Angry   │             │
│ └─────────┘ └─────────┘ └─────────┘ └─────────┘             │
│                                                             │
│ ┌─────────────────────────────────────────────────────────┐ │
│ │ What's on your mind today?                              │ │
│ │                                                         │ │
│ │ [Rich text editor with formatting options]              │ │
│ │                                                         │ │
│ │ Today I woke up feeling pretty good. The weather is    │ │
│ │ nice and I have some exciting plans for the weekend... │ │
│ │                                                         │ │
│ │                                                         │ │
│ │                                                         │ │
│ └─────────────────────────────────────────────────────────┘ │
│                                                             │
│ ┌─────────────────────┐ ┌─────────────────────────────────┐ │
│ │   Writing Prompts   │ │        AI Suggestions           │ │
│ │                     │ │                                 │ │
│ │ • What made you     │ │ Based on your recent entries:   │ │
│ │   smile today?      │ │                                 │ │
│ │ • What challenged   │ │ • Consider exploring your       │ │
│ │   you?              │ │   feelings about work stress    │ │
│ │ • What are you      │ │ • You mentioned family often -  │ │
│ │   grateful for?     │ │   how are those relationships?  │ │
│ │                     │ │                                 │ │
│ └─────────────────────┘ └─────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

### 2.4 Analytics Page

#### Analytics Dashboard
```
┌─────────────────────────────────────────────────────────────┐
│ Analytics & Insights                      [Export Data]     │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ ┌─────────────────────┐ ┌─────────────────────────────────┐ │
│ │   Mood Overview     │ │        Weekly Summary           │ │
│ │                     │ │                                 │ │
│ │ Average Mood: 6.8   │ │ This Week: 📈 Trending up       │ │
│ │ Best Day: Monday    │ │ Best Day: Thursday (8.2)        │ │
│ │ Most Common: Happy  │ │ Challenging Day: Tuesday (4.1)  │ │
│ │                     │ │                                 │ │
│ │ [View Details]      │ │ "You've shown great resilience  │ │
│ └─────────────────────┘ │  this week despite Tuesday's    │ │
│                         │  challenges."                   │ │
│ ┌─────────────────────┐ └─────────────────────────────────┘ │
│ │   Mood Trends       │                                   │ │
│ │                     │ ┌─────────────────────────────────┐ │
│ │ [Line Chart showing │ │      Journal Insights           │ │
│ │  mood over time     │ │                                 │ │
│ │  with trend line]   │ │ Most Common Words:              │ │
│ │                     │ │ ┌─────┐ ┌─────┐ ┌─────┐         │ │
│ │ Time Range:         │ │ │work │ │happy│ │tired│         │ │
│ │ [7D][30D][90D][1Y]  │ │ └─────┘ └─────┘ └─────┘         │ │
│ └─────────────────────┘ │                                 │ │
│                         │ Sentiment Trend: 📈 Positive    │ │
│ ┌─────────────────────┐ │ Writing Frequency: 5.2/week     │ │
│ │   AI Insights       │ │                                 │ │
│ │                     │ │ [View Word Cloud]               │ │
│ │ "Pattern detected:  │ └─────────────────────────────────┘ │
│  Your mood tends to   │                                   │ │
│  improve on days when │                                   │ │
│  you write longer     │                                   │ │
│  journal entries."    │                                   │ │
│ │                     │                                   │ │
│ │ [View All Insights] │                                   │ │
│ └─────────────────────┘                                   │ │
└─────────────────────────────────────────────────────────────┘
```

### 2.5 Resources Page

#### Mental Health Resources
```
┌─────────────────────────────────────────────────────────────┐
│ Mental Health Resources                    [Search...]      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ ┌─────────────────────────────────────────────────────────┐ │
│ │                🚨 Crisis Support                        │ │
│ │                                                         │ │
│ │ If you're in crisis or need immediate help:             │ │
│ │ • National Suicide Prevention Lifeline: 988             │ │
│ │ • Crisis Text Line: Text HOME to 741741               │ │
│ │ • Emergency Services: 911                              │ │
│ │                                                         │ │
│ │ [Get Help Now]                                         │ │
│ └─────────────────────────────────────────────────────────┘ │
│                                                             │
│ Resource Categories:                                        │
│ [All] [Anxiety] [Depression] [Stress] [Sleep] [Therapy]     │
│                                                             │
│ ┌─────────────────────┐ ┌─────────────────────────────────┐ │
│ │   📚 Articles       │ │        🎥 Videos               │ │
│ │                     │ │                                 │ │
│ │ • "Understanding    │ │ • "5-Minute Meditation"        │ │
│ │   Anxiety Triggers" │ │ • "Breathing Exercises"        │ │
│ │ • "Sleep Hygiene    │ │ • "Progressive Muscle          │ │
│ │   Tips"             │ │   Relaxation"                  │ │
│ │ • "Mindfulness      │ │ • "Dealing with Panic          │ │
│ │   Techniques"       │ │   Attacks"                     │ │
│ │                     │ │                                 │ │
│ │ [View All Articles] │ │ [View All Videos]              │ │
│ └─────────────────────┘ └─────────────────────────────────┘ │
│                                                             │
│ ┌─────────────────────┐ ┌─────────────────────────────────┐ │
│ │   🧠 Exercises      │ │      👨‍⚕️ Find Help             │ │
│ │                     │ │                                 │ │
│ │ • Guided Breathing  │ │ • Psychology Today Directory    │ │
│ │ • Thought Records   │ │ • BetterHelp (Online Therapy)   │ │
│ │ • Gratitude Journal │ │ • Local Mental Health Centers   │ │
│ │ • Progressive       │ │ • Insurance Provider Search     │ │
│ │   Relaxation        │ │                                 │ │
│ │                     │ │ [Find Therapists Near Me]      │ │
│ │ [Try an Exercise]   │ └─────────────────────────────────┘ │
│ └─────────────────────┘                                   │ │
└─────────────────────────────────────────────────────────────┘
```

### 2.6 Profile/Settings Page

#### User Profile & Settings
```
┌─────────────────────────────────────────────────────────────┐
│ Profile & Settings                              [Save]      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ ┌─────────────────────┐ ┌─────────────────────────────────┐ │
│ │   Profile Info      │ │        Preferences              │ │
│ │                     │ │                                 │ │
│ │ Name: Alex Johnson  │ │ Notifications:                  │ │
│ │ Email: alex@...     │ │ ☑ Daily mood reminders         │ │
│ │ Joined: Jan 2025    │ │ ☑ Weekly insights               │ │
│ │                     │ │ ☐ Research participation        │ │
│ │ [Change Email]      │ │                                 │ │
│ │                     │ │ Time Zone: EST                  │ │
│ └─────────────────────┘ │ Reminder Time: 8:00 PM          │ │
│                         │                                 │ │
│ ┌─────────────────────┐ │ Theme: ◉ Light ○ Dark ○ Auto   │ │
│ │   Privacy & Data    │ └─────────────────────────────────┘ │
│ │                     │                                   │ │
│ │ Data Export:        │ ┌─────────────────────────────────┐ │
│ │ [Download My Data]  │ │        AI Settings              │ │
│ │                     │ │                                 │ │
│ │ Account Deletion:   │ │ AI Insights: ☑ Enabled         │ │
│ │ [Delete Account]    │ │ Insight Frequency: Weekly       │ │
│ │                     │ │ Privacy Level: Standard         │ │
│ │ Privacy Policy      │ │                                 │ │
│ │ Terms of Service    │ │ ☑ Mood pattern analysis        │ │
│ └─────────────────────┘ │ ☑ Journal sentiment analysis    │ │
│                         │ ☐ Predictive insights           │ │
│                         └─────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

## 3. Mobile-Specific Considerations

### 3.1 Navigation
- **Bottom Tab Bar**: Dashboard, Journal, Analytics, Resources, Profile
- **Hamburger Menu**: Secondary navigation and settings
- **Swipe Gestures**: Quick mood logging, entry navigation

### 3.2 Mobile Optimizations
- **Touch Targets**: Minimum 44px for all interactive elements
- **Thumb-Friendly**: Primary actions within easy thumb reach
- **Progressive Enhancement**: Core features work offline
- **Performance**: Lazy loading, image optimization

### 3.3 Accessibility Features
- **Screen Reader Support**: Semantic HTML, ARIA labels
- **High Contrast Mode**: Enhanced visual accessibility
- **Large Text Support**: Scalable typography
- **Voice Input**: Alternative input methods

## 4. Interactive Elements

### 4.1 Mood Selection
- **Visual**: Emoji-based mood selection with color coding
- **Accessibility**: Text labels and keyboard navigation
- **Quick Entry**: One-tap mood logging from dashboard

### 4.2 Charts & Visualizations
- **Interactive**: Hover states, drill-down capabilities
- **Responsive**: Adapt to different screen sizes
- **Colorblind Friendly**: Pattern and shape variations

### 4.3 Forms & Input
- **Validation**: Real-time feedback with helpful messages
- **Auto-save**: Prevent data loss during entry
- **Rich Text**: Formatting options for journal entries

## 5. Design Guidelines

### 5.1 Visual Hierarchy
- **Primary Actions**: Bold colors, prominent placement
- **Secondary Actions**: Subtle styling, logical grouping
- **Information**: Clear typography, appropriate contrast

### 5.2 Emotional Design
- **Calming Colors**: Avoid harsh or alarming color choices
- **Positive Reinforcement**: Encouraging messages and progress indicators
- **Safe Space**: Non-judgmental language and inclusive design