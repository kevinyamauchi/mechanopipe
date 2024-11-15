"""The main CLI entry point."""

from pathlib import Path
from typing import Annotated

import typer

app = typer.Typer(help="The mechanopipe command line interface.", no_args_is_help=True)


@app.command(no_args_is_help=True)
def initialize(
    project_table: Annotated[
        Path, typer.Argument(help="The path to the project table.")
    ],
    root_directory: Annotated[
        Path, typer.Argument(help="The path to the root directory for the project.")
    ],
):
    """Initialize a project."""
    import pandas as pd

    from mechanopipe.project.initialize import initialize_project_from_table

    # load the table
    project_table = pd.read_csv(project_table)

    # initialize the project
    initialize_project_from_table(
        project_table=project_table, root_directory=root_directory
    )


@app.command(no_args_is_help=True)
def preprocess():
    print("not implemented")


if __name__ == "__main__":
    # guard for multiprocessing compatibility
    app()
