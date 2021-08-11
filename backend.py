from flask import Flask, request
from flask_cors import CORS
from Extraction.regex_engine import extract_data
import sys


app = Flask(__name__)
CORS(app)

# receive data here
# pass the file path to the file

@app.route('/test', methods=['POST'])
def run_execution():
    data = request.form['file']
    extract_data(data)
    print(data, file=sys.stderr)
    # return 'hello world'

# get file path

if __name__ == '__main__':
    app.run()