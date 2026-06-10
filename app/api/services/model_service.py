import joblib
import os
import pandas as pd
from app.core.config import settings
from app.cache.redis_cache import get_cached_prediction, set_cached_prediction  


model = joblib.load(settings.MODEL_PATH)  # Load the trained model at startup   



def predict_car_price(data: dict):
    cache_key = " ".join([str(val) for val in data.values()])
    cached = get_cached_prediction(cache_key)
    if cached:
        print("Returning cached prediction")
        return cached
    
    input_data = pd.DataFrame([data])
    prediction = model.predict(input_data)[0]
    print(f"Predicted price: {prediction}")
    result = {"predicted_price": prediction}
    set_cached_prediction(cache_key, result)
    return result

              