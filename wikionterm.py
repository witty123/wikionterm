import click
import urllib2
import urllib
import json

@click.command()
@click.option('--log', type=click.File('a'), help="URL log file")
@click.option('--search_term', help="Word you want to search wkipedia for")
def search(search_term,log):
    if log == None:
        click.echo("Enter the log file")
        log = raw_input()
        log = open(log, 'a')
    if search_term == None:
        click.echo("Enter the search term")
        search_term = raw_input()
    jsonres =  urllib2.urlopen("https://en.wikipedia.org/w/api.php?action=opensearch&search="+ search_term +"&limit=1&namespace=0&format=json").read()
    jsonres = str(jsonres)
    # click.echo(jsonres)
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
