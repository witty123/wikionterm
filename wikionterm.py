import click
import urllib2
import json

@click.command()
@click.argument('search_term')
def search(search_term):
	 jsonres =  urllib2.urlopen("https://en.wikipedia.org/w/api.php?action=opensearch&search="+ search_term +"&limit=1&namespace=0&format=json").read()
	 jsonres = str(jsonres)
	 jsonres = jsonres.split(",")
	 #beg = jsonres.find("http")
	 url = jsonres[3]
	 click.echo(str(url))
	 

