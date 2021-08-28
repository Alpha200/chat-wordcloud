import click

from telegram import generate_telegram_wordcloud
from threema import generate_threema_wordcloud


@click.group()
def cli():
    pass


@cli.command()
@click.argument('filename', type=click.File('r'))
def telegram(filename):
    generate_telegram_wordcloud(filename)


@cli.command()
@click.argument('filename', type=click.File('r'))
def threema(filename):
    generate_threema_wordcloud(filename)


if __name__ == '__main__':
    cli()
