import json
from app.core.config import settings

try:
    import redis
except ImportError:
    redis = None

redis_client = None


def get_redis_client():
    global redis_client
    if redis_client is not None:
        return redis_client

    if redis is None:
        print("Redis package not installed, cache disabled")
        return None

    if not settings.REDIS_URL:
        return None

    try:
        client = redis.Redis.from_url(settings.REDIS_URL)
        client.ping()
        redis_client = client
        return redis_client
    except redis.RedisError as exc:
        print(f"Redis unavailable, cache disabled: {exc}")
        redis_client = None
        return None


def get_cached_prediction(key: str):
    client = get_redis_client()
    if client is None:
        return None

    try:
        value = client.get(key)
        print(f"Cache lookup for key: {key}")
        if value:
            return json.loads(value)
    except redis.RedisError as exc:
        print(f"Redis get failed, cache disabled: {exc}")
    return None


def set_cached_prediction(key: str, value: dict, ex: int = 3600):
    client = get_redis_client()
    if client is None:
        return

    try:
        client.setex(key, ex, json.dumps(value))
    except redis.RedisError as exc:
        print(f"Redis set failed, cache disabled: {exc}")
