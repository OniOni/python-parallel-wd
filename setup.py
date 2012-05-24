import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "python-wd-parallel",
    packages = ['wd'],
    version = "0.1.0",
    author = "Mathieu Sabourin",
    author_email = "mathieu.c.sabourin@gmail.com",
    maintainer = "Mathieu Sabourin",
    maintainer_email = "mathieu.c.sabourin@gmail.com",
    description = ("python-wd-parallel lets you easilly run your test in multiple borwsers."),
    keywords = " Testing, Selenium",
    url = "https://github.com/OniOni",
    download_url = "https://github.com/OniOni/python-parallel-wd",
    install_requires = ["selenium>=2.21.3"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: No Input/Output (Daemon)",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Quality Assurance",
        "Topic :: Software Development :: Testing"
        ]
)


