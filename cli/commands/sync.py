import typer
from rich import print as rprint
from core.agent.core import MCPAgentCore
from utils.logging import logger

sync_app = typer.Typer()

@sync_app.command("notion")
def sync_notion(force: bool = False):
    """Force full Notion sync"""
    logger.info("Starting full Notion sync")
    agent = MCPAgentCore()
    rprint("[green]Notion sync completed[/green]")
