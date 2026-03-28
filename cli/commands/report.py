import typer
from core.staleness.tracker import StalenessTracker
from rich import print as rprint

report_app = typer.Typer()

@report_app.command()
def report(pr: int | None = None):
    """Generate staleness / freshness report"""
    tracker = StalenessTracker()
    report_data = tracker.generate_report(pr)
    rprint(report_data)