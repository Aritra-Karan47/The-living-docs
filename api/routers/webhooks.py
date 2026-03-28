from fastapi import APIRouter, Request, HTTPException
from core.github.payload import parse_github_pr_payload
from core.agent.core import MCPAgentCore
from utils.logging import logger

router = APIRouter()

@router.post("/github")
async def github_webhook(request: Request):
    payload = await request.json()

    # Only process PR open/update events for docs sync
    action = payload.get("action", "")
    if action not in {"opened", "synchronize", "reopened"}:
        logger.info(f"Skipping unsupported PR action: {action}")
        return {"status": "skipped", "action": action}

    try:
        event = await parse_github_pr_payload(payload)
    except Exception as e:
        logger.error(f"Failed to parse GitHub payload: {e}")
        raise HTTPException(status_code=400, detail=str(e))

    logger.info(f"Received GitHub webhook for PR #{event.pr_number} in {event.repo}")
    agent = MCPAgentCore()
    result = await agent.process(event)
    return {"status": "processed", "result": result}
