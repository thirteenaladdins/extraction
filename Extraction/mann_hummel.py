from collections import namedtuple
from list_of_countries import EU_27
import re
import pprint

# from tariff_extractor import values

# pass in values, return new value for net and gross
# gross and net are a constant for each file

# EAD to T1 afterwards


list_items = []
invoice = namedtuple('inv', 'tariff description pieces gross net value')

# TODO there should be a generic base function that does each thing, value, tariff, COO etc.

# so if we get the lists of items


def extract_tariff_and_origin(EU_True, line):
    try:
        sep = 'per'
        second_half_of_line = line.split(sep, 1)[1]
        # print(second_half_of_line)

        items = second_half_of_line.split()
                
        match = re.compile(r'\d{8}')
        indices = [i for i, s in enumerate(items, start=0) if re.search(match, s)]
        
        # so with this we're 

        tariff_index = indices[0]
        tariff_origin = ' '.join(items[tariff_index:])

        # TODO regex -
        # getting closer here. 

        # tariff_origin = ' '.join(items[1:])

        filtered_tariff_origin = tariff_origin.replace(
            'total', '').replace('net', '').replace('-', ' ').replace('Total', '').replace('_', '').replace('Invoice', ''
            ).replace('Unternehmensbereich Automotive to', '').strip()

            
        print(filtered_tariff_origin)      

        # remove digits and leave country name
        country = re.sub(r'\d', '', filtered_tariff_origin)

        numbers = filter(str.isdigit, filtered_tariff_origin)
        tariff = "".join(numbers)

        country_stripped = country.strip()

        # if the checkbox is checked then
        if EU_True == True:
            # print("Convert to EU checked")
            if country_stripped in EU_27:
                filtered_tariff_origin = f'{tariff} EU'

        return filtered_tariff_origin

    except:
        pass


def extract_pieces(line):
    try:

        sep = 'per'
        stripped_2 = line.split(sep, 1)[0]
        # print(stripped_2)
        split_list = stripped_2.split()

        num_pieces = split_list[-3]
        pieces = num_pieces.replace(',', '')
        # pass
        return pieces
    except:
        pass


def extract_value(line):
    try:
        sep = 'per'
        # need better variables this is ridiculous. No idea what anything is.
        second_half_of_line = line.split(sep, 1)[1]

        items = second_half_of_line.split()
        # print(split_list_first)
        # remove the first 3 items from list
        # for _ in range(3):
        #     split_list_first.pop(0)

        value = items[1]
        return value
    except:
        pass


# TODO clear the cache before running it the next time.
# TODO resize the window, maybe colour it differently

def extract_mann(Convert_EU, matched_items):
    # pass invoice data here
    for line in matched_items:
        # print(line)

        tariff = extract_tariff_and_origin(Convert_EU, line)

        pieces = extract_pieces(line)

        description = ''
        gross = ''
        net = ''

        value = extract_value(line)

        list_items.append(invoice(tariff, description,
                                  pieces, gross, net, value))

    # populate a csv from these values

    # print(list_items)
    return list_items

# close app after running.
