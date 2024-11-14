"""Model of a preprocessing run."""

from pathlib import Path

from pydantic import BaseModel


class PreprocessingRun(BaseModel):
    """Model of a preprocessing run."""

    image_path: Path
    pipeline_version: str
