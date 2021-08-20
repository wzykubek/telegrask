import argparse
from . import ProjectInitializer

parser = argparse.ArgumentParser(
    prog="telegrask", description="CLI for Telegrask framework.", allow_abbrev=False,
)
subparsers = parser.add_subparsers(dest="command", required=True)

parser_init = subparsers.add_parser("init", help="initialize project")
parser_init.add_argument(
    "name", metavar="NAME", type=str, nargs=1, help="name for package"
)
parser_init.add_argument(
    "--no-venv",
    dest="venv",
    action="store_false",
    help="do not create virtual environment",
)
parser_init.add_argument(
    "--no-gitignore",
    dest="gitignore",
    action="store_false",
    help="do not include .gitignore file",
)

args = parser.parse_args()
cmd = args.command


def main():
    if cmd == "init":
        ProjectInitializer(args.name[0], args.venv, args.gitignore)
