import os
import json
import subprocess
# Let's extract the package-license pairs from the provided text file and convert them into a JSON format.
# Run the "dart run output.snapshot" command and capture the output
output = subprocess.check_output(["dart", "run", "dart_license_checker.dart"]).decode("utf-8")

# Print the output to the terminal
print(output)

# Write the output to the raw.txt file
with open("raw.txt", "w") as file:
    file.write(output)
    
# First, we'll read the contents of the file.
with open('raw.txt', 'r') as file:
    lines = file.readlines()

# Initialize a dictionary to store the package-license pairs.
package_license_pairs = {}

# Extract package-license pairs from the lines.
# We'll start processing from line 3 to skip the table header and borders.
for line in lines[4:-2]:
    # Removing Unicode characters and extra spaces from each line.
    cleaned_line = line.replace('\u2502', '').strip()
    # Splitting the cleaned line into package and license parts, assuming they are separated by two or more spaces.
    parts = cleaned_line.rsplit('  ', 1)
    if len(parts) == 2:
        package, license = parts[0].strip(), parts[1].strip()
        # Handle the 'No license file' case, setting the license to None.
        package_license_pairs[package] = None if license == "No license file" else license

# Specify the path for the output JSON file.
output_file_path = 'license_list.json'

# Write the dictionary to the specified JSON file.
with open(output_file_path, 'w') as json_file:
    json.dump(package_license_pairs, json_file, indent=4)

print(f"Package-license pairs have been extracted to {output_file_path}")
