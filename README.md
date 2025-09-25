Flask two-tier example with Postgres and Docker.

Services:
- web: Flask app served by Gunicorn
- db: Postgres

Run:
  docker-compose up --build

API:
  GET  /            -> health / hello
  GET  /users       -> list users
  POST /users       -> add user { "name": "Alice" }
