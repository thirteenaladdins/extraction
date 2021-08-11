# generate RX template
# create a table
# make it different for williams haulage. 

# use pandas to create a new file

import pandas as pd
from Generation.generate_file import generate_file_name
# from collections import namedtuple

# create named tuple

# create a CSV file with headers?
# add this as the 
# TODO add blank cells, add title row to CSV
# add extra command lin input to add more information to the file

# RX = namedtuple('RX', '''reference vehicle consignor consignee 
# warehouse aca cpc tariff description quantity2 value gross net header_packages
# quantity pkg type marks ai_code ai_code_2 ai_text ai_text_2
# document_code document_status ref document_code_2 document_status_2 ref_2
# document_code_3 document_status_3 ref_3 spoff prev_doc_code prev_doc_type prev_doc_ref
# '''
# )


headers_list = ['reference', 'vehicle', 'consignor', 'consignee', 
'warehouse', 'aca', 'cpc', 'tariff', 'description', 'quantity2', 'value', 'gross', 'net', 'header_packages',
'quantity', 'pkg_type', 'marks', 'ai_code', 'ai_code_2', 'ai_text', 'ai_text_2',
'document_code', 'document_status', 'ref', 'document_code_2', 'document_status_2', 'ref_2',
'document_code_3', 'document_status_3', 'ref_3', 'spoff', 'prev_doc_code', 'prev_doc_type', 'prev_doc_ref']

# Start here

item_information_list = [
        '', '', '', '', '', '', '1000001', '', '', '',
        '', '', '', '', '', 'PK', 'PART OF PACKAGES', 'LIC99', '', '',
        'N821', 'AC', '', '', '', '', '', '', '', '', 
        '', 'Z', '380', 'INV', 
    ]

# could create a class here? Not sure why just want to use one

# TODO create CSV file with this column headings

# the list items I pass in are the dictionary - 
# pass those into the RX template, once for each 
def generate_RX_template(list_items):
    file_name = generate_file_name()
    df = pd.DataFrame(list_items)
    
    # df.index = df.index + 1

    # TODO - Export and Save
    df.to_csv(f'../Export-RX-{file_name}.csv', header=headers_list, index=False)

    return df

# for the list of items, add 28 blank spaces 
    # print(list_items)
    # 34 column headers
    
    # TODO specific to Williams Haulage - this works for only a single item - I need to run this once for 
    # each row of items - do we do this once per item?
    # Does this go here? 
    # I should create the data frame once I have all the info right?
    
    # df = pd.DataFrame(data=[RX('reference', 'vehicle', list_items['short_code'], '', '', '', '1000001', list_items['tariff'], 
    # 'description', list_items['trailers'], list_items['value'], list_items['weight'], list_items['weight'], '', list_items['trailers'], 
    # 'PK', 'PART OF PACKAGES', 'LIC99', '', '' , '', 
    # 'N821', 'AC', 'LRN', '', '' , '', 
    # '', '', '', '', '', 
    # 'Z', '380', 'Invoice_number'

    # )])

    # TODO loop over the list and convert it into this and add CSV
    # df = pd.DataFrame(data=[RX('reference', 'vehicle', list_items[0], '', '', '', '1000001', list_items[1], 
    # 'description', list_items[2], list_items[4], list_items[3], list_items[3], '', list_items[2], 
    # 'PK', 'PART OF PACKAGES', 'LIC99', '', '' , '', 
    # 'N821', 'AC', 'LRN', '', '' , '', 
    # '', '', '', '', '', 
    # 'Z', '380', 'Invoice_Number'

    # )])


# generate_RX_template(RX)
