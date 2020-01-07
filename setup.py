from setuptools import setup, find_packages
from pathlib import Path

# What packages are required for this module to be executed?
def list_reqs(fname='requirements.txt'):
    with open(fname) as fd:
        return fd.read().splitlines()

# Load the package's __version__.py module as a dictionary.
ROOT_DIR = Path(__file__).resolve().parent
PACKAGE_DIR = ROOT_DIR
about = {}
with open(PACKAGE_DIR / 'python_template'/'VERSION') as f:
    _version = f.read().strip()
    about['__version__'] = _version

setup(
    name='python_template',
    version=about['__version__'],
    url='https://github.com/piotrplata/python_template.git',
    author='Piotr Plata',
    author_email='psplata@gmail.com',
    description='Python template',
    packages=find_packages(),
    install_requires=list_reqs(),
    entry_points={
        'console_scripts': ['python_template_run=python_template.entry_points:run']
    },
    include_package_data=True
)
