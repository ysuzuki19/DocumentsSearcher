# -*- coding: utf-8 -*-
import sys
import os
sys.path.append(os.path.join('..', 'module'))
from module.get_articles import get_articles
import arxiv
import json
import urllib

json_path = '../articles_list.json'
articles = get_articles(json_path)
data_number = 0
for article in articles:
    print(str(data_number) + ' : ' + article['title'].replace('\n', '').replace('  ', ' ') + ' is downloading ...')
    arxiv.download(article, "../articles")
    data_number+=1
