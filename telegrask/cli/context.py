from os import path, getcwd


class ctx(object):
    app_root = getcwd()
    venv_dir = ".venv"
    templates_dir = path.join(path.dirname(path.realpath(__file__)), "templates")
