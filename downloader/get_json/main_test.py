import arxiv
import json

result = arxiv.query(query="cs", max_chunk_results=10, iterative=True)
print('[')
for paper in result():
#		json_str = json.dumps(paper, indent=2)
		json_str = json.dumps(paper)
		print(json_str.replace('true', 'True').replace('null', 'None'))
		print(', ')
print(']')
