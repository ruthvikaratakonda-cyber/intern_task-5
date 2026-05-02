import redis
import json

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

def get_products():
    cache = r.get("products")

    if cache:
        return json.loads(cache)

    # Simulated DB data
    products = [
        {"id": 1, "name": "Laptop"},
        {"id": 2, "name": "Phone"}
    ]

    r.setex("products", 60, json.dumps(products))
    return products