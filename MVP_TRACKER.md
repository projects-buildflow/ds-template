# BuildFlow DS - MVP Implementation Tracker

**Project:** Cartly Virtual Data Internship Platform
**Last Updated:** 2026-01-16
**Overall Progress:** ~75% Complete

---

## Project Overview

A full-stack platform for a simulated 4-week data science internship with:
- GitHub-based task submissions with automated testing
- In-platform Team Chat for engagement and support
- AI-powered code review (Claude)
- Admin dashboard for cohort management
- XP/gamification system

**Components:**
1. **Backend** (FastAPI) - API, webhooks
2. **Frontend** (Next.js) - Student dashboard, admin portal, Team Chat
3. **GitHub Template** - Intern submission repo with CI/CD
4. **Database** (Supabase/PostgreSQL) - Data persistence

---

## Component Status Summary

| Component | Status | Progress |
|-----------|--------|----------|
| Backend API | Working | 90% |
| Team Chat | Working | 90% |
| Frontend (Student) | Working | 85% |
| Frontend (Admin) | **Not Started** | 0% |
| GitHub Template | **Complete** | 100% |
| Database Schema | Complete | 100% |

---

## 1. Backend API (`/backend`)

### Implemented & Working

| Route | Endpoints | Status |
|-------|-----------|--------|
| `/students` | register, get, progress, verify-token, activity, update | Done |
| `/cohorts` | get, stats, leaderboard, students, analytics | Done |
| `/tasks` | list, by-week, by-id, student-tasks, summary | Done |
| `/admin` | create/list/update cohorts, add students, bulk import, broadcast | Done |
| `/webhooks` | github (test results), ai-review-complete | Done |
| `/auth` | oauth (authorize, callback, unlink) | Done |

### Partially Working

| Feature | Issue |
|---------|-------|
| Task locking | `UNLOCK_ALL_TASKS = True` - disabled for testing |
| In-app messages | Fixed - now sends via Team Chat |

### Not Implemented

- [ ] Admin authentication (endpoints are unprotected)
- [x] Peer review converted to PR-based task (code review guidelines document)
- [ ] Certificate generation
- [ ] Email notifications
- [ ] Student filtering/search endpoint
- [ ] Data export (CSV/PDF)

---

## 2. Frontend - Student Dashboard (`/frontend`)

### Implemented Pages

| Page | Features | Status |
|------|----------|--------|
| `/login` | Email/password auth | Done |
| `/signup` | Registration | Done |
| `/onboarding` | Collect name, GitHub | Done |
| `/dashboard` | Progress, current task, stats | Done |
| `/tasks` | All 16 tasks by week | Done |
| `/tasks/[id]` | Task details, submission guide | Done |
| `/leaderboard` | Cohort rankings | Done |
| `/profile` | Student stats, submissions | Done |
| `/help` | Resources and FAQ | Done |

### Components

- NavHeader, DashboardWrapper, WeekProgress, ProgressBar
- TaskCard, LeaderboardTable, TokenSubmitForm
- WelcomeModal, OnboardingForm

---

## 3. Frontend - Admin Dashboard (NOT IMPLEMENTED)

### Required for MVP

- [ ] **`/admin`** - Admin home/overview
- [ ] **`/admin/cohorts`** - List all cohorts
- [ ] **`/admin/cohorts/new`** - Create new cohort
- [ ] **`/admin/cohorts/[id]`** - View/edit cohort details
- [ ] **`/admin/cohorts/[id]/students`** - Manage students
- [ ] **`/admin/cohorts/[id]/analytics`** - Cohort analytics
- [ ] **`/admin/students`** - All students across cohorts
- [ ] **`/admin/students/[id]`** - Individual student view

### Admin Features Needed

| Feature | Description | Priority |
|---------|-------------|----------|
| Cohort CRUD | Create, view, edit, archive cohorts | High |
| Student management | Add, remove, view students | High |
| Bulk student import | CSV upload for multiple students | High |
| Progress monitoring | View student progress across cohort | High |
| Manual overrides | Override XP, task status, roles | Medium |
| Broadcast messages | Send messages as personas | Medium |
| Analytics dashboard | Completion rates, XP distribution | Medium |
| GitHub repo creation | Auto-create cohort repos | Medium |

---

## 4. GitHub Template (`/github-template`)

### Week 1: Onboarding (100% Complete)

| Task | XP | Test | Docs | Instructions | Status |
|------|-----|------|------|--------------|--------|
| 1.1 Environment Setup | 25 | `test_1_1.py` | Done | Done | Complete |
| 1.2 First Bug Fix | 50 | `test_1_2.py` | Done | Done | Complete |
| 1.3 Fix Date Bug | 50 | `test_1_3.py` | Done | Done | Complete |
| 1.4 Document the Fix | 25 | `test_1_4.py` | Done | Done | Complete |

### Week 2: Data Quality (100% Complete)

| Task | XP | Test | Docs | Instructions | Status |
|------|-----|------|------|--------------|--------|
| 2.1 Data Profiling | 75 | `test_2_1.py` | Done | Done | Complete |
| 2.2 Validation Schema | 75 | `test_2_2.py` | Done | Done | Complete |
| 2.3 Data Cleaning | 100 | `test_2_3.py` | Done | Done | Complete |
| 2.4 Code Review | 50 | `test_2_4.py` | Done | Done | Complete |

### Week 3: Analysis (100% Complete)

| Task | XP | Test | Docs | Instructions | Status |
|------|-----|------|------|--------------|--------|
| 3.1 Revenue Investigation | 100 | `test_3_1.py` | Done | Done | Complete |
| 3.2 SQL Cohort Analysis | 75 | `test_3_2.py` | Done | Done | Complete |
| 3.3 Query Optimization | 75 | `test_3_3.py` | Done | Done | Complete |
| 3.4 Dashboard Creation | 100 | `test_3_4.py` | Done | Done | Complete |

### Week 4: Capstone (100% Complete)

| Task | XP | Test | Docs | Instructions | Status |
|------|-----|------|------|--------------|--------|
| 4.1 Pipeline Architecture | 100 | `test_4_1.py` | Done | Done | Complete |
| 4.2 Implement Pipeline | 125 | `test_4_2.py` | Done | Done | Complete |
| 4.3 Debug AI Code | 75 | `test_4_3.py` | Done | Done | Complete |
| 4.4 Final Presentation | 150 | `test_4_4.py` | Done | Done | Complete |

### Task Starter Files

| File | Location | Status |
|------|----------|--------|
| Buggy validator | `week-4/task-4.3/ai_generated_validator.py` | Done |
| Slow query | `week-3/task-3.3/slow_query.sql` | Done |
| Data loader (with bug) | `src/data_loader.py` | Done |
| INSTRUCTIONS.md | All 16 task folders | Done |

### Infrastructure (Complete)

| Component | Status |
|-----------|--------|
| CI/CD workflows (4 files) | Done |
| Data generation script | Done |
| 8 CSV datasets (83K rows) | Done |
| Test configuration (conftest.py) | Done |
| Requirements.txt | Done |

---

## 5. Database Schema (Complete)

| Table | Description | Status |
|-------|-------------|--------|
| students | Student profiles, progress, XP | Done |
| cohorts | Cohort metadata, settings | Done |
| tasks | 16 tasks with metadata | Done |
| submissions | Task submissions, results | Done |
| programs | Program templates | Done |
| scheduled_messages | Narrative/broadcast messages | Done |

---

## Priority Checklist for MVP

### P0 - Must Have

- [ ] **Admin Dashboard** - Create/manage cohorts and students
- [x] Week 2 documentation (`docs/week-2-tasks.md`)
- [x] Task 2.4 test file
- [x] Week 3 tasks (3.1-3.4) - tests and instructions
- [x] Week 4 tasks (4.1-4.4) - tests and instructions
- [x] Week 3 documentation (`docs/week-3-tasks.md`)
- [x] Week 4 documentation (`docs/week-4-tasks.md`)
- [x] `week-4/task-4.3/ai_generated_validator.py` (buggy file)
- [x] `week-3/task-3.3/slow_query.sql` (slow query for optimization)
- [x] `tests/conftest.py` - Add student_path fixture

### P1 - Should Have

- [ ] Admin authentication on backend endpoints
- [x] Broadcast messages sending via Team Chat
- [ ] Task locking based on prerequisites (set `UNLOCK_ALL_TASKS = False`)
- [x] `src/data_loader.py` for Task 1.3 (with intentional bug)
- [x] Task starter templates in week folders (INSTRUCTIONS.md)

### P2 - Nice to Have

- [ ] Certificate generation
- [x] Peer review system - converted to PR-based task
- [ ] Email notifications
- [ ] Data export (CSV/PDF)
- [ ] Advanced analytics dashboard

---

## Recent Changes (2026-01-16)

### GitHub Template
- Added `student_path` fixture to `tests/conftest.py`
- Created `docs/week-2-tasks.md`, `docs/week-3-tasks.md`, `docs/week-4-tasks.md`
- Created test files: `test_2_4.py`, `test_3_1.py` through `test_4_4.py`
- Created `src/data_loader.py` with intentional date parsing bug
- Created `week-4/task-4.3/ai_generated_validator.py` with 5 bugs
- Created `week-3/task-3.3/slow_query.sql` for optimization task
- Created 16 `INSTRUCTIONS.md` files in all task folders

### Backend
- Implemented broadcast message functionality in `admin.py`
- Updated `scheduled_messages.py` to handle broadcast trigger type

---

## Notes from PRD

**In MVP Scope (per PRD):**
- Week 1-4 content (16 tasks)
- GitHub repo with all task files
- GitHub Actions for automated testing
- Custom Claude code review
- Claude vision review for Power BI screenshots
- Team Chat with AI personas
- XP system and leaderboard
- Role progression
- Narrative messages (pre-written)
- Synthetic data generation
- Basic cohort management API

**NOT in MVP Scope (per PRD):**
- Partner admin portal (web UI) - *But user wants this*
- CodeRabbit integration
- Certificate generation (manual for MVP)
- Advanced analytics dashboard
- Multiple company narratives
- Week 5-8 content

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | FastAPI, Python 3.11 |
| Frontend | Next.js 15, React, Tailwind |
| Database | PostgreSQL (Supabase) |
| Team Chat | In-platform messaging |
| AI | Claude Sonnet (Anthropic API) |
| CI/CD | GitHub Actions |
| Auth | Supabase Auth |
