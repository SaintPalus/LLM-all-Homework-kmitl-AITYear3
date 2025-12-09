## Do this first
docker compose up -d
## FrontEnd
uv run alembic upgrade head
uv run python main.py
## Backend
npm install
npm run dev
