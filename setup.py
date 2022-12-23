from setuptools import setup
from pyservicenow import __version__, __module_name__
import os

directory = os.path.join(".","pyservicenow")

_packages = [x[0].replace("\\",".") for x in os.walk(directory) if "__pycache__" not in x[0]]

setup(
    name = __module_name__,
    version = __version__,
    author = "dmcanady",
    author_email = "dmcanady@liberty.edu",
    description = ("Service-Now API wrapper"),
    license = "MIT",
    #keywords = "example documentation tutorial",
    url = "https://bitbucket.os.liberty.edu/projects/DMG/repos/graph_python_module",
    packages=_packages,
    #long_description=read('README'),,
)