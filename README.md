# Car Price Prediction API

A production-ready ML-based REST API built with FastAPI that predicts car prices. Features JWT authentication, Redis caching, Prometheus metrics, Grafana dashboards, and full Docker support.

---

## Features

- **ML Prediction** - Scikit-learn model served via FastAPI for real-time car price prediction
- **JWT Authentication** - Secure API access using JSON Web Tokens
- **Redis Caching** - Fast response times with Redis-backed caching layer
- **Prometheus Monitoring** - Auto-instrumented metrics exposed at `/metrics`
- **Grafana Dashboards** - Visual monitoring of API performance and usage
- **Dockerized** - Fully containerized with Docker and Docker Compose
- **Cloud Ready** - Render.com deployment config included

---

## Project Structure

```
Fast_API_Project/
├── app/
│   ├── api/
│   │   ├── routes_auth.py     # JWT login/token endpoints
│   │   └── route_predict.py   # Car price prediction endpoint
│   ├── cache/                 # Redis caching logic
│   ├── core/
│   │   └── exceptions.py      # Global exception handlers
│   ├── middleware/
│   │   └── logging_middleware.py  # Request logging middleware
│   ├── models/                # Trained ML model (model.joblib)
│   └── main.py                # FastAPI app entrypoint
├── data/                      # Raw/processed datasets
├── notebooks/                 # Jupyter notebooks for training/EDA
├── training/                  # Model training scripts
├── Dockerfile                 # Docker image definition
├── docker-compose.yaml        # Multi-service orchestration
├── prometheus.yaml            # Prometheus scrape config
├── render.yaml                # Render.com deployment config
├── requirement.txt            # Python dependencies
└── README.md
```

---

## Tech Stack

| Component       | Technology                              |
|----------------|------------------------------------------|
| API Framework  | FastAPI 0.110.0                          |
| ML Library     | Scikit-learn 1.3.2                       |
| Authentication | JWT (python-jose)                        |
| Caching        | Redis 5.0.4                              |
| Monitoring     | Prometheus + Grafana                     |
| Server         | Uvicorn                                  |
| Containerization | Docker + Docker Compose               |
| Language       | Python 3.10                              |

---

## Installation

### Option 1 - Run Locally

1. **Clone the repository**

```bash
git clone https://github.com/tadevilas/Fast_API_Project.git
cd Fast_API_Project
```

2. **Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirement.txt
```

4. **Set up environment variables**

Create a `.env` file in the root directory:

```env
API_KEY=your_api_key
JWT_SECRET_KEY=your_jwt_secret
REDIS_URL=redis://localhost:6379
MODEL_PATH=app/models/model.joblib
```

5. **Run the API**

```bash
uvicorn app.main:app --reload
```

API will be available at `http://localhost:8000`

---

### Option 2 - Run with Docker Compose

Starts all services: FastAPI app, Redis, Prometheus, and Grafana.

```bash
docker-compose up --build
```

| Service     | URL                        |
|------------|----------------------------|
| FastAPI API | http://localhost:8000      |
| API Docs   | http://localhost:8000/docs |
| Prometheus | http://localhost:9090      |
| Grafana    | http://localhost:3000      |
| Redis      | localhost:6379             |

---

## API Endpoints

### Authentication

| Method | Endpoint      | Description          |
|--------|--------------|----------------------|
| POST   | /auth/login  | Get JWT access token |

### Prediction

| Method | Endpoint           | Description              |
|--------|-------------------|--------------------------|
| POST   | /api/predict      | Predict car price        |

### Monitoring

| Method | Endpoint   | Description               |
|--------|-----------|---------------------------|
| GET    | /metrics  | Prometheus metrics        |
| GET    | /docs     | Swagger UI (interactive)  |
| GET    | /redoc    | ReDoc documentation       |

---

## Example Usage

**Step 1: Get a token**

```bash
curl -X POST "http://localhost:8000/auth/login" \
     -H "Content-Type: application/json" \
     -d '{"username": "admin", "password": "password"}'
```

**Step 2: Make a prediction**

```bash
curl -X POST "http://localhost:8000/api/predict" \
     -H "Authorization: Bearer <your_token>" \
     -H "Content-Type: application/json" \
     -d '{"year": 2020, "km_driven": 15000, "fuel": "Diesel", "transmission": "Manual", "owner": "First Owner"}'
```

---

## Deployment

This project includes a `render.yaml` for one-click deployment to [Render.com](https://render.com):

1. Push the repo to GitHub
2. Connect the repo on Render.com
3. Render will auto-detect `render.yaml` and deploy

---

## Dependencies

```
fastapi==0.110.0
uvicorn[standard]==0.29.0
python-jose==3.3.0
python-dotenv==1.0.1
scikit-learn==1.3.2
joblib
pandas
numpy==1.26.4
redis==5.0.4
prometheus-fastapi-instrumentator==8.0.0
```

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Author

**tadevilas** - [GitHub Profile](https://github.com/tadevilas)
