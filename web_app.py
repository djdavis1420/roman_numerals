#!/C/Users/djdav/Development/Python/roman_numerals/venv/Scripts/python

import json

from flask import Flask
from flask import Response
from flask import request

from src.models.roman_to_arabic import RomanToArabicConverter
from src.models.arabic_to_roman import ArabicToRomanConverter

app = Flask(__name__)


@app.route('/convert/<input_string>', methods=['GET'])
def convert_by_get(input_string):
    try:
        number = int(input_string)
        converter = ArabicToRomanConverter()
        converted_number = converter.convert(number)
        result = str(input_string) + ' converts to ' + str(converted_number)
    except ValueError:
        converter = RomanToArabicConverter()
        converted_number = converter.convert(input_string)
        result = input_string + ' converts to ' + str(converted_number)
    return Response(json.dumps(result), status=200)


@app.route('/convert', methods=['POST'])
def convert_by_post():
    input_string = json.loads(request.data)
    try:
        number = int(input_string['convert'])
        converter = ArabicToRomanConverter()
        converted_number = converter.convert(number)
        result = str(number) + ' converts to ' + converted_number
    except ValueError:
        converter = RomanToArabicConverter()
        converted_number = converter.convert(input_string['convert'])
        result = input_string['convert'] + ' converts to ' + str(converted_number)
    return Response(json.dumps(result), status=200)


if __name__ == '__main__':
    app.run(debug=True)
