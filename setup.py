import os
from os import path

import setuptools

this_directory = path.abspath(path.dirname(__file__))


def read_file(filename):
    with open(path.join(this_directory, filename), encoding='utf-8') as f:
        long_description = f.read()
    return long_description


def read_requirements(filename):
    return [line.strip() for line in read_file(filename).splitlines() if not line.startswith('#')]


setuptools.setup(
    name="GitDatabase",
    version=os.environ.get('PACKAGE_VERSION', '0.0.1'),
    author="Han",
    author_email="mirrorhanyu@gmail.com",
    maintainer="Han",
    maintainer_email="mirrorhanyu@gmail.com",
    description="use git repository as database",
    long_description=read_file('README.md'),
    long_description_content_type="text/markdown",
    url="https://github.com/mirrorhanyu/GitDatabase",
    install_requires=read_requirements('requirements.txt'),
    packages=['gitdatabase'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)