from core.models.pr import PREvent
from core.github.client import GitHubClient
from utils.logging import logger

async def parse_github_pr_payload(payload: dict) -> PREvent:
    if "pull_request" not in payload or "repository" not in payload:
        raise ValueError("Invalid payload: expected GitHub pull_request event shape")

    pr_payload = payload["pull_request"]
    diff = ""
    if pr_payload.get("diff_url"):
        try:
            diff = await GitHubClient().fetch_pr_diff(pr_payload["diff_url"])
        except Exception as e:
            logger.warning(f"Could not fetch PR diff, continuing with empty diff: {e}")

    return PREvent(
        pr_number=pr_payload.get("number"),
        repo=payload["repository"].get("full_name", ""),
        action=payload.get("action", "opened"),
        author=pr_payload.get("user", {}).get("login", ""),
        diff=diff,
        description=pr_payload.get("body", "")
    )
