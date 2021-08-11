# keep working on this.
# keep working on this until it just fucking works.

def get_match_definition(dropdown_value):
    if dropdown_value == 'Mann + Hummel':
        return r'0\d{3}  .*?per .*?[A-Z](?:(?!\d).)*'

    elif dropdown_value == 'Electrolux':
        return r' \d{6}.*%'
    elif dropdown_value == 'Williams Spares':
        return r'\d{8}.*'
    else:
        pass
