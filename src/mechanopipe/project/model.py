"""A model for a mechanopipe project."""

import json
from os import PathLike
from pathlib import Path

from pydantic import BaseModel, field_validator

from mechanopipe.preprocess.model import PreprocessingRun


class MechanoPipeProject(BaseModel):
    """Model representing a mechanopipe project."""

    root_path: Path
    preprocessing_runs: list[PreprocessingRun]
    pipeline_version: str

    @field_validator("root_path")
    @classmethod
    def validate_root_path(cls, v: PathLike):
        """Coerce the root path and verify that it exists."""
        if not isinstance(v, Path):
            v = Path(v)

        if not v.exists():
            error_message = f"The root path '{v}' does not exist."
            raise FileNotFoundError(error_message)
        return v

    def to_json_file(self, file_path: str, indent: int = 2) -> None:
        """Save the model as a JSON file."""
        with open(file_path, "w") as f:
            # serialize the model
            json.dump(self.model_dump(), f, indent=indent)


class MechanoPipeSample(BaseModel):
    """Model representing a mechanopipe sample.

    Parameters
    ----------
    raw_data_path : Path
        The absolute path to the raw data file.
    sample_name : str
        The name for the sample. Ideally this should be unique.
    voxel_size_um : tuple[float, float, float]
        The voxel size in microns.
    pipeline_version : str
        The version of mechanopipe used to generate this config.
    """

    raw_data_path: Path
    sample_name: str
    voxel_size_um: tuple[float, float, float]
    pipeline_version: str

    def to_json_file(self, file_path: str, indent: int = 2) -> None:
        """Save the model as a JSON file."""
        with open(file_path, "w") as f:
            # serialize the model
            json.dump(self.model_dump(), f, indent=indent)
