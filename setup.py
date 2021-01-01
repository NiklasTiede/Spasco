import pathlib

import setuptools

__version__ = "0.1.0"
__author__ = 'Niklas Tiede'
__author_email__ = 'niklastiede2@gmail.com'
__src_url__ = 'https://github.com/NiklasTiede/spasco'


setuptools.setup(
    name="spasco",
    version=__version__,
    author=__author__,
    author_email=__author_email__,
    description="command line tool for replacing spaces of file-/dir-names by underscores",
    long_description=pathlib.Path("README.md").read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    url=__src_url__,
    license="MIT",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),  # production install:  pip install .
    extras_require={
        'dev': [
            'pytest',
            # 'pytest-pep8',
            # 'pytest-cov',
        ],
    },
    # extras_require=[
    #         'pytest',
    #         # 'pytest-pep8',
    #         # 'pytest-cov',
    #         # 'yapf',
    #         # 'isort',
    #         # 'sphinx',
    # ],
    platforms="linux",
    python_requires=">=3.5",
    # entry_points={"console_scripts": ["spasco = spasco.py:run_main"]},
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
