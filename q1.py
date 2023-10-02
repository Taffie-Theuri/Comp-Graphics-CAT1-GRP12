import os
import json
import pandas as pd

def generate_excel_files_for_language(folder_path, output_directory):
    # Create a dictionary to store data for each language
    language_data = {}

    # Loop through JSONL files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".jsonl"):
            with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as file:
                for line in file:
                    data = json.loads(line)
                    language = data.get('locale')

                    # Filter for English (en) language
                    if language == 'en-US':
                        language_id = data.get('id')
                        utt = data.get('utt')
                        scenario = data.get('scenario')
                        intent = data.get('intent')
                        annot_utt = data.get('annot_utt')

                        if language_id not in language_data:
                            language_data[language_id] = {'id': [], 'utt': [],'scenario': [], 'intent': [],'annot_utt': []}

                        language_data[language_id]['id'].append(language_id)
                        language_data[language_id]['utt'].append(utt)
                        language_data[language_id]['scenario'].append(scenario)
                        language_data[language_id]['intent'].append(intent)
                        language_data[language_id]['annot_utt'].append(annot_utt)

    # Create Excel files for each language in the specified output directory
    for language_id, data_dict in language_data.items():
        df = pd.DataFrame(data_dict)
        excel_filename = os.path.join(output_directory, f'en-{language_id}.xlsx')
        df.to_excel(excel_filename, index=False)
        print(f'Excel file {excel_filename} created for language {language_id}')

# Specify the folder path and output directory
folder_path = r'C:\Users\stanl\Downloads\Group_CAT-main\Group_CAT-main\data\output'  # Replace with your folder path
output_directory = r'C:\Users\stanl\Downloads\Group_CAT-main\Group_CAT-main\data\output'  # Desired output directory

# Call the function with the specified paths
generate_excel_files_for_language(folder_path, output_directory)
