dev: django
  caddy start

stopdev:
  caddy stop

django:
  uv run ./manage.py runserver &

tw:
  uv run ./manage.py tailwind start

prod:
  hypercorn -c hypercorn.toml --workers 8 vgarchive.asgi:app

static:
  uv run ./manage.py collectstatic

migrate:
  uv run ./manage.py migrate

migrateup:
  uv run ./manage.py makemigrations
