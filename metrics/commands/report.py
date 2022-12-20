""" Commands to send Test Reports to MongoDB """

import json
import logging
from pathlib import Path
from typing import Dict, List

import typer
from pymongo import MongoClient
from rich.console import Console

from metrics import config, transform

log = logging.getLogger(__name__)
app = typer.Typer(rich_markup_mode="rich")
console = Console()


def read_report_json(report_file=".report.json") -> Dict:
    """Return a report JSON file as a Python Dictionary.

    * This looks for the file starting from the Project Root.
    """
    # 1. Get the absolute path of the Project Root
    path = Path(__file__).absolute().parent.parent.parent

    # 2. Load the file as JSON and return it
    with open(path.joinpath(report_file), "r") as file:
        report = json.load(file)
    return report


@app.command(help="Preprocess the given report and send it to MongoDB.")
def send(
    report_file: str = typer.Argument(..., help="The report JSON file to send"),
    tags: List[str] = typer.Argument(..., help="List of tags or categories to add to the report"),
):
    # 1. Read the report JSON we want to send to MongoDB
    report = read_report_json(report_file)

    # 2. Preprocess the data so it's in a better format for MongoDB
    report["created"] = transform.unix_timestamp_to_datetime(report["created"])
    report["tags"] = tags

    # 3. Connect to MongoDB and send the data!
    with MongoClient(config.MONGODB_ATLAS_URI) as mongo:
        db = mongo.get_database("test_results")

        result = db.results.insert_one(report)
        console.print("Test Report added to MongoDB:", result.acknowledged)
