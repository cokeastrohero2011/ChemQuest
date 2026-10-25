# Gamified Homework Tracker - Replit Configuration

## Overview

A gamified homework tracking application that transforms task management into an engaging, game-like experience. The project uses Flask for the backend API and a single-page React application for the frontend. The application includes integration with OpenAI's API for enhanced features, themed as "TGA ChemQuest: Molecular Arena" based on the frontend template.

**Current Status:** Early development phase with basic scaffolding in place. The project has Flask backend structure and HTML template foundations, but requires React frontend initialization and core feature implementation.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture
- **Framework:** React (single-page application)
- **Current State:** Placeholder package.json; React app needs initialization
- **UI Theme:** Retro-futuristic "Molecular Arena" design with neon cyberpunk aesthetics
- **Styling:** Custom CSS with animated gradients, neon effects, and retro grid scanlines
- **API Communication:** Direct calls to Flask backend proxy endpoints

**Design Decision:** Single-page application architecture chosen for seamless user experience and simplified deployment. The gamified theme uses visual effects (animated nebula blobs, scanlines) to create an engaging interface that makes homework tracking feel less like a chore.

### Backend Architecture
- **Framework:** Flask 3.0.0 (Python web framework)
- **Server:** Gunicorn for production deployment
- **CORS:** Flask-Cors 4.0.0 for cross-origin resource sharing
- **Architecture Pattern:** RESTful API with proxy pattern for external services
- **File Structure:** 
  - `main.py` - Main application entry point
  - `templates/` - Static HTML templates served by Flask

**Design Decision:** Flask selected for its lightweight nature and simplicity, suitable for a school project while providing professional-grade capabilities. The proxy pattern for OpenAI API calls keeps sensitive API keys server-side, preventing exposure in client-side code.

### Data Storage
- **ORM:** SQLAlchemy 2.0.0
- **Database:** Not yet specified (Drizzle-compatible database may be added)
- **Current State:** SQLAlchemy included in dependencies but not yet implemented

**Design Decision:** SQLAlchemy provides database-agnostic ORM capabilities, allowing flexibility in choosing the final database solution (SQLite for development, PostgreSQL for production).

### Authentication & Security
- **API Key Management:** Environment variables via python-dotenv
- **Security Pattern:** Server-side proxy for external API calls
- **Current State:** Basic environment variable configuration in place

**Design Decision:** Storing sensitive credentials (OPENAI_API_KEY) in environment variables follows security best practices, preventing credential leakage in version control or client-side code.

## External Dependencies

### Third-Party APIs
- **OpenAI API:** Chat completions endpoint for AI-powered features
  - Accessed via proxy endpoint `/api/molecule`
  - Requires `OPENAI_API_KEY` environment variable
  - 30-second timeout configured for API calls

### Python Packages
- **Flask 3.0.0:** Web framework and routing
- **Flask-Cors 4.0.0:** Cross-origin resource sharing support
- **SQLAlchemy 2.0.0:** Database ORM and query builder
- **python-dotenv 1.0.0:** Environment variable management
- **requests:** HTTP library for external API calls
- **gunicorn:** WSGI HTTP server for production

### Frontend Dependencies
- **Current State:** Empty dependencies object in package.json
- **Planned:** React and associated tooling (to be added in Phase 2)

### Environment Requirements
- **OPENAI_API_KEY:** Required for AI features functionality
- **Server:** Configured to run on host 0.0.0.0, port 5000

### Development Tools
- **uv:** Python package installer (configured in `.config/uv/`)

**Integration Notes:** The OpenAI integration uses a secure proxy pattern where the frontend makes requests to `/api/molecule`, which the Flask backend forwards to OpenAI with proper authentication. This prevents API key exposure while maintaining clean separation of concerns.