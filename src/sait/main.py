import click


@click.group(invoke_without_command=True)
@click.version_option(package_name="siat")
def main():
    """Мой замечательный CLI-инструмент."""
    click.echo("Hey! You are using the Simple AI Tools!")


if __name__ == "__main__":
    main()
