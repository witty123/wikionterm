import click
import urllib2
import json

@click.command()
@click.argument('log', type=click.File('a+'), help="URL log file")
@click.argument('search_term', help="Word you want to search wkipedia for")
def search(search_term, out):
    jsonres =  urllib2.urlopen("https://en.wikipedia.org/w/api.php?action=opensearch&search="+ search_term +"&limit=1&namespace=0&format=json").read()
    jsonres = str(jsonres)
    click.echo(jsonres)
    jsonres = jsonres.split(",")
    url = jsonres[len(jsonres)-1]
    url = url.replace("[","")
    url = url.replace("]","")
    url = url.replace("\"","")
    url = str(url)
    if url != "":
        click.echo(url+'\n')
        log.write(url+'\n')
    else:
        click.echo("No wiki link found!")
