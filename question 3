import os
import json
import sys

if len(sys.argv) != 2:
    print("Usage: python q3.py <data_directory>")
    sys.exit(1)

data_directory = sys.argv[1]

# Create an output directory called "q3_output" if it doesn't exist
output_directory = os.path.join(data_directory, 'q3_output')
os.makedirs(output_directory, exist_ok=True)

# Define language codes and splits
languages = ['en-US', 'sw-KE', 'de-DE']

# Create a dictionary to store translations
translations = {}

# Iterate through languages
for lang_code in languages:
    # Define the path to the input JSONL file for the current language and split (train)
    input_jsonl_file = os.path.join(data_directory, 'q2_output', f'{lang_code}_train.jsonl')

    # Initialize a list to hold records for the current language
    lang_records = []

    # Read the JSONL file and extract relevant fields (id and utt)
    with open(input_jsonl_file, 'r', encoding='utf-8') as jsonl_file:
        for line in jsonl_file:
            record = json.loads(line)
            lang_records.append({'id': record['id'], 'utt': record['utt']})

    # Add the language records to the translations dictionary
    translations[lang_code] = lang_records

# Save the translations to a single JSON file within the "q3_output" directory
output_json_file = os.path.join(output_directory, 'translations.json')
with open(output_json_file, 'w', encoding='utf-8') as output_file:
    json.dump(translations, output_file, ensure_ascii=False, indent=4)

print(f"Saved '{output_json_file}'")
print("Generation of the large JSON file completed.")
