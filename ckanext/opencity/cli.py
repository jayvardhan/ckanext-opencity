import click


@click.group(short_help="opencity CLI.")
def opencity():
    """opencity CLI.
    """
    pass


@opencity.command()
@click.argument("name", default="opencity")
def command(name):
    """Docs.
    """
    click.echo("Hello, {name}!".format(name=name))


def get_commands():
    return [opencity]
