# TODO just make this better
# DRY

# this is what is supposed to be removed from the full text

def get_definitions(dropdown_value):
    if dropdown_value == 'Mann + Hummel':
        test_header = r"MANN\+ HUMMEL.*origin"
        # test_header = r"MANN\+HUMMEL"
        # test_header_2 = r"MANN\+ HUMMEL"
        test_footer = r"Our published terms.*"
        # test_footer = r"Invoice.*"
        other_text = r"Total net"
        test_numbers = r"- \d.*"
        # underscore = r'-'
        

        regex_definitions = [test_header, test_footer, test_numbers, '_', 'Invoice', 'Page']
        return regex_definitions

# this isn't exactly what I'm going for.
# I'll come back to this
    elif dropdown_value == 'Electrolux':
        pass
    elif dropdown_value == 'Williams Spares':
        
        definition = r'As an approved.*'
        regex_definitions = [definition]
        return regex_definitions
        
    else:
        pass


# electrolux - requires preprocess to remove all new lines from each page
# new_item = re.compile(r' \d{6}.*%', flags=re.DOTALL)
