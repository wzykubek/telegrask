# Contributing

## Setup

```shell
$ git clone https://github.com/samedamci/telegrask
$ cd telegrask
$ python -m pip install poetry
$ poetry install
```

## Build

```shell
$ poetry build
```

## Before Push

Check if following command runs without errros:

```shell
$ poetry run flake8
```

After all format code with black:

```shell
$ poetry run black .
```

These steps will help your code to pass all CI checks after Pull Request.
