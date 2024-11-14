"""A model for a mechanopipe project."""

from os import PathLike
from pathlib import Path

from pydantic import BaseModel, field_validator

from mechanopipe.preprocess.model import PreprocessingRun


class MechanoPipeProject(BaseModel):
    """Model representing a mechanopipe project."""

    root_path: Path
    preprocessing_runs: list[PreprocessingRun]

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
