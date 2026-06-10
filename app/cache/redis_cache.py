import json
import redis
from app.core.config import settings


redis_client = redis.Redis.from_url(settings.REDIS_URL) 


def get_cached_prediction(key: str):
    value = redis_client.get(key)
    print(f"Cache lookup for key: {key}")
    if value:
        return json.loads(value)
    return None

def set_cached_prediction(key: str, value: dict, ex: int = 3600):
    redis_client.setex(key, ex, json.dumps(value))