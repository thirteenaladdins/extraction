# all this spaghetti code
# this is the entry point. 

import argparse
import sys
import re
import pprint

# from Extraction.data_generic import jaguar
import fitz


from Generation.export_template import generate_RX_template
from misc_functions import execute_function, check_company
from Generation.generate_file import generate_file

from input import get_input
# from misc_functions import count_exporters

# final_RX_template = []
# so the data we want to extract is going to be put into the saem format each time
# should I start adding classes?

def parse_args():
    if len(sys.argv) < 2:
        print('format: python script.py <filename>')

    elif len(sys.argv) == 2 or len(sys.argv) > 2:
        # input = get_input()

        
        for arg in sys.argv[1:]:
            print(arg)
            company_name = check_company(arg)

            # this is basically the extract data function
            # this data should be in the form of 

            # TODO for each file - run this following function and add the results to a new list...        

            extracted_data = execute_function(arg, company_name)            
            print(extracted_data)
            # the default - separate files or commbine files - that should be an option
            # Using the final list generate a new CSV or Worksheet 

            # TODO generate combined file instead
            # TODO if rx flag selected then generate template
            generate_file(extracted_data)

            



# generate multiple invoices -
        # TODO fix this 
        ''' 
            Only multi-item invoices here - need to support multiple 
            for each file in system path - run the functions below, 
            return each list - append - then generate file with final

        '''
        # if company_name == 'Williams':
        #     # should this be an option? - if you 
        #     # generate_RX_template(extracted_data)
        #     generate_file(extracted_data)

        #     ''' Mann + Hummel works fine - move onto the next one'''
        # elif company_name == 'Mann + Hummel':
        #     generate_file(extracted_data)

        #     ''' This also works well - need to test on more files'''
        # elif company_name == 'Jaguar':
        #     generate_file(extracted_data)

        # elif company_name == 'Siemens':
        #     generate_file(extracted_data)
    else:
        pass
        
def main():
    parse_args()

if __name__ == "__main__":
    main()