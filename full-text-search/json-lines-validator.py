# Python program to validate records of JSON lines file

import json

def is_json(myjson):
  try:
    json.loads(myjson)
  except ValueError as e:
    return False
  return True

print("Enter the name of the JSON lines file to be validated:")
filename = str(input())
print("\nChecking file:", filename)

# validate one line at a time
with open(filename, 'rt') as f:
    linecount = 0
    number_invalid_lines = 0
    for line in f:
        linecount += 1
        if (is_json(line)):
            pass
        else:
            number_invalid_lines += 1
            print("\nline ", linecount, " is not valid JSON")
            
print("\n", number_invalid_lines, "invalid lines in ", filename)

        