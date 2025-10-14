import os
import click
from pathlib import Path
from py_boiler.basic.templates import (
    README_CODE as BASIC_README_CODE,
    MAIN_CODE as BASIC_MAIN_CODE,
    GITIGNORE_CODE as BASIC_GITIGNORE_CODE,
)
from py_boiler.django.templates import (
    README_CODE as DJANGO_README_CODE,
    MAIN_CODE as DJANGO_MAIN_CODE,
    ASGI_CODE,
    WSGI_CODE,
    URLS_CODE,
    SETTINGS_CODE,
    API_ADMIN_CODE,
    API_APPS_CODE,
    API_MODELS_CODE,
    API_TESTS_CODE,
    API_URLS_CODE,
    API_VIEWS_CODE
)


@click.group()
def main():
    """Py-Boiler: Generate boilerplate Python apps."""
    pass


@main.group()
def new():
    """Scaffold new boilerplate projects."""
    pass


@new.command("basic")
@click.option("--name", help="Project Name")
def basic(name: str):
    if not name:
        name = "py_boiler 🚀"
    """Generate a Hello World app.py file."""
    target_files = ["README.md", "app.py", ".gitignore", "__init__.py"]
    print(name)
    for file in target_files:
        target_file = Path(f"./templates/{file}")

        if target_file.exists():
            click.echo(f"⚠️  {file} already exists, not overwriting.")
            continue

        match file:
            case "README.md":
                app_code = BASIC_README_CODE.format(project_name=name)
            case "app.py":
                app_code = BASIC_MAIN_CODE
            case ".gitignore":
                app_code = BASIC_GITIGNORE_CODE
            case _:
                app_code = ""
        try:
            target_file.write_text(app_code, encoding="utf-8")
        except UnicodeEncodeError:
            # Fallback for systems with encoding issues
            target_file.write_text(app_code, encoding="utf-8", errors="replace")
        click.echo(f"✅ Created {file} with Hello World template.")


@new.command("django")
@click.option("--name", help="Project Name")
def django(name: str):
    if not name:
        name = "py_boiler 🚀"
    target_files = ["README.md", "manage.py", ".gitignore"]
    project_folder = ["settings.py", "asgi.py", "wsgi.py", "urls.py", "__init__.py"]
    api_folder = [
        "admin.py",
        "apps.py",
        "__init__.py",
        "models.py",
        "tests.py",
        "urls.py",
        "views.py",
    ]
    for file in target_files:
        target_file = Path(f"./templates/{file}")

        if target_file.exists():
            click.echo(f"⚠️  {file} already exists, not overwriting.")
            continue

        match file:
            case "README.md":
                app_code = DJANGO_README_CODE.format(project_name=name)
            case "manage.py":
                app_code = DJANGO_MAIN_CODE
            case ".gitignore":
                app_code = BASIC_GITIGNORE_CODE
            case _:
                app_code = ""
        try:
            target_file.write_text(app_code, encoding="utf-8")
        except UnicodeEncodeError:
            # Fallback for systems with encoding issues
            target_file.write_text(app_code, encoding="utf-8", errors="replace")
        click.echo(f"✅ Created {file} with Django template.")

    target_folder = Path(f"./templates/{name}")
    if target_folder.exists():
        click.echo(f"⚠️ Folder {name} already exists")
    else:
        target_folder.mkdir()

    for file in project_folder:
        target_file = Path(f"./templates/{name}/{file}")

        if target_file.exists():
            click.echo(f"⚠️ {file} already exists, not overwriting.")
            continue

        match file:
            case "settings.py":
                app_code = SETTINGS_CODE
            case "urls.py":
                app_code = URLS_CODE
            case "asgi.py":
                app_code = ASGI_CODE
            case "wsgi.py":
                app_code = WSGI_CODE
            case _:
                app_code = ""
        try:
            target_file.write_text(app_code, encoding="utf-8")
        except UnicodeEncodeError:
            # Fallback for systems with encoding issues
            target_file.write_text(app_code, encoding="utf-8", errors="replace")
        click.echo(f"✅ Created {file} with Django template.")

    target_folder = Path("./templates/api")
    if target_folder.exists():
        click.echo(f"⚠️ Folder api already exists")
    else:
        target_folder.mkdir()

    for file in api_folder:
        target_file = Path(f"./templates/api/{file}")

        if target_file.exists():
            click.echo(f"⚠️ {file} already exists, not overwriting.")
            continue

        match file:
            case "admin.py":
                app_code = API_ADMIN_CODE
            case "apps.py":
                app_code = API_APPS_CODE
            case "models.py":
                app_code = API_MODELS_CODE
            case "tests.py":
                app_code = API_TESTS_CODE
            case "urls.py":
                app_code = API_URLS_CODE
            case "views.py":
                app_code = API_VIEWS_CODE
            case _:
                app_code = ""
        try:
            target_file.write_text(app_code, encoding="utf-8")
        except UnicodeEncodeError:
            # Fallback for systems with encoding issues
            target_file.write_text(app_code, encoding="utf-8", errors="replace")
        click.echo(f"✅ Created {file} with Django template.")


if __name__ == "__main__":
    main()
