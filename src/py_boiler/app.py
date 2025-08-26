import click
from pathlib import Path
from templates import README_CODE, MAIN_CODE

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
        "README_TEMPLATE.md", "app_template.py"
    ]
    for file in target_files:
        target_file = Path("templates/"+file)
        
        if target_file.exists():
            click.echo(f"⚠️  {file} already exists, not overwriting.")
        else:
            match file:
                case "README_TEMPLATE.md":
                    app_code = README_CODE
                case "app_template.py":
                    app_code = MAIN_CODE
                case _:
                    raise ValueError("Borkn")
            target_file.write_text(app_code)
            click.echo("✅ Created {file} with Hello World template.")


if __name__ == "__main__":
    main()
