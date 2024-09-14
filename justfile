dev: stopdev django
  caddy start

stopdev:
  -caddy stop

django:
  uv run ./manage.py runserver &

tw:
  cd ./vgarchive/theme/static_src/ && postcss -w --verbose \
    ./src/styles.css \
    -o ../static/css/dist/styles.css

fonts:
  python scripts/bi-css.py
  python scripts/min-fonts.py

prod:
  hypercorn -c hypercorn.toml --workers 8 vgarchive.asgi:app

static:
  uv run ./manage.py collectstatic

migrate:
  uv run ./manage.py migrate

migrateup:
  uv run ./manage.py makemigrations
