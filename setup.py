import pathlib
from setuptools import setup

#The directory containing this file
BASE = pathlib.Path(__file__).parent

# The text of the readme file
README = (BASE / "README.md").read_text()

#This call to setup does all the work