import typer
from pathlib import Path
from core.diff.preprocessor import DiffPreprocessor
from rich import print as rprint

diff_app = typer.Typer()

@diff_app.command("analyze")
def analyze_diff(file: Path):
    """Debug diff preprocessing"""
    diff_text = file.read_text()
    processed = DiffPreprocessor().process(diff_text)
    rprint(processed)