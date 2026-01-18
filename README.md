# BuildFlow - Data Science Learning Platform

A full-stack platform for managing data science internships with Discord bot integration, GitHub Actions automation, and AI-powered code review.

## Project Structure

```
ds-buildflow/
├── frontend/          # Next.js frontend application
│   ├── src/          # Source code
│   ├── public/       # Static assets
│   └── package.json  # Frontend dependencies
├── backend/          # FastAPI backend application
│   ├── app/          # Main application code
│   ├── bot/          # Discord bot code
│   └── requirements.txt  # Python dependencies
├── supabase/         # Database migrations
│   └── migrations/   # SQL migration files
└── docs/             # Documentation
```

## Prerequisites

- **Node.js** 18+ and npm
- **Python** 3.11+
- **PostgreSQL** (via Supabase)
- **Discord Bot Token** (for Discord integration)
- **GitHub Token** (for GitHub Actions integration)

## Quick Start

### 1. Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Frontend will be available at: http://localhost:3000

### 2. Backend Setup

```bash
cd backend

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env  # Edit .env with your values

# Run the backend
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Backend will be available at: http://localhost:8000
API Documentation: http://localhost:8000/docs

### 3. Database Setup

The project uses Supabase for the database. Migrations are in `supabase/migrations/`.

Run migrations through Supabase dashboard or CLI.

## Environment Variables

### Backend (.env)

Create `backend/.env` with:

```env
# Database (Supabase)
DATABASE_URL=your-database-url
SUPABASE_URL=your-supabase-url
SUPABASE_KEY=your-supabase-key
SUPABASE_SERVICE_KEY=your-service-key

# GitHub
GITHUB_TOKEN=your-github-token
GITHUB_WEBHOOK_SECRET=your-webhook-secret

# Discord
DISCORD_TOKEN=your-discord-bot-token
DISCORD_GUILD_ID=your-discord-server-id

# Anthropic (for AI review)
ANTHROPIC_API_KEY=your-anthropic-api-key

# Backend
BACKEND_URL=http://localhost:8000
WEBHOOK_SECRET=your-webhook-secret

# CORS
CORS_ORIGINS=http://localhost:3000
```

### Frontend (.env.local)

Create `frontend/.env.local` with:

```env
NEXT_PUBLIC_SUPABASE_URL=your-supabase-url
NEXT_PUBLIC_SUPABASE_ANON_KEY=your-supabase-anon-key
NEXT_PUBLIC_BACKEND_URL=http://localhost:8000
```

## Running Both Services

### Option 1: Separate Terminals

**Terminal 1 - Backend:**
```bash
cd backend
source venv/bin/activate
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm run dev
```

### Option 2: Background Processes

```bash
# Backend
cd backend && source venv/bin/activate && uvicorn app.main:app --reload --host 0.0.0.0 --port 8000 &

# Frontend
cd frontend && npm run dev &
```

## Discord Bot

See [DISCORD_BOT_SETUP.md](./DISCORD_BOT_SETUP.md) for detailed Discord bot setup instructions.

Quick start:
```bash
cd backend
source venv/bin/activate
python3 -m bot.main
```

## Development

### Frontend Development
- Framework: Next.js 15 with App Router
- Styling: Tailwind CSS
- UI Components: Radix UI
- State Management: React Server Components

### Backend Development
- Framework: FastAPI
- Database: PostgreSQL (via Supabase)
- ORM: asyncpg (async PostgreSQL driver)
- Validation: Pydantic

## Documentation

- [Product Requirements Document](./docs/01-PRD.md)
- [Technical Architecture](./docs/02-TECHNICAL-ARCHITECTURE.md)
- [Database Schema](./docs/03-DATABASE-SCHEMA.md)
- [API Specification](./docs/04-API-SPECIFICATION.md)
- [Discord Bot Specification](./docs/05-DISCORD-BOT-SPEC.md)
- [GitHub Actions Setup](./docs/06-GITHUB-ACTIONS.md)
- [Discord Bot Setup Guide](./DISCORD_BOT_SETUP.md)

## Testing

### Backend Tests
```bash
cd backend
source venv/bin/activate
pytest
```

### Frontend Tests
```bash
cd frontend
npm test
```

## Deployment

### Backend (Railway/Heroku)
- Set environment variables in your hosting platform
- Deploy from `backend/` directory
- Use `uvicorn app.main:app --host 0.0.0.0 --port $PORT`

### Frontend (Vercel)
- Deploy from `frontend/` directory
- Configure environment variables in Vercel dashboard

## Troubleshooting

### Backend Issues
- **Module not found**: Make sure virtual environment is activated and dependencies are installed
- **Database connection errors**: Verify `DATABASE_URL` in `.env`
- **Port already in use**: Change port with `--port 8001`

### Frontend Issues
- **Next.js not found**: Run `npm install` in `frontend/` directory
- **Build errors**: Check Node.js version (18+ required)
- **API connection errors**: Verify `NEXT_PUBLIC_BACKEND_URL` in `.env.local`

## License

[Add your license here]
