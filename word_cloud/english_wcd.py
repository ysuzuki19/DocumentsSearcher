import sys
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from bs4 import BeautifulSoup
import requests
import MeCab as mc

from pdf2text import pdf2text

def create_wordcloud(wordlist):
	fontpath = "/System/Library/Fonts/HelveticaNeue.ttc"
	stop_words = [ 'am', 'is', 'of', 'and', 'the', 'to', 'it', 'for', 'in', 'as', 'or', 'are', 'be', 'this', 'that', 'will', 'there', 'was']
	wordcloud = WordCloud(background_color="black",font_path=fontpath, width=900, height=500, stopwords=set(stop_words)).generate(wordlist)
	plt.figure(figsize=(8,5))
	plt.imshow(wordcloud)
	plt.axis("off")
	plt.show()

def main():
	text_in_pdf = pdf2text(sys.argv[1])
	text_in_pdf = text_in_pdf.replace('-\n', '')
	text_in_pdf = text_in_pdf.replace('\n', ' ')
	print(text_in_pdf)
	create_wordcloud(text_in_pdf)

if __name__ == '__main__':
	main()
