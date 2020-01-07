import pathlib
import python_template
import json

PACKAGE_ROOT = pathlib.Path(python_template.__file__).resolve().parent
PACKAGE_DIR = pathlib.Path(python_template.__file__)
DATA_DIR = PACKAGE_ROOT / 'data'

with open(PACKAGE_ROOT / 'config.json') as file:
    configuration = json.load(file)

if configuration["MODE"] != "DEVELOPMENT":
    if "DATA_DIR" in configuration:
        DATA_DIR = pathlib.Path(configuration['DATA_DIR'])