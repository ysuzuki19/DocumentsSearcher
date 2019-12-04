# -*- coding: utf-8 -*-
import json

def get_articles(path):
    data = []
    with open(path) as f:
        json_str = ''
        for line in f:
            json_str += line
            if line == '}{\n':
                json_str = json_str.replace('\n', '')
                json_str = json_str.replace('}{', '}')
                data.append(json.loads(json_str))
                json_str = '{'
        data.append(json.loads(json_str))
    return data
