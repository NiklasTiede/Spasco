import pathlib

import setuptools

from spasco import __src_url__
from spasco import __title__
from spasco import __version__

setuptools.setup(
    name=__title__,
    version=__version__,
    author="Niklas Tiede",
    author_email="niklastiede2@gmail.com",
    description="command line tool for replacing/removing whitespaces or other patterns of file- and directory names.",
    long_description=pathlib.Path("README.md").read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    url=__src_url__,
    license="MIT",
    packages=setuptools.find_packages(),
    extras_require={
        "dev": [
            "pytest",
        ],
    },
    platforms="linux",
    python_requires=">=3.5",
    entry_points={"console_scripts": ["spasco = spasco.main:run_main"]},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: System :: Filesystems",
        "Topic :: Utilities",
    ],
)
