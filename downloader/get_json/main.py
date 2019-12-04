import arxiv
import json

result = arxiv.query(query="cs", max_chunk_results=10, iterative=True)
with open('../articles_list.json', 'w') as article:
    for paper in result():
        print(paper)
        json.dump(paper, article, indent=2)
