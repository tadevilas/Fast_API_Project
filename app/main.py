from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from app.api import routes_auth as route_auth, route_predict
from app.middleware.logging_middleware import LoggingMiddleware
from app.core.exceptions import register_exception_handlers


app = FastAPI(title="Car Price Prediction API", version="1.0.0")

app.add_middleware(LoggingMiddleware)

app.include_router(route_auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(route_predict.router, prefix="/api", tags=["Prediction"])    

Instrumentator().instrument(app).expose(app)

register_exception_handlers(app)