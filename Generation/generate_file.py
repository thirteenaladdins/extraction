import datetime
import pandas as pd


def generate_file_name():
    ##### UNIQUE FILE NAME ######
    basename = "invoice_extracted-data"
    suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")

    # e.g. 'filename_120508_171442'
    file_name = "_".join([basename, suffix])
    return file_name


headers_list = ['tariff', 'description', 'quantity', 'gross', 'net', 'value'] 

def generate_file(list_items):
    file_name = generate_file_name()
    df = pd.DataFrame(list_items)

    df.index = df.index + 1

    # TODO - Export and Save
    df.to_csv(f'../{file_name}.csv', header=headers_list)
    return df

    # DF to CSV.
