from setuptools import setup
from typing import List
from pyservicenow import __version__, __module_name__
import os

def get_dependancies() -> List[str]:
    dependancies = []

    with open("./requirements.txt","r") as file:
        dependancies = file.read().split("\n")
        dependancies = filter(None, dependancies)
        dependancies = filter(bool, dependancies)
        dependancies = filter(len, dependancies)
        dependancies = list(filter(None, dependancies))

    return dependancies

def get_packages() -> List[str]:
    directory = os.path.join(".","pyservicenow")

    _packages = [x[0].replace("\\",".") for x in os.walk(directory) if "__pycache__" not in x[0]]

    return _packages

setup(
    name = __module_name__,
    version = __version__,
    author = "michaeldcanady",
    author_email = "",
    description = ("Service-Now API wrapper"),
    license = "MIT",
    #keywords = "example documentation tutorial",
    url = "https://github.com/michaeldcanady/pyservicenow",
    packages=get_packages(),
    install_requires=get_dependancies()
    #long_description=read('README'),,
)