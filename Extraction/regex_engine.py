import fitz
import re
import pprint
# from misc_functions import generate_file
from Processing.preprocessor_templates import get_definitions
from Processing.match_definition import get_match_definition
from Extraction.mann_hummel import extract_mann

print(fitz.__doc__)

# add flags as a separate argument later.

def regex_compiler(string):
    compile_regex = re.compile(string, flags=re.DOTALL)
    # compile_regex = re.compile(string)
    return compile_regex


# Add re.DOTALL in the sub function
# the re.DOTALL should be selected by choice 

def remove_data(regex_pattern, repl, string):
    page_after_filter = re.sub(regex_pattern, repl, string, flags=re.DOTALL)
    return page_after_filter


# right now all I'm doing is removing data -
# pass functions in to map to data -
# TODO improve functionality of this function

def regex_preprocessor(regex_definitions, page_text):
    # print(regex_definitions)
    for regex_def in regex_definitions:
        page_text = remove_data(regex_def, "", page_text)

    return page_text


# replace items here...
# pre processor...?
def define_replace(string):
    pass


def find_matches(item_to_search, text):
    all_matches = re.findall(item_to_search, text)
    return all_matches

def is_number(x):
    try:
        # only integers and float converts safely
        num = float(x)
        return True
    except ValueError as e: # not convertable to float
        return False

def remove_commas(list_of_items):
    values_list = []

    # replace commas with blank
    if isinstance(list_of_items, list):
        for item in list_of_items:
            x = item.replace(',', '')
            values_list.append(x)
        
        return values_list
    elif isinstance(list_of_items, str):
        x = list_of_items.replace(',' '')
        return x
    

# TODO take into account 
# Could check the actual invoice the name instead of the input file
# let the logic in the functions decide instead


def extract_data(path_to_pdf, dropdown_value):

    
    pdf_document = fitz.open(path_to_pdf)
    regex_definitions = get_definitions(dropdown_value)

    # is this overly complicated?
    # TODO come back and refactor
    item_to_match = get_match_definition(dropdown_value)

    full_text = ''
    for page in pdf_document:
        # Text vs block etc
        page_text = page.get_text("text")
        # print(page_text)

        # get the relevant process here for preprocessing the pages
        

        # if the page needs to be run through the preprocessor
        if regex_definitions:

            # # TODO this works - preprocessing the data before extracting information
            processed_page = regex_preprocessor(regex_definitions, page_text)
            # print(processed_page)
            full_text += processed_page
            pass
      
        else:
            full_text += page_text

    

    if (dropdown_value == 'Mann + Hummel'):
        item_to_search = regex_compiler(item_to_match)
        
        # TODO not sure if this part matters
        split_text = full_text.split('\n')
        
        full_text_spaces = ' '.join(split_text).strip()
        all_matches = find_matches(item_to_search, full_text_spaces)

        # for item in all_matches:
        #     print(item)

        
        # for item in all_matches:
        #     # pprint.pprint(repr(item.split()))
        #     print(repr(item.split()[-1]))

        matches = extract_mann(True, all_matches)
        
        return matches

        # for each item
        # for item in all_matches:
        #     print(item)




# other invoices etc let's just grab the trailers, weight and total charge

    
    
