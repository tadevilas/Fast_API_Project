from fastapi import APIRouter, Depends
from typing import Optional
from pydantic import BaseModel
from app.core.dependencies import get_api_key, get_current_user
from app.api.services.model_service import predict_car_price

router = APIRouter()


class CarFeatures(BaseModel):
    """Pydantic model for car features accepted by the prediction endpoint.

    Note: `selling_price` is the target and should not be provided when
    requesting a prediction.
    """
    company: str
    year: int
    owner: str
    fuel: str
    seller_type: str
    transmission: str
    km_driven: int
    mileage_mpg: Optional[float] = None
    engine_cc: Optional[float] = None
    max_power_bhp: Optional[float] = None
    torque_nm: Optional[float] = None
    seats: Optional[float] = None
    

@router.post("/predict")
def predict_price(car: CarFeatures, user = Depends(get_current_user), api_key: str = Depends(get_api_key)):
    """Endpoint to predict car price based on input features.

    This endpoint requires a valid API key and JWT token for authentication.
    It accepts car features as input and returns the predicted price.
    """
    prediction = predict_car_price(car.model_dump())
    return {"predicted_price": prediction["predicted_price"]}