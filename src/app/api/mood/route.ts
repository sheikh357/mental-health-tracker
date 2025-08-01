import { NextRequest, NextResponse } from 'next/server'
import type { ApiResponse, MoodCheckInForm, MoodEntry } from '@/types'

// Mock database - replace with actual MongoDB connection
const mockMoodEntries: MoodEntry[] = []

export async function GET(request: NextRequest) {
  try {
    const { searchParams } = new URL(request.url)
    const userId = searchParams.get('user_id')
    const limit = parseInt(searchParams.get('limit') || '10')
    const offset = parseInt(searchParams.get('offset') || '0')

    if (!userId) {
      return NextResponse.json<ApiResponse<null>>({
        success: false,
        error: 'User ID is required'
      }, { status: 400 })
    }

    // Filter mood entries by user and apply pagination
    const userMoodEntries = mockMoodEntries
      .filter(entry => entry.user_id === userId)
      .sort((a, b) => new Date(b.created_at).getTime() - new Date(a.created_at).getTime())
      .slice(offset, offset + limit)

    return NextResponse.json<ApiResponse<MoodEntry[]>>({
      success: true,
      data: userMoodEntries,
      message: `Retrieved ${userMoodEntries.length} mood entries`
    })
  } catch (error) {
    console.error('Error fetching mood entries:', error)
    return NextResponse.json<ApiResponse<null>>({
      success: false,
      error: 'Internal server error'
    }, { status: 500 })
  }
}

export async function POST(request: NextRequest) {
  try {
    const body: MoodCheckInForm & { user_id: string } = await request.json()
    
    if (!body.user_id || !body.mood_value || !body.mood_label) {
      return NextResponse.json<ApiResponse<null>>({
        success: false,
        error: 'User ID, mood value, and mood label are required'
      }, { status: 400 })
    }

    if (body.mood_value < 1 || body.mood_value > 10) {
      return NextResponse.json<ApiResponse<null>>({
        success: false,
        error: 'Mood value must be between 1 and 10'
      }, { status: 400 })
    }

    const newMoodEntry: MoodEntry = {
      id: `mood_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`,
      user_id: body.user_id,
      mood_value: body.mood_value,
      mood_label: body.mood_label,
      notes: body.notes,
      created_at: new Date(),
      updated_at: new Date()
    }

    // Add to mock database
    mockMoodEntries.push(newMoodEntry)

    return NextResponse.json<ApiResponse<MoodEntry>>({
      success: true,
      data: newMoodEntry,
      message: 'Mood entry created successfully'
    }, { status: 201 })
  } catch (error) {
    console.error('Error creating mood entry:', error)
    return NextResponse.json<ApiResponse<null>>({
      success: false,
      error: 'Internal server error'
    }, { status: 500 })
  }
}