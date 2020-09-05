# Always prefer setuptools over distutils
from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="yaml2plist",
    version="0.2.0",
    description="Generate plist files from yaml input",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/benjamineskola/yaml2plist",
    author="Benjamin Eskola",
    author_email="ben@eskola.uk",
    license="Creative Commons Attribution-NonCommercial 4.0 International",
    classifiers=["License :: Free for non-commercial use"],
    packages=find_packages(),
    python_requires=">=3.5, <4",
    install_requires=[],
    entry_points={"console_scripts": ["yaml2plist=yaml2plist:main"]},
    project_urls={
        "Bug Reports": "https://gitlab.com/benjamineskola/yaml2plist/issues",
        "Source": "https://gitlab.com/benjamineskola/yaml2plist/",
    },
)
