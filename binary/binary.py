import os
import ConfigParser

import click
import requests


repos = '/api/repositories'
all_repos = '[?type=repositoryType (local|remote)]'
location = 'NONE'
art_name = 'NONE'
img = 'NONE'

default_config_path = '~/.artifactory.cfg'
config_path = os.path.expanduser(default_config_path)

config = ConfigParser.ConfigParser()
config.read(config_path)
username = config.get('artifactory', 'username')
password = config.get('artifactory', 'password')
url = config.get('artifactory', 'url')


def cmd_all():
    r = requests.get(url + repos, auth=(username, password), params=all_repos)
    print(r.text)


def cmd_upload():
    with open(art_name, 'rb') as fh:
        r = requests.put(url + '/' + location + '/' + img, auth=(username, password), data=fh)
    print(r.content)


def cmd_dnld():
    r = requests.get(url + '/' + location + '/' + art_name, auth=(username, password), stream=True)
    with open(art_name, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                f.flush()
    return art_name


def cmd_del():
    r = requests.delete(url + '/' + location + '/' + art_name, auth=(username, password))
    print(r.text)


@click.group()
@click.version_option()
def cli():
    pass


@cli.command('all')
def cli_all():
    cmd_all()


@cli.command('upload')
@click.option('--repo', '-r', help='Name of repository')
@click.option('--image', '-i', help='Name of what you want to call you artifact')
@click.option('--file', '-f', help='File you want to upload')
def cli_upload(repo, image, binary):
    global location
    location = repo
    global art_name
    art_name = binary
    global img
    img = image
    art_name = binary
    cmd_upload()


@cli.command('download')
@click.option('--repo', '-r', help='Name of repository')
@click.option('--artifact', '-a', help='Name of artifact you want to download')
def cli_dnld(repo, artifact):
    global location
    location = repo
    global art_name
    art_name = art_name
    cmd_dnld()


@cli.command('delete')
@click.option('--repo', '-r', help='Name of repository')
@click.option('--artifact', '-a', help='Name of artifact you want to delete')
def cli_del(repo, artifact):
    global location
    location = repo
    global art_name
    art_name = art_name
    cmd_del()


if __name__ == '__main__':
    cli()
