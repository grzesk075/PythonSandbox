# PythonSandbox
Space for Python learning and experiments.

### Packages
After Python installation on windows,
path for python.exe and Python Package Manager pip.exe
should be manually added to PATH system variable.
To install module e.g. pytest type in shell
> pip install -U pytest

On Linux pip should be installed manually (e.g. for Mint distribution)
> sudo apt-get install python3-pip

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
