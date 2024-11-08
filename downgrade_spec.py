import argparse
import json
import copy

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Fix the anthropic-spec.json file.")
parser.add_argument(
    "-f", "--file", default="specs/anthropic-spec.json", help="Path to the JSON file."
)
args = parser.parse_args()

filename = args.file
print(f"Fixing the JSON file: {filename}")

input_file = filename
output_file = filename.split('.')[0] + '_v3.0.0.json'

with open(input_file, 'r') as f:
    data = json.load(f)

if 'openapi' not in data or data['openapi'] != '3.1.0':
    print("The input file is not a valid OpenAPI 3.1.0 file.")
    exit(1)

data['openapi'] = '3.0.0'

def process_anyof(obj):
    if isinstance(obj, dict):
        cp_obj = copy.copy(obj)
        for key in cp_obj.keys():
            value = obj[key]
            # remove 'null' from anyOf
            if key == 'anyOf' and isinstance(value, list):
                new_anyof = [v for v in value if v.get('type') != 'null']
                if len(new_anyof) != len(value):
                    obj['nullable'] = True
                value = new_anyof
            
            # remove 'const' from type (if enum)
            if key == "const" and 'enum' in obj:
                obj.pop(key)
                continue

            # else process recursively
            obj[key] = value
            obj[key] = process_anyof(value)

    elif isinstance(obj, list):
        return [process_anyof(item) for item in obj]

    return obj

new_data = process_anyof(data)

with open(output_file, 'w') as f:
    json.dump(new_data, f, indent=2)
