from lxml import html
import requests

page = requests.get('')
tree = html.fromstring(page.content)
