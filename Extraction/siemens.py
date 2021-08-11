import fitz 
import re
# from misc_functions import generate_file
import sys
import pprint

# TODO fix the things like 

# from pdfminer.high_level import extract_text
# from sorted import SortedCollection

# doc = 'C:/Users/Mo_Am/Desktop/480113 GAI.pdf'
# doc = 'C:/Users/Mo_Am/Documents/PSL - Andromeda/electron-react/python-backend/480113 GAI.pdf'

# from operator import itemgetter
# from itertools import groupby

# fitz removes any protection from file, if it's password protected 

# how am I supposed to string all these scripts together into one cohesive program?

# TODO still needs to be fixed
# TODO seems as though my logic doesn't work for every invoice. This item is split between two 


def str_list(x): 
	return str(x)

# the methods I'm using to extract the data is naive
def item_sorter(item):
	try:
		value = item[-1]
		description = item[-5]
		quantity = item[-4]
		return [description, quantity, value]
	except:
		pass
	
''' The amount of times I transform the types here is ridiculous. Is there a simpler way? 
	 A method I have used before is locating the index of an element and gettinig all that precedes it
'''

def extract_siemens(path_to_pdf):
	doc = fitz.open(path_to_pdf)
	# doc.authenticate()

	# create a list comprehension, that appends page data to the list
	pages = [ doc[i] for i in range( doc.pageCount ) ]
	
	full_list = []
	tariff_list = []
	gross = ''
	net = ''

	for page in pages:
		text = page.get_text('text')
		# pprint.pprint(text)
		
		text_split = text.split('\n')
		# print(text_split)
		item_list = []

		for item in text_split:
			if 'Material' in item:
				# find material - the preceding values are for this item, the following HS Code 
				# also belongs to this item 
				# print(item)
				item_index = text_split.index(item)
				# make sure we're getting the right information
				value = text_split[item_index - 1]
				quantity = text_split[item_index - 4]
				description = text_split[item_index - 5]
				
				item_list = [description, quantity, gross, net, value] 
				full_list.append(item_list)

			if 'HS Code' in item:
				item = item.replace('HS Code: ', '')
				tariff_list.append([item])
	
	# combines two lists together - well nested lists in this case
	full_list = [i + j for i, j in zip(tariff_list, full_list)]
	return full_list

