
# AI Prompt Library App

## Run
docker-compose up --build

## Backend API
- GET /prompts/
- POST /prompts/create/
- GET /prompts/{id}/

## Tech
Django + PostgreSQL + Redis + Docker

## Notes
- Redis handles view count
- Extend frontend with Angular CLI for full UI
