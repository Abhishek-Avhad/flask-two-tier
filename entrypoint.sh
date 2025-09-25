#!/bin/sh
set -e

echo "Waiting for database..."
python - <<PY
import time, os
from sqlalchemy import create_engine
db_url = os.environ.get('DATABASE_URL') or 'postgresql://postgres:postgres@db:5432/postgres'
for i in range(30):
    try:
        engine = create_engine(db_url)
        conn = engine.connect()
        conn.close()
        print("Database is available")
        break
    except Exception as e:
        print("Database not ready, sleeping 1s")
        time.sleep(1)
else:
    raise SystemExit("Database did not become available in time")

from app import create_app, db
app = create_app()
with app.app_context():
    db.create_all()
print("DB tables ensured")
PY

exec gunicorn -b 0.0.0.0:5000 wsgi:app
