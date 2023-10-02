import os
import json
import sys

if len(sys.argv) != 2:
    print("Usage: python q2.py <data_directory>")
    sys.exit(1)

data_directory = sys.argv[1]

# Create an output directory called "q2_output" if it doesn't exist
output_directory = os.path.join(data_directory, 'q2_output')
os.makedirs(output_directory, exist_ok=True)

# Define language codes and splits
languages = ['en-US', 'sw-KE', 'de-DE']
splits = ['test', 'train', 'dev']

# Step 1: Iterate through languages and splits
for lang_code in languages:
    for split in splits:
        # Define the path to the input JSONL file for the current language and split
        input_jsonl_file = os.path.join(data_directory, f'{lang_code}.jsonl')

        # Define the path to the output JSONL file for the current language and split
        output_jsonl_file = os.path.join(output_directory, f'{lang_code}_{split}.jsonl')

        # Create a list to hold records for the current split
        split_records = []

        # Read the JSONL file and filter records by split
        with open(input_jsonl_file, 'r', encoding='utf-8') as jsonl_file:
            for line in jsonl_file:
                record = json.loads(line)
                if record.get('partition') == split:
                    split_records.append(record)

        # Step 2: Save filtered records to a JSONL file for the current split
        with open(output_jsonl_file, 'w', encoding='utf-8') as output_file:
            for record in split_records:
                output_file.write(json.dumps(record, ensure_ascii=False) + '\n')

        print(f"Saved '{output_jsonl_file}'")

print("Generation of JSONL files completed.")
