from codecs import open
from os import path
from setuptools import setup, find_packages

_VERSION = '0.1'

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="py_dotenv",
    version=_VERSION,

    description="Read dotenv file",
    long_description=long_description,

    url="https://github.com/aongko/py_dotenv",

    author="Andrew Ongko",
    author_email="Andrew.Ongko@gmail.com",

    keywords="python env",

    license="MIT License",

    classifiers=[
        # "Development Status :: 3 - Alpha",
        "Development Status :: 4 - Beta",
        # "Development Status :: 5 - Production/Stable",
        # "Development Status :: 6 - Mature",
        # "Development Status :: 7 - Inactive",

        "Intended Audience :: Developers",

        "License :: OSI Approved :: MIT License",

        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        ],

    packages=find_packages(exclude=['contrib', 'docs', 'tests'])
)
