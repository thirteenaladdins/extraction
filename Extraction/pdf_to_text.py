import sys
import fitz


def pdf_to_text(fname):
    # this is the beginning here

    # fname = sys.argv[1]  # get document filename
    doc = fitz.open(fname)  # open document
    out = open(fname + ".txt", "wb")  # open text output

    for page in doc:  # iterate the document pages
        text = page.get_text().encode("utf8")  # get plain text (is in UTF-8)
        out.write(text)  # write text of page
        out.write(bytes((12,)))  # write page delimiter (form feed 0x0C)
        # out.close()
    out.close()

# write out file to current script directory
