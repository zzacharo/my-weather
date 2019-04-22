import click
from flask.cli import with_appcontext
from myweatherapp.app import app
from myweatherapp.factory import db as db_

@click.group()
def cli():
    """:"""

@cli.group('db')
def db_cli():
    """myweather command line interface database management."""

@db_cli.command('init')
@with_appcontext
def db_init():
    """Initialize database."""
    try:
        db_.create_all()
        click.echo(click.style('Database successfully initialized.',
                               fg='green'))
    except Exception as e:
        click.echo(
            click.style(
                'Something went wrong while creating the database:\n{0}'
                .format(e), fg='red'), err=True)


@db_cli.command('drop')
@with_appcontext
def db_drop():
    """Drop database."""
    try:
        db_.drop_all()
        click.echo(click.style('Database successfully dropped.',
                               fg='green'))
    except Exception as e:
        click.echo(
            click.style(
                'Something went wrong while dropping the database:\n{0}'
                .format(e), fg='red'), err=True)
