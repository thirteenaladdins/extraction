# import fitz
# import re


# from Extraction.regex_engine import extract_data
# # from Generation.export_template import generate_RX_template
# from Extraction.regex_engine import remove_commas
# # RX template generator
# # from Extraction.williams import extract_williams_data
# # from misc_functions import count_exporters

# # TODO fix the count_exporters problem


# deeside_pattern = re.compile(r'INV\d{1}')

# final_RX_template = []


# def get_trailer_count(list_of_words):
#     # find index of word 
#     try:
#         test = re.compile(r'(Total Charge.*)', re.DOTALL)
#         search_list = re.findall(test, list_of_words)[0]
#         split_list = search_list.split(' ')
        
#         # TODO check here for tariff

#         trailer_index = split_list.index('87163950')
#         trailer_count = split_list[trailer_index + 1]
#         return trailer_count
        
#     except IndexError:
#         # print('No matches found')
#         pass


# def extract_williams_data(path_to_pdf, input, multiple_exp):
#     goods_values = re.compile(r'TOTAL GOODS VALUE \d.*?[^A-Z]*')
#     # invoice_charge = re.compile(r'TOTAL INVOICE CHARGE \d.*?[^A-Z]*')
#     # invoice_charge_deur = re.compile(r'DEUR TOTAL INVOICE CHARGE \d')
#     weight = re.compile(r'WEIGHT \(KG\) TOTAL ITEMS \d.*?[^A-Z]*')
#     ifor = re.compile(r'Ifor Williams Trailers Ltd') 
#     deeside = re.compile(r'IWT Deeside Ltd')
    
#     # TODO add this to the export template file
#     # TODO - separate this out

    
#     # TODO - this input is for the template
#     # ref, vehicle, exchange = input
    
#     # if SI-S - run extract_data

#     # TODO 
#     if 'SI-S' in path_to_pdf:
#         # pdf_document_SI-S = fitz.open(path_to_pdf)
#         final_output = []

#         # TODO bring extraction logic here


#         list_of_tariff_info = extract_data(path_to_pdf, 'Williams Spares')
#         # print(list_of_tariff_info)
#         for item in list_of_tariff_info:

#             # item_information_list = [
#             # '', '', '', '', '', '', '1000001', '', '', '',
#             # '', '', '', '', '', 'PK', 'PART OF PACKAGES', 'LIC99', '', '',
#             # 'N821', 'AC', '', '', '', '', '', '', '', '', 
#             # '', 'Z', '380', 'INV', 
#             # ]

#             # # capitalize the reference and all the other text
#             # if ref:
#             #     # if multi is true add A for IFOR and B for IWT 
#             #     if multiple_exp:
#             #         item_information_list[0] = ref + 'A'
#             #         item_information_list[22] = ref + 'A'
#             #     else:
#             #         item_information_list[0] = ref
#             #         item_information_list[22] = ref

#             # if vehicle:
#             #     item_information_list[1] = vehicle

#             # item_information_list[2] = 'IFORWILLI'
#             # # tariff
#             # item_information_list[7] = item[0]
#             # # quantity2
#             # item_information_list[9] = item[1]
#             # # quantity
#             # item_information_list[14] = item[1]
#             # # gross
#             # item_information_list[11] = item[2]
#             # # net weight
#             # item_information_list[12] = item[2]
#             # # value 
            

#             if exchange:             
#                 # convert to exchange rate   
#                 value_split = float(item[3]) / float(exchange)
#                 # print(value_split)
#                 rounded_3dp = round(value_split, 3)
#                 # print(rounded_3dp)
#                 item_information_list[10] = rounded_3dp
                
#             else:
#                 item_information_list[10] = item[3]

#             # print(item_information_list)
#             final_output.append(item_information_list)
#             # print(final_output)
        
#         # print(final_output) 
#         return final_output
        

#     else:
#         pdf_document = fitz.open(path_to_pdf)

#         full_text = ''
#         # item_information = {}

#         for page in pdf_document:
#             # Text vs block etc
#             page_text = page.get_text("text")
#             full_text += page_text

        
#         split_words = full_text.split('\n')
#         joined_words = ' '.join(split_words)

#         trailer_count = get_trailer_count(joined_words)
#         goods_value_search = re.search(goods_values, joined_words)

#         # invoice_search = re.search(invoice_charge, joined_words)
#         weight_search = re.search(weight, joined_words)
#         ifor_search = re.search(ifor, joined_words)
#         iwt_search = re.search(deeside, joined_words) 
            
#         # if vehicle:
#         #         item_information_list[1] = vehicle
        
#         # if iwt_search:
#         #     # item_information.append('IWT')
#         #     # item_information_list.append('IWT')
#         #     item_information_list[2] = 'IWTDEESI'
#         #     # item_information['short_code'] = 'IWT'
#         #     # print(iwt_search.group(0))
#         #     if ref:
#         #         if multiple_exp:
#         #             item_information_list[0] = ref + 'B'
#         #             item_information_list[22] = ref + 'B'
#         #         else:
#         #             item_information_list[0] = ref
#         #             item_information_list[22] = ref

        
#         # elif ifor_search:
#         #     # item_information_list.append('IFORWILLI')
#         #     # item_information['short_code'] = 'IFORWILLI'
#         #     # print(ifor_search.group(0))
#         #     item_information_list[2] = 'IFORWILLI'

#         #     if ref:
#         #         if multiple_exp:
#         #             item_information_list[0] = ref + 'A'
#         #             item_information_list[22] = ref + 'A'
#         #         else:
#         #             item_information_list[0] = ref
#         #             item_information_list[22] = ref
        
#         # if trailer_count:
#         #     # print('TARIFF 87163950')
#         #     # print('TRAILERS', trailer_count)
#         #     item_information_list[7] = '87163950'
#         #     item_information_list[9] = trailer_count
#         #     item_information_list[14] = trailer_count
            
#         #     # item_information_list.append('87163950')
#         #     # item_information_list.append(trailer_count)

#         #     # item_information['tariff'] = '87163950'
#         #     # item_information['trailers'] = trailer_count
#         #     # item_information.append(trailer_count)

#         # if weight_search:
#         #     weight_split = weight_search.group(0).split(' ')
#         #     weight_split = remove_commas(weight_split)

#         #     item_information_list[11] = weight_split[4] 
#         #     item_information_list[12] = weight_split[4] 
#         #     # item_information['weight'] = weight_split[4]
#         #     # print(weight_search.group(0))
            
#         # if goods_value_search:
#         #     value_split = goods_value_search.group(0).split(' ') 
#         #     value_split = remove_commas(value_split)

#         #     print(value_split)

#         #     if exchange:
#         #         value_split = float(value_split[3]) / float(exchange)
#         #         # print(value_split)
#         #         rounded_3dp = round(value_split, 3)
#         #         # print(rounded_3dp)

#         #         item_information_list[10] = rounded_3dp
            
#         #     else:

#         #         item_information_list[10] = value_split[3]

            
#         #     # item_information_list.append(value_split[3])
#         #     # item_information['value'] = value_split[3]
#         #     # print(goods_value_search.group(0))       

#     # print(item_information_list)
#     return item_information_list

# # this code is a mess. I should just start again.