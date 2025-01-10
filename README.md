# python-playground

## Introduction

* Playground for python

## Skills

* python 3.13
* FastAPI

## Poetry

### API Documentations

```
http://localhost:8000/docs
```

### How to set poetry virtual environment settings in project

```
brew install python@3.13
poetry config virtualenvs.in-project true
poetry env remove python
# (poetry version 2.0 higher) virtualenvs
poetry env use 3.13
# (poetry version 2.0 lower) virtualenvs
poetry shell
poetry install -vvv
```

### CLI for poetry settings

```bash
poetry install -vvv
poetry update -vvv
poetry shell
poetry lock --no-update

# export the file "requirement.txt"
poetry export -f requirements.txt --output requirements.txt --without-hashes
```

### Intellij settings

* Edit run/debug configurations

```
# run script
/opt/homebrew/bin/uvicorn src.main:app --reload --log-level debug
```

* Auto import the poetry librarires

```
right-click .venv in the project tree -> Mark Directory as ... -> Excluded
```
