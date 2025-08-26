import click
from pathlib import Path
from templates import README_CODE, MAIN_CODE, GITIGNORE_CODE

@click.group()
def main():
    """Py-Boiler: Generate boilerplate Python apps."""
    pass


@main.group()
def new():
    """Scaffold new boilerplate projects."""
    pass


@new.command("hello-world")
def hello_world():
    """Generate a Hello World app.py file."""
    target_files = [
        "README.md", "app.py", ".gitignore", "__init__.py"
    ]
    for file in target_files:
        target_file = Path("templates/"+file)
        
        if target_file.exists():
            click.echo(f"⚠️  {file} already exists, not overwriting.")
        else:
            match file:
                case "README.md":
                    app_code = README_CODE
                case "app.py":
                    app_code = MAIN_CODE
                case ".gitignore":
                    app_code = GITIGNORE_CODE
                case _:
                    continue
            target_file.write_text(app_code)
            click.echo("✅ Created {file} with Hello World template.")


if __name__ == "__main__":
    main()
