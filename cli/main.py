import typer
from rich import print as rprint
from cli.commands import run_app, diff_app, sync_app, report_app, debug_app

app = typer.Typer(
    name="living-docs",
    help="Living Docs Architecture Synchronizer - MCP-powered",
    rich_markup_mode="rich",
    add_completion=False,
)

app.add_typer(run_app, name="run")
app.add_typer(diff_app, name="diff")
app.add_typer(sync_app, name="sync")
app.add_typer(report_app, name="report")
app.add_typer(debug_app, name="debug")

if __name__ == "__main__":
    app()