# Python program to validate records of JSON lines file
# input must be edges file... knowledge base triples 
# converts to plain text file

import json

def is_json(myjson):
  try:
    json.loads(myjson)
  except ValueError as e:
    return False
  return True

# here the file for testing is nielsen-edges.jl
print("Enter the name of the JSON lines file to be renedered as text:")
filename = str(input())
print("\nInput JSON lines file:", filename)

# validate one line at a time while writing to text csv file
with open ('triples_text.csv', 'wt') as fcsv:
    with open(filename, 'rt') as f:
        linecount = 0
        number_invalid_lines = 0
        for line in f:
            linecount += 1
            if (is_json(line)):
                json_data = json.loads(line)
                text_to_parse = json_data['subject_type'] + ' ' + json_data['subject_name'] + ' ' + json_data["relation"] + ' ' + json_data["object_type"] + ' ' + json_data["object_name"]     
                text_parsed = text_to_parse.replace('_',' ')
                fcsv.write(text_parsed + '\n')
            else:
                number_invalid_lines += 1
                print("\nline ", linecount, " is not valid JSON")
            
print("\n", number_invalid_lines, "invalid lines in ", filename)

