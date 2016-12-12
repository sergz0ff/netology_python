import json
from pprint import pprint

with open('newsafr.json') as newsafr:
    afr = json.load(newsafr)

pprint(afr['rss']['channel'].items())

# pprint(afr)
