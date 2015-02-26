import click
import requests

URL = '<INSERT URL OF UR ARTIFACTORY INSTANCE'
repos = URL+'/api/repositories'
all_repos = '[?type=repositoryType (local|remote)]'
location = 'None'
input = 'None'
img = 'None'

def cmd_all():
    r = requests.get(repos, params=all_repos)
    print(r.text)

def cmd_upload():
    with open(input, 'rb') as fh:
      r = requests.put(URL+location+'/'+img, data=fh)
    print(r.content)

def cmd_dnld():
    r = requests.get(URL+location+'/'+input, stream=True)
    with open(input, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                f.flush()
    return input

@click.group()
@click.version_option()
def cli():
    pass

@cli.command('all')
def cli_all():
    cmd_all()

@cli.command('upload')
@click.option('--repo','-r',help='Name of repository')
@click.option('--image','-i',help='Name of what you want to call you artifact')
@click.option('--file','-f',help='File you want to upload')
def cli_upload(repo, image, file):
    global location
    location = repo
    global input
    input = file
    global img
    img = image
    input = file
    cmd_upload()

@cli.command('download')
@click.option('--repo','-r',help='Name of repository')
@click.option('--artifact','-a',help='Name of artifact you want to download')
def cli_dnld(repo,artifact):
    global location
    location = repo
    global input
    input = artifact
    cmd_dnld()

if __name__ == '__main__':
   cli()
