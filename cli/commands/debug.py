import typer
from rich import print as rprint
from core.agent.core import MCPAgentCore
from utils.logging import logger

debug_app = typer.Typer()

@debug_app.command()
def debug(verbose: bool = True):
    """Run full debug pipeline"""
    logger.info("Debug mode started")
    agent = MCPAgentCore()
    rprint("[bold blue]Debug mode started[/bold blue]")
