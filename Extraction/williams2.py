import fitz
import re
from Extraction.regex_engine import remove_commas, is_number

# extract the data, add it all to a table
# no RX logic here
# start with a single file

list_of_items = []

# invoice_charge = re.compile(r'TOTAL INVOICE CHARGE \d.*?[^A-Z]*')
# invoice_charge_deur = re.compile(r'DEUR TOTAL INVOICE CHARGE \d')

goods_values = re.compile(r'TOTAL GOODS VALUE \d.*?[^A-Z]*')
weight = re.compile(r'WEIGHT \(KG\) TOTAL ITEMS \d.*?[^A-Z]*')
ifor = re.compile(r'Ifor Williams Trailers Ltd') 
deeside = re.compile(r'IWT Deeside Ltd')

def extract_williams(path_to_pdf):
    
    # need to open these files from one file instead of repeating the code
    ''' 
    Single item vs multi-item 
    need to differentiate between them
    '''
    full_text = ''

    doc = fitz.open(path_to_pdf)
    for page in doc:
        text = page.get_text('text')
        full_text += text

    
    if 'SI-S' in path_to_pdf:
        # if (dropdown_value == 'Williams Spares'):
        list_of_items = []
        # TODO cut all after total charge
        test = re.compile(r'(Total Charge.*)', re.DOTALL)
        matches = re.findall(test, full_text)
        
        values_list = matches[0].split('\n')       
        clean_list = remove_commas(values_list)  

        for value in clean_list:
            if (is_number(value)):
                list_of_items.append(value)
        
        # divide the list by intervals of 4 

        ''' This function and the one after yield the same result'''
        final_output = [list_of_items[i:i + 4] for i in range(0, len(list_of_items), 4)]

        # def chunks(lst, n):
        #     """Yield successive n-sized chunks from lst."""
        #     for i in range(0, len(lst), n):
        #         yield lst[i:i + n]
        # for item in final_output:
        #     item.insert(0, 'IFORWILLI')
        
        # print(final_output)

        return final_output

    else:
        # else find the information 


        ''' 
        Single page invoices here
        '''
        # return list_of_items
        pass

# def williams(list_of_files):
    
#     files = list_of_files
#     # multi = count_exporters(files)

#     # testing the function without the function
#     multi = 2
#     print(multi)
            
#     for file in files:
#         # print(file)
#         item_data = extract_williams_data(file, input, multi)
#         # print(item_data)
#         # checks for a nested list 
#         if any(isinstance(i, list) for i in item_data):
#             # print(item_data)
#             for item in item_data:
#                 # print(item)
#                 final_RX_template.append(item)
#         else:
#             final_RX_template.append(item_data)
            
    
#     # print(final_RX_template)

#     # basically when we get to this part here - if IWTDEESI - add up the packages to that count
#     # if IFOR then add to a second count
#     IWT_count = []
#     IFOR_count = []


#     # not the best way to do this... 
#     ''' THIS function gets the number of packages from each exporter'''
#     for rx_item in final_RX_template:
#         if rx_item[2] == 'IWTDEESI':
#             IWT_count.append(rx_item[9])
            
#         elif rx_item[2] == 'IFORWILLI':
#             IFOR_count.append(rx_item[9])
    

#     total_packages_IWT = sum([int(i) for i in IWT_count])
#     total_packages_IFOR = sum([int(i) for i in IFOR_count])
    
    
#     for rx_item in final_RX_template:
#         if rx_item[2] == 'IWTDEESI':
#             rx_item[13] = total_packages_IWT
#             rx_item[16] = f'PART OF {total_packages_IWT} PACKAGES'
            

#         elif rx_item[2] == 'IFORWILLI':
#             rx_item[13] = total_packages_IFOR
#             rx_item[16] = f'PART OF {total_packages_IFOR} PACKAGES'
