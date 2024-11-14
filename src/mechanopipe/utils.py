"""General utility functions."""

from importlib.metadata import version


def get_pipeline_version() -> str:
    """Get the current version of mechanopipe.

    Returns
    -------
    str
        Current version of mechanopipe.
    """
    return version("mechanopipe")
