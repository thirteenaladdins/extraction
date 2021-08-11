import pandas as pd
import re
import fitz
import sys

# from Generation.generate_file import generate_file
from Extraction.electro import extract_electro
from Extraction.regex_engine import extract_data
from Extraction.data_generic import extract_coordinates
from Extraction.williams2 import extract_williams
from Extraction.siemens import extract_siemens

# this is basically the extract data function from before...
# TODO think I'm performing the same function twice - fix this


def execute_function(arg, company_name):
    if company_name == 'Mann + Hummel':
        extracted_data = extract_data(sys.argv[1], 'Mann + Hummel')
        return extracted_data
    
        ''' 
        Williams extraction also accepts multiple files...
        they should all really accept multiple files 
        a funciton that works for one should work for all. 
        '''
    elif company_name == "Williams":
        extracted_data = extract_williams(arg)
        return extracted_data
        
    elif company_name == 'Electrolux':
        # TODO - electrolux - 
        pass
        # extracted_data = extract_electro(sys.argv[1])
        # return extracted_data

    elif company_name == 'Jaguar':
        # jaguar land rover T1 here
        extracted_data = extract_coordinates(arg)            
        return extracted_data

    elif company_name == 'Siemens':
        extracted_data = extract_siemens(arg)
        return extracted_data

        pass

    else:
        print('Testing')


def check_company(path_to_pdf):
    # TODO These are all case sensitive... could cause problems

    mann_search = r"MANN \+ HUMMEL"
    IWT_search = r"IWT Deeside Ltd"
    IFOR_search = r"Ifor Williams"
    Elec_search = r'ELECTROLUX'
    Jag_search = r'JAGUAR LAND ROVER LTD'
    Siemens_search = r'Siemens'

    doc = fitz.open(path_to_pdf)
    first_page = doc.load_page(0)

    page_text = first_page.get_text('text')

    # Works well - could break with the new system
    if re.search(mann_search, page_text):
        print('Match Found - Mann + Hummel')
        return 'Mann + Hummel'

    if re.search(IWT_search, page_text):
        print('Match Found - IWT Deeside')
        return 'Williams'

    if re.search(IFOR_search, page_text):
        print('Match Found - IFOR Williams')
        return 'Williams'
    
    if re.search(Elec_search, page_text):
        print('Match Found - Electrolux')
        return 'Electrolux'
    
    # Works well enough
    if re.search(Jag_search, page_text):
        print('Match Found - Jaguar Land Rover')
        return 'Jaguar'
    
    # Could do with a little improvement - very rudimentary at the moment
    if re.search(Siemens_search, page_text):
        print('Match Found - Siemens')
        return 'Siemens'

    else:
        return 'Generic'


def count_exporters(exporter_list):
    length = len(exporter_list)

    if length == 1:
        return False
    elif length > 1:
        list_of = []
        for item in exporter_list:
            if 'SI-' in item:
                print('SI- Exists')
                if 'IFOR' not in list_of:
                    list_of.append('IFOR')                

            elif 'INV' in item:
                print('INV Exists')
                if 'DEESIDE' not in list_of:
                    list_of.append('DEESIDE')
            else:
                pass

        # if they both exist in the same list then the list will be of length 2
        print(list_of)
        if len(list_of) > 1:
            return True
        else:
            return False

