
# add flags?
# capitalise the inputs - remove commas just incase
# reference - allow only letters and numbers - maybe dashes



from Extraction.regex_engine import is_number

def get_input():

    # TODO remove accidental commas - ?

    reference = str(input("Reference: ")).upper()
    vehicle = str(input('Vehicle: ')).upper()
    
    # should be a number only 
    # exchange_rate = input('Exchange Rate: ')

    while True:
        exchange_rate = input("Exchange Rate: ")
        
        if not exchange_rate:
            break
        # check for number
        elif is_number(exchange_rate):            
            break
        else:
            print ("Exchange rate must be positive number. Try Again. \n")

    return reference, vehicle, exchange_rate

# exchange rate has to be a number