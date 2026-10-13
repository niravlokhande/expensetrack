ExpenseTrack



ExpenseTrack is a full-stack expense-tracking application. Users can add expenses, view saved records, and see totals grouped by category. The project uses Docker Compose to run an Nginx frontend, FastAPI backend, and MySQL database together.

Architecture

Browser → Nginx → FastAPI → MySQL



Tech stack

Area

Technology

Frontend

HTML, JavaScript, Nginx

Backend

Python 3.12, FastAPI, Uvicorn

Database

MySQL 8.4

Database access

PyMySQL

Containers

Docker and Docker Compose

Testing

pytest, httpx, Bash smoke test

CI/CD

GitHub Actions

Container registry

GitHub Container Registry (GHCR)

Run locally

git clone https://github.com/niravlokhande/expensetrack.git
cd expensetrack
cp .env.example .env
docker compose up --build

Open the app at http://localhost:8080.

To stop the application:

docker compose down

To delete the database data and start again from scratch:

docker compose down -v

Testing

Run the full smoke test after starting the containers:

./scripts/smoke_test.sh

The test checks that the API becomes healthy, creates an expense, and confirms it can be read back from MySQL.

CI/CD pipeline

GitHub Actions runs three jobs:

test — starts MySQL, loads the schema, and runs the FastAPI pytest tests.

smoke-test — builds and starts the complete Docker Compose stack, then runs the smoke test script.

build-and-push — after a successful push to main, builds backend and frontend images and publishes them to GitHub Container Registry.

Screenshots

ExpenseTrack application



Successful GitHub Actions pipeline



What I learned

How to build a multi-container application with Docker Compose.

How FastAPI connects to MySQL using parameterized SQL queries.

How Docker volumes keep database data after containers restart.

How health checks control the startup order of dependent services.

How GitHub Actions can test, build, and publish container images.

Why passwords belong in an ignored .env file rather than Git.

Future improvements

Add edit and delete expense endpoints.

Add date filtering and pagination.

Improve frontend validation and error messages.

Add user accounts and authentication.

Add Trivy container-image security scanning.

Add automated database backups.

Deploy the application to a cloud platform.

