import { NextRequest, NextResponse } from 'next/server'
import type { ApiResponse, JournalEntryForm, JournalEntry } from '@/types'

// Mock database - replace with actual MongoDB connection
const mockJournalEntries: JournalEntry[] = []

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

    // Filter journal entries by user and apply pagination
    const userJournalEntries = mockJournalEntries
      .filter(entry => entry.user_id === userId)
      .sort((a, b) => new Date(b.created_at).getTime() - new Date(a.created_at).getTime())
      .slice(offset, offset + limit)

    return NextResponse.json<ApiResponse<JournalEntry[]>>({
      success: true,
      data: userJournalEntries,
      message: `Retrieved ${userJournalEntries.length} journal entries`
    })
  } catch (error) {
    console.error('Error fetching journal entries:', error)
    return NextResponse.json<ApiResponse<null>>({
      success: false,
      error: 'Internal server error'
    }, { status: 500 })
  }
}

export async function POST(request: NextRequest) {
  try {
    const body: JournalEntryForm & { user_id: string } = await request.json()
    
    if (!body.user_id || !body.content) {
      return NextResponse.json<ApiResponse<null>>({
        success: false,
        error: 'User ID and content are required'
      }, { status: 400 })
    }

    if (body.content.trim().length < 10) {
      return NextResponse.json<ApiResponse<null>>({
        success: false,
        error: 'Journal entry must be at least 10 characters long'
      }, { status: 400 })
    }

    const newJournalEntry: JournalEntry = {
      id: `journal_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`,
      user_id: body.user_id,
      title: body.title,
      content: body.content,
      mood_id: body.mood_id,
      is_private: body.is_private ?? true,
      created_at: new Date(),
      updated_at: new Date()
    }

    // Add to mock database
    mockJournalEntries.push(newJournalEntry)

    // TODO: Trigger AI analysis workflow here
    // This would normally call the n8n workflow for sentiment analysis
    
    return NextResponse.json<ApiResponse<JournalEntry>>({
      success: true,
      data: newJournalEntry,
      message: 'Journal entry created successfully'
    }, { status: 201 })
  } catch (error) {
    console.error('Error creating journal entry:', error)
    return NextResponse.json<ApiResponse<null>>({
      success: false,
      error: 'Internal server error'
    }, { status: 500 })
  }
}