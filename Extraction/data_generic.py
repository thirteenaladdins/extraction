# from invoice2data import extract_data
# from invoice2data.extract.loader import read_templates

# import pprint
# import re
# import pdfminer

# import pandas as pd
# import tabula
import json
import fitz

# from misc_functions import generate_file

# fix some functions - rename functions - add RX template to separate file
# what I could is start with the first box, program the coorindates in 
# move the box down a set amount for each item, start at the top of each page and then move it down

# this is a specific solution for this invoice 

# separate each set of coordinates into items

item_list = []
full_list = []


def extract_coordinates(path_to_pdf):
    doc = fitz.open(path_to_pdf)
    number_pages = doc.page_count
    # page = doc.load_page(1)

    with open('templates/jaguar_template_2.json') as f:
        data = json.load(f)

    # collect the group into an item
    # for each page get these elements, group into sets of six

    ''' For each page of the document run the following code'''
    # for n in range(1, number_pages):
    count = 0
    for page in doc:
        if count < 1:
            # skip the first page
            count += 1
        else: 
            # page = doc.load_page(n)
            # print(n)
            count += 1
            for i in range(24):
                item = (data[i]['x1'], data[i]['y1'], data[i]['x2'], data[i]['y2'])
                
                item_1_text = page.get_text('text', clip=item)
                item_list.append(item_1_text.strip())

            # print(item_list)
            # print('\n')

    remove_empty = [string for string in item_list if string != ""]
    split_size = 6
    split_list = [remove_empty[x:x+split_size] for x in range(0, len(remove_empty), split_size)]

    final_list = []
    # put it in the order necessary for RX
    order = [2, 1, 0, 5, 4, 3]
    for ls in split_list:
        my_list = [ls[i] for i in order]
        final_list.append(my_list)
        print(my_list)
        
    # rearrange

    # generate_file(split_list)
    return final_list

# generate RX worksheet