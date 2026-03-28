import asyncio
import typer
from rich import print as rprint
from core.agent.core import MCPAgentCore
from core.models.pr import PREvent
from core.config import settings
from utils.logging import logger

run_app = typer.Typer()

SAMPLE_DIFF = """--- a/core/agent/core.py
+++ b/core/agent/core.py
@@ -1,3 +1,4 @@
+# updated agent logic
 from core.diff.preprocessor import DiffPreprocessor
 from core.agent.page_resolver import PageResolver
 from core.agent.confidence_scorer import ConfidenceScorer
"""

@run_app.command("pr")
def run_pr(pr_number: int, verbose: bool = False):
    """Trigger full pipeline for a specific PR"""
    logger.info(f"Starting sync for PR #{pr_number}")
    agent = MCPAgentCore()
    event = PREvent(
        pr_number=pr_number,
        repo=settings.repo,
        action="opened",
        author="cli-user",
        diff=SAMPLE_DIFF
    )
    result = asyncio.run(agent.process(event))
    rprint(f"[green]✅ Sync completed for PR #{pr_number}[/green]")
    rprint(result)
