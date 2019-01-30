# PythonSandbox
Space for Python learning and experiments.

### Packages
After Python installation on windows,
path for python.exe and Python Package Manager pip.exe
should be manually added to PATH system variable.
To install module e.g. pytest (newest) type in shell
> pip install -U pytest

Library root for installed packages is *site-packages* folder in Python environment.

On Linux pip should be installed manually (e.g. for Mint distribution)
> sudo apt-get install python3-pip

To make requirements.txt file type
> pip freeze > requirements.txt

To update your environment with requirements type
> pip install -r requirements.txt

To upgrade pytest package to newest version type
> pip install --upgrade pytest

Packages can be searched on https://pypi.org .

You can also save wheel archives with packages, when you have wheel package installed.
> pip wheel -r requirements.txt

### Virtual Environments
This concept allows to have separate folders with links to particular
Python version and physical space for packages in expected versions.
To create folder sandbox-env with virtual environment
you need to install and use venv program.
> sudo apt-get install python3-venv

> python3 -m venv sandbox-env

To activate environment in shell use the command below
> source sandbox-env/bin/activate

Also running ./python link from sandbox-env/bin runs Python with
site-packages from sandbox-env virtual environment.
You can verify this in Python shell by
> import sys; sys.path

Logging library used for logging is conceptually similar to java log4j.

There are two most popular unit tests libraries: built-in unittest and external and more powerful pytest.
