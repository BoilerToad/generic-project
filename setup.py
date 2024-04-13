from setuptools import setup, find_packages

with open("config/requirements.txt") as requirement_file:
    requirements = requirement_file.read().split()

setup(
    name="generic_project",
    description="A simple project for GitHub.",
    version="1.0.0",
    author="Name",
    author_email="Name@domain.com",
    install_requires=requirements,
    packages=find_packages(exclude=["generic-project"]), # package = any folder with an __init__.py file
)