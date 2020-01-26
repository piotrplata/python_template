from python_template import config
import os

with open(os.path.join(config.PACKAGE_DIR, 'VERSION')) as version_file:
    __version__ = version_file.read().strip()
