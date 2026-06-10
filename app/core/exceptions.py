from fastapi import FastAPI, HTTPException  
from fastapi.responses import JSONResponse


def register_exception_handlers(app: FastAPI):
    @app.exception_handler(Exception)
    async def unhandled_exception_handler(request, exc: Exception):
        return JSONResponse(
            status_code=500,
            content={"detail": str(exc)},
            )
