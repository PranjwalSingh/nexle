# Setup

## Prerequisites
- Node.js (v18+)
- Python (3.10+)
- Supabase account

## Clone
```bash
git clone https://github.com/nexle-ca/nexle.git
cd nexle
```

## Backend
```bash
cd backend
python -m venv env
env\Scripts\activate        # Windows
source env/bin/activate     # Mac/Linux
pip install -r requirements.txt
cp .env.example .env        # fill in your values
uvicorn main:app --reload
```

## Frontend
```bash
cd frontend
npm install
cp .env.example .env        # fill in your values
npm run dev
```

## Environment Variables
See `.env.example` in both `backend/` and `frontend/` for required variables.

## Work in your brach
Work in dev-<your_name>

main is only for simplified mvp
main-dev for writing code for mvp
prod is for the actual product
dev-<your-name> for yourself
```