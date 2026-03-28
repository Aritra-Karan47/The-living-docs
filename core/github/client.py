from utils.logging import logger

class GitHubClient:
    async def post_comment(self, pr_number: int, message: str):
        logger.info(f"[GitHub] PR #{pr_number} comment: {message}")
