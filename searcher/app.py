from flask import Flask, render_template, request
from hamlish_jinja import HamlishExtension
from werkzeug import ImmutableDict
#from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

json = {
	"id": "http://arxiv.org/abs/1805.08355v1",
	"guidislink": True,
	"updated": "2018-05-22T02:12:33Z",
	"updated_parsed": [
		2018,
		5,
		22,
		2,
		12,
		33,
		1,
		142,
		0
	],
	"published": "2018-05-22T02:12:33Z",
	"published_parsed": [
		2018,
		5,
		22,
		2,
		12,
		33,
		1,
		142,
		0
	],
	"title": "Opening the black box of deep learning",
	"title_detail": {
		"type": "text/plain",
		"language": None,
		"base": "http://export.arxiv.org/api/query?search_query=deep+learning&id_list=&start=0&max_results=10&sortBy=relevance&sortOrder=descending",
		"value": "Opening the black box of deep learning"
	},
	"summary": "The great success of deep learning shows that its technology contains\nprofound truth, and understanding its internal mechanism not only has important\nimplications for the development of its technology and effective application in\nvarious fields, but also provides meaningful insights into the understanding of\nhuman brain mechanism. At present, most of the theoretical research on deep\nlearning is based on mathematics. This dissertation proposes that the neural\nnetwork of deep learning is a physical system, examines deep learning from\nthree different perspectives: microscopic, macroscopic, and physical world\nviews, answers multiple theoretical puzzles in deep learning by using physics\nprinciples. For example, from the perspective of quantum mechanics and\nstatistical physics, this dissertation presents the calculation methods for\nconvolution calculation, pooling, normalization, and Restricted Boltzmann\nMachine, as well as the selection of cost functions, explains why deep learning\nmust be deep, what characteristics are learned in deep learning, why\nConvolutional Neural Networks do not have to be trained layer by layer, and the\nlimitations of deep learning, etc., and proposes the theoretical direction and\nbasis for the further development of deep learning now and in the future. The\nbrilliance of physics flashes in deep learning, we try to establish the deep\nlearning technology based on the scientific theory of physics.",
	"summary_detail": {
		"type": "text/plain",
		"language": None,
		"base": "http://export.arxiv.org/api/query?search_query=deep+learning&id_list=&start=0&max_results=10&sortBy=relevance&sortOrder=descending",
		"value": "The great success of deep learning shows that its technology contains\nprofound truth, and understanding its internal mechanism not only has important\nimplications for the development of its technology and effective application in\nvarious fields, but also provides meaningful insights into the understanding of\nhuman brain mechanism. At present, most of the theoretical research on deep\nlearning is based on mathematics. This dissertation proposes that the neural\nnetwork of deep learning is a physical system, examines deep learning from\nthree different perspectives: microscopic, macroscopic, and physical world\nviews, answers multiple theoretical puzzles in deep learning by using physics\nprinciples. For example, from the perspective of quantum mechanics and\nstatistical physics, this dissertation presents the calculation methods for\nconvolution calculation, pooling, normalization, and Restricted Boltzmann\nMachine, as well as the selection of cost functions, explains why deep learning\nmust be deep, what characteristics are learned in deep learning, why\nConvolutional Neural Networks do not have to be trained layer by layer, and the\nlimitations of deep learning, etc., and proposes the theoretical direction and\nbasis for the further development of deep learning now and in the future. The\nbrilliance of physics flashes in deep learning, we try to establish the deep\nlearning technology based on the scientific theory of physics."
	},
	"authors": [
		"Dian Lei",
		"Xiaoxiao Chen",
		"Jianfei Zhao"
	],
	"author_detail": {
		"name": "Jianfei Zhao"
	},
	"author": "Jianfei Zhao",
	"links": [
		{
			"href": "http://arxiv.org/abs/1805.08355v1",
			"rel": "alternate",
			"type": "text/html"
		},
		{
			"title": "pdf",
			"href": "http://arxiv.org/pdf/1805.08355v1",
			"rel": "related",
			"type": "application/pdf"
		}
	],
	"arxiv_primary_category": {
		"term": "cs.LG",
		"scheme": "http://arxiv.org/schemas/atom"
	},
	"tags": [
		{
			"term": "cs.LG",
			"scheme": "http://arxiv.org/schemas/atom",
			"label": None
		},
		{
			"term": "stat.ML",
			"scheme": "http://arxiv.org/schemas/atom",
			"label": None
		}
	],
	"pdf_url": "http://arxiv.org/pdf/1805.08355v1",
	"affiliation": "None",
	"arxiv_url": "http://arxiv.org/abs/1805.08355v1",
	"arxiv_comment": None,
	"journal_reference": None,
	"doi": None
}

@app.route('/')
def start():
	return render_template('form.html')

@app.route('/form')
def form( ):
	return render_template('form.html')

@app.route('/search', methods=['POST', 'GET'])
def search():
	if request.method == 'POST':
		print(request)
		result = request.form
		print(request)
		return render_template('json_view.html',search_words=request.form['Name'], results_json=json)
#		return render_template('json_view.html',search_words=request.form['Name'])
#		return render_template('search_result.html', search_words=request.form['Name'])

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)
