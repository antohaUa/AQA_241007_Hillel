# https://alembic.sqlalchemy.org/en/latest/
# alembic init <dir>
# alembic revision --autogenerate -m 'initial'
# alembic upgrade head

# migrate data
# https://pgloader.readthedocs.io/en/latest/ref/sqlite.html
# pg_dump -h localhost -U romblin --dbname=db --no-owner --schema-only --no-privileges > migration/schema.dump