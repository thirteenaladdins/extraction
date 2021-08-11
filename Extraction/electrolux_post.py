# from fetch_tariff import extract_tariff_data
# from misc_functions import get_num_pages
import re
import pprint
from collections import namedtuple
import fitz

def filter_invoice():

    return
    # TODO Create generic function that accepts a list of regex parameters and
    # filters each page based on those criteria - reuse thse for all invoices


list_items = []


# TODO still working on making it all more useful
# this actually isn't as simple as I thought

# from 6 digits all the way to a %... doesn't work. Do we have a prefix?
# getting closer to cracking the puzzle.

# so can I do 6 or 8?
# so preceeded by a space makes the difference.

# just as long as they're not

# multi line or dotall.
# the dot should match
# match = re.compile(r' \d{6}.*% [a-zA-z]', flags=re.MULTILINE)# type:

# min 6 digits up to 10
match = re.compile(r' \d{6}.* [A-Z]')

# so this is going to be different for fitz I guess...

# match = re.compile(r'\d{6}', flags=re.DOTALL)



def parse_pdf(pdf_document):
    full_text = ''

    # number_of_pages = get_num_pages(pdf)

    # for i in range(number_of_pages):
    for page in pdf_document:
        page = page.get_text("text")
        # page = pdf.pages[i].extract_text()

        # print(page)


        print(page)
        full_text += page
        


    joined_text = ' '.join(full_text.split('\n'))

    print(joined_text)
    matched_items = re.findall(match, joined_text)
    # print(matched_items)
    return matched_items


# easiest one
def extract_tariff(item):
    tariff = item[0]
    origin = item[-1]
    # return tariff + origin
    tariff_origin = f'{tariff} {origin}'
    return tariff_origin


def extract_pieces(item):
    try:
        pieces = item[1].replace(',', '.')
        return pieces
    except:
        pass

def extract_value(item):
    try:
        value = item[3].replace('.', '').replace(',', '.')
        return value
    except:
        pass

# should I convert all ints to floats across the whole program?
def calculate_pieces(matched_items):
    count = float()
    for item in matched_items:
        split_list = item.split()
        # print(split_list)
        pieces = split_list[1].replace(',', '.').strip()
        count += float(pieces)

    # print(count)
    return count


invoice = namedtuple('inv', 'tariff pieces gross net value')

# the fact that they're throwing in random 6 digit tariffs makes it a bit harder.


def extract_electro(path_to_pdf):

    pdf_file = fitz.open(path_to_pdf)
    matched_items = parse_pdf(pdf_file)
    # total_pieces = calculate_pieces(matched_items)
    # print(total_pieces)
    # print(matched_items)

    for line in matched_items:

        # turn string into list
        item = line.split()
        tariff = extract_tariff(item)
        pieces = extract_pieces(item)
        # pieces = ''
        # gross = ''
        # net = ''

        # weight - total quantity - pieces
        # gross = pro_rata_weight(gross_weight, total_pieces, pieces)
        # net = pro_rata_weight(net_weight, total_pieces, pieces)

        gross = ''
        net = ''

        value = extract_value(item)
        # value = ''

        list_items.append(invoice(tariff,
                                  pieces, gross, net, value))
    
    print(list_items)

    return list_items
