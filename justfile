dev: stopdev django
  caddy start

stopdev:
  -caddy stop

django:
  uv run ./manage.py runserver &

tw:
  cd ./vgarchive/theme/static_src/

fonts:
  python scripts/bi-css.py
  python scripts/min-fonts.py

add-bi-class:
  python scripts/add-class.py
  just fonts

prod:
  hypercorn -c hypercorn.toml --workers 8 vgarchive.asgi:app

static:
  uv run ./manage.py collectstatic

migrate:
  uv run ./manage.py migrate

migrateup:
  uv run ./manage.py makemigrations
