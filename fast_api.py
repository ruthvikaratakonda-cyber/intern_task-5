from fastapi import FastAPI, Request
import httpx

app = FastAPI()

SERVICES = {
    "user": "http://localhost:8001",
    "product": "http://localhost:8002",
    "order": "http://localhost:8003"
}

@app.api_route("/api/{service}/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def gateway(service: str, path: str, request: Request):
    url = f"{SERVICES[service]}/{path}"

    async with httpx.AsyncClient() as client:
        response = await client.request(
            request.method,
            url,
            headers=request.headers.raw,
            content=await request.body()
        )
    return response.json()