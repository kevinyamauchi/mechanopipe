import pandas as pd

from mechanopipe.constants import (
    PROJECT_TABLE_FILE_PATH,
    PROJECT_TABLE_SAMPLE_NAME,
    PROJECT_TABLE_VOXEL_X,
    PROJECT_TABLE_VOXEL_Y,
    PROJECT_TABLE_VOXEL_Z,
)
from mechanopipe.project.utils import validate_project_table


def test_validate_project_table_valid():
    """Check that a valid table passes."""
    table = pd.DataFrame(
        {
            PROJECT_TABLE_FILE_PATH: ["test.tif"],
            PROJECT_TABLE_SAMPLE_NAME: ["sample_1"],
            PROJECT_TABLE_VOXEL_X: [0.75],
            PROJECT_TABLE_VOXEL_Y: [0.75],
            PROJECT_TABLE_VOXEL_Z: [0.75],
        }
    )

    table_valid = validate_project_table(table)
    assert table_valid


def test_validate_project_table_invalid():
    """Check that a table missing a column doesn't pass."""
    table = pd.DataFrame(
        {
            PROJECT_TABLE_FILE_PATH: ["test.tif"],
            PROJECT_TABLE_SAMPLE_NAME: ["sample_1"],
            PROJECT_TABLE_VOXEL_X: [0.75],
            PROJECT_TABLE_VOXEL_Y: [0.75],
        }
    )

    table_valid = validate_project_table(table)
    assert not table_valid
