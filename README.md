[![Python application test with Github Actions](https://github.com/leandrohvieira/python-devops/actions/workflows/devops.yml/badge.svg)](https://github.com/leandrohvieira/python-devops/actions/workflows/devops.yml)


# python-devops
This is a new prepository for Python DevOps.


1. Create a Python Virtual Enviroment 'python3 -m venv ~/.venv' or 'virtualenv ~/.venv'
2. Activate Virtual Enviroment 'source ~/.venv/bin/activate'
3. Create empty files: 'Makefile', 'requirements.txt', main.py', 'Dockerfile', 'mylib/__init__.py'
4. Populate 'Makefile': 'make install', 'make format', 'make all'
5. Stup Continuous Integration, i.e. check code for issues like lint error
6.  Build cli using Python Fire library './cli-fire.py --help' to test logic 
