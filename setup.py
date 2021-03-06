#
# Access-Log file analysis.
# (c) ISC Clemenz & Weinbrecht GmbH 2018
#

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cmds",
    version="0.0.1",
    author="ISC Clemenz & Weinbrecht GmbH",
    author_email="info@isc-software.de",
    description="Some simple commands",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bernd-clemenz/cmds",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    install_requires=(
        "argparse",
        "requests",
        "paramiko"
    ),
)