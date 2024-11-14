"""Utilities for setting up projects."""

import logging

import pandas as pd

from mechanopipe.constants import PROJECT_TABLE_COLUMNS

logger = logging.getLogger(__name__)


def validate_project_table(project_table: pd.DataFrame) -> bool:
    """Verify that the project table has the required columns.

    See mechanopipe.constants.PROJECT_TABLE_COLUMNS for the
    required columns.

    Parameters
    ----------
    project_table : pd.DataFrame
        The project table to be validated.

    Returns
    -------
    bool
        Returns True if all required columns are present.
    """
    table_valid = True
    for column_name in PROJECT_TABLE_COLUMNS:
        if column_name not in project_table.columns:
            message = f"Column {column_name} not in the project table."
            logger.info(message)
            table_valid = False
    return table_valid
