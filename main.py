import typer
from rich.console import Console
from metrics.commands import report


console = Console()
app = typer.Typer()
app.add_typer(report.app, name="report")


if __name__ == "__main__":
    app()
