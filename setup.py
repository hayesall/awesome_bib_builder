from setuptools import setup
from setuptools import find_packages
from codecs import open
from os import path

# Get __version__ from _meta.py
with open(path.join("abb", "_meta.py")) as f:
    exec(f.read())

_here = path.abspath(path.dirname(__file__))
with open(path.join(_here, "README.md"), encoding="utf-8") as f:
    LONG_DESCRIPTION = f.read()

setup(
    name="abb",
    packages=find_packages(exclude=["tests"]),
    package_dir={"abb": "abb"},
    author="Alexander L. Hayes (hayesall)",
    author_email="alexander@batflyer.net",
    version=__version__,
    description="abb: Awesome Bibliography Builder.",
    long_description=LONG_DESCRIPTION,
    url="https://hayesall.com",
    download_url="https://github.com/hayesall/awesome_bib_builder",
    license="MIT",
    zip_safe=False,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    keywords="bibliography bibtex awesome",
    install_requires=["liquidpy", "bibtexparser"],
    extras_require={
        "tests": ["coverage", "pytest"],
    },
)
