import pathlib
import python_template
import json
import sys

PACKAGE_ROOT = pathlib.Path(python_template.__file__).resolve().parent.parent
PACKAGE_DIR = pathlib.Path(python_template.__file__).resolve().parent
DATA_DIR = PACKAGE_ROOT / 'data'
SYS_PREFIX_PARENT = pathlib.Path(sys.prefix).resolve().parent

if (SYS_PREFIX_PARENT / 'config.json').is_file():
    with open(SYS_PREFIX_PARENT / 'config.json') as file:
        configuration = json.load(file)
else:
    with open(PACKAGE_DIR/ 'config.json') as file:
        configuration = json.load(file)

if configuration["MODE"] != "DEVELOPMENT":
    if "DATA_DIR" in configuration:
        DATA_DIR = pathlib.Path(configuration['DATA_DIR'])