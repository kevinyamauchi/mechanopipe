"""Constants used by mechanopipe."""

# run directory name pattern: run_000X
RUN_DIRECTORY_NAME_TEMPLATE = "run_{run_index:04}"
RUN_DIRECTORY_GLOB_PATTERN = "run_[0-9]{4}"

# directory and file names for preprocessing
PREPROCESS_DIRECTORY = "preprocess"

# project table
PROJECT_TABLE_FILE_PATH = "file_path"
PROJECT_TABLE_SAMPLE_NAME = "sample_name"
PROJECT_TABLE_VOXEL_X = "voxel_um_x"
PROJECT_TABLE_VOXEL_Y = "voxel_um_y"
PROJECT_TABLE_VOXEL_Z = "voxel_um_z"

PROJECT_TABLE_COLUMNS = {
    PROJECT_TABLE_FILE_PATH,
    PROJECT_TABLE_SAMPLE_NAME,
    PROJECT_TABLE_VOXEL_X,
    PROJECT_TABLE_VOXEL_Y,
    PROJECT_TABLE_VOXEL_Z,
}

# name of the sample configuration file
SAMPLE_CONFIG_NAME = "sample_config.json"
