#!/bin/bash
set -e
cd /root/task

echo "Starting Docker containers..."
docker-compose up -d

# Wait for PostgreSQL to be ready
until docker exec bookstore_postgres pg_isready -U bookstore_user -d bookstore_db; do
  echo "Waiting for PostgreSQL to be available..."
  sleep 2
done

echo "PostgreSQL is ready! Setting up schema..."
docker exec -i bookstore_postgres psql -U bookstore_user -d bookstore_db < /root/task/schema.sql

echo "Populating sample data..."
docker exec -i bookstore_postgres psql -U bookstore_user -d bookstore_db < /root/task/data/sample_data.sql

echo "Validating API healthcheck..."
sleep 2
API_UP=false
for i in {1..10}; do
  if curl -sf http://localhost:8000/health; then
    API_UP=true
    break
  else
    sleep 2
  fi
done
if [ "$API_UP" = true ]; then
  echo "API is up and running!"
else
  echo "API failed to start or connect to DB."
  exit 1
fi
