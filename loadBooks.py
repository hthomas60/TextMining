import pickle
import requests
import codecs

def loadbooks():
	"""
	Loads books from gutenberg.org. Book id has to be manualy changed each book.
	"""
	downloaded_book = requests.get('http://www.gutenberg.org/ebooks/1522.txt.utf-8').text
	return downloaded_book

def savebook(book_text, filename):
	"""
	Saves a the text of a book into a file. 
	"""
	f = open(filename, 'wb')
	pickle.dump(book_text, f)
	f.close()

def opensavedbook(file):
	"""
	Opens a file that is saved on the computer
	"""
	input_file = open(file, 'rb')
	opened_text = pickle.load(input_file)
	return opened_text



