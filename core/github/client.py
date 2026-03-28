import httpx
from core.config import settings
from utils.logging import logger

class GitHubClient:
    async def fetch_pr_diff(self, diff_url: str) -> str:
        headers = {
            "Accept": "application/vnd.github.v3.diff",
        }
        if settings.github_api_token:
            headers["Authorization"] = f"token {settings.github_api_token}"

        async with httpx.AsyncClient() as client:
            resp = await client.get(diff_url, headers=headers, timeout=30.0)
            resp.raise_for_status()
            return resp.text

    async def post_comment(self, pr_number: int, message: str):
        logger.info(f"[GitHub] PR #{pr_number} comment: {message}")
