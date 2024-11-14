"""Functions to set up a project."""

import multiprocessing as mp
import os
import shutil
from functools import partial
from pathlib import Path

import pandas as pd

from mechanopipe.constants import (
    PROJECT_TABLE_FILE_PATH,
    PROJECT_TABLE_SAMPLE_NAME,
    PROJECT_TABLE_VOXEL_X,
    PROJECT_TABLE_VOXEL_Y,
    PROJECT_TABLE_VOXEL_Z,
    SAMPLE_CONFIG_NAME,
)
from mechanopipe.project.model import MechanoPipeSample
from mechanopipe.project.utils import validate_project_table
from mechanopipe.utils import get_pipeline_version


def initialize_project_from_table(
    project_table: pd.DataFrame, root_directory: Path, n_processes: int = 1
) -> None:
    """Create a project directory from a table of images.

    Parameters
    ----------
    project_table : pd.DataFrame
        The table to build the project from.
    root_directory : Path
        The path to the directory where the project will be saved.
        If it doesn't exist, it will be created.
    n_processes : int
        The number of processes to use. If set to 1, multiprocessing
        will not be used. Default value is 1.
    """
    table_valid = validate_project_table(project_table)
    if not table_valid:
        raise ValueError("Table is not valid. See log for details.")

    # make the root directory
    os.makedirs(root_directory, exist_ok=True)

    # initialize each dataset
    if n_processes == 1:
        for _, row in project_table.iterrows():
            initialize_sample_from_table_row(row=row, root_directory=root_directory)
    elif n_processes > 1:
        table_rows = [row for _, row in project_table.iterrows()]
        initialize_function = partial(
            initialize_sample_from_table_row, root_directory=root_directory
        )
        with mp.get_context("spawn").Pool() as pool:
            pool.map(initialize_function, table_rows)
    else:
        error_message = f"Invalid number of processes: {n_processes}"
        raise ValueError(error_message)


def initialize_sample_from_table_row(row: pd.Series, root_directory: Path) -> None:
    """Initialize a sample from a sample table row.

    See mechanopipe.constants.PROJECT_TABLE_COLUMNS for the
    required columns.

    Parameters
    ----------
    row : pd.Series
        The row to initialize from.
    root_directory : Path
        The path to the root directory to create the sample in.
    """
    initialize_sample(
        file_path=row[PROJECT_TABLE_FILE_PATH],
        sample_name=row[PROJECT_TABLE_SAMPLE_NAME],
        voxel_size_um=(
            row[PROJECT_TABLE_VOXEL_Z],
            row[PROJECT_TABLE_VOXEL_Y],
            row[PROJECT_TABLE_VOXEL_X],
        ),
        root_directory=root_directory,
    )


def initialize_sample(
    file_path: os.PathLike,
    sample_name: str,
    voxel_size_um: tuple[float, float, float],
    root_directory: Path,
    copy_raw_data: bool = False,
) -> None:
    """Initialize a sample.

    This function:
        - creates a directory for the sample (root_directory/sample_name)
        - writes a sample config
        - if requested, copies the file.

    Parameters
    ----------
    file_path : os.PathLike,
        The path to the raw image.
    sample_name : str
        The name of the sample. This will be referred to
        in downstream processing. Ideally it is unique.
    voxel_size_um : tuple[float, float, float]
        The size of the voxels in microns.
    root_directory : Path
        The base directory to create the sample folder in.
    copy_raw_data : bool
        If True, copy the raw data into the sample directory.
        Default value is False.
    """
    file_path = Path(file_path)

    # make the sample directory
    sample_directory_path = root_directory / sample_name
    sample_directory_path.mkdir(exist_ok=True)

    # make the sample model
    sample_model = MechanoPipeSample(
        raw_data_path=file_path,
        sample_name=sample_name,
        voxel_size_um=voxel_size_um,
        pipeline_version=get_pipeline_version,
    )

    # write the sample model
    sample_model_path = sample_directory_path / SAMPLE_CONFIG_NAME
    sample_model.to_json_file(sample_model_path)

    if copy_raw_data:
        # copy the data
        shutil.copy2(file_path, sample_directory_path)
