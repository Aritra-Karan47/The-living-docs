from fastapi import APIRouter, Request, HTTPException
from core.github.payload import PREvent
from core.agent.core import MCPAgentCore
from utils.logging import logger

router = APIRouter()

@router.post("/github")
async def github_webhook(request: Request):
    payload = await request.json()
    # Validate secret in production
    event = PREvent.model_validate(payload)
    logger.info(f"Received GitHub webhook for PR #{event.pr_number}")
    agent = MCPAgentCore()
    result = await agent.process(event)
    return {"status": "processed", "result": result}