# Description: This script adds the x-api-key parameter to all operations in the
#              anthropic-spec.json file. This is necessary because the x-api-key
#              parameter is required for authenticating all operations in the API.
# Usage: python fix_spec.py --file <path-to-anthropic-spec.json>

import argparse
import json

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Fix the anthropic-spec.json file.")
parser.add_argument(
    "-f", "--file", default="specs/anthropic-spec.json", help="Path to the JSON file."
)
args = parser.parse_args()

filename = args.file
print(f"Fixing the JSON file: {filename}")

with open(filename, "r") as f:
    data = json.load(f)

# Find the x-api-key parameter
x_api_key_param = None

for path_item in data.get("paths", {}).values():
    for operation in path_item.values():
        parameters = operation.get("parameters", [])
        for param in parameters:
            if param.get("name") == "x-api-key":
                x_api_key_param = param
                break
        if x_api_key_param:
            break
    if x_api_key_param:
        break

if x_api_key_param is None:
    print("x-api-key parameter not found in the JSON file.")
    exit(1)

# Add x-api-key parameter to all operations
for path_item in data.get("paths", {}).values():
    for operation in path_item.values():
        if isinstance(operation, dict):
            parameters = operation.setdefault("parameters", [])
            if not any(param.get("name") == "x-api-key" for param in parameters):
                parameters.append(x_api_key_param)

# Save the updated JSON data
with open(filename, "w") as f:
    json.dump(data, f, indent=2)
