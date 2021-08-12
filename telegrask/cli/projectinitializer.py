from .context import ctx
import venv
from os import mkdir, path


class ProjectInitializer:
    def __init__(
        self,
        project_name: str,
        create_venv: bool = True,
        include_gitignore: bool = True,
    ) -> None:
        if create_venv:
            self.create_venv()
        if include_gitignore:
            self.add_gitignore()
        self.create_package(project_name)

    @staticmethod
    def create_venv() -> None:
        venv.create(
            path.join(ctx.app_root, ctx.venv_dir, "venv"),
            system_site_packages=True,
            with_pip=True,
        )

    @staticmethod
    def read_template(template_name: str) -> str:
        with open(path.join(ctx.templates_dir, template_name), "r") as f:
            return f.read()

    @staticmethod
    def write_file(file_path: str, content: str) -> None:
        with open(file_path, "w+") as f:
            f.write(content)

    def add_gitignore(self) -> None:
        template = self.read_template(".gitignore")
        self.write_file(
            path.join(ctx.app_root, ".gitignore"),
            template.replace("__VENV_DIR", ctx.venv_dir),
        )

    def create_package(self, package_name: str) -> None:
        mkdir(path.join(ctx.app_root, package_name))
        package_dir = path.join(ctx.app_root, package_name)
        for template in ["__init__.py", "config.py", "commands.py"]:
            self.write_file(
                path.join(package_dir, template), self.read_template(template)
            )
