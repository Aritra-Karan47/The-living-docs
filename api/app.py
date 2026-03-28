from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routers.webhooks import router as webhook_router
from core.config import settings
from utils.logging import logger

app = FastAPI(title="Living Docs Sync API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(webhook_router, prefix="/webhook", tags=["webhooks"])

@app.get("/health")
async def health():
    return {"status": "healthy", "mcp_agent": "ready"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)