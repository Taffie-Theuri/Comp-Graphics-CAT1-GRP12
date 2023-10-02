import os
import pandas as pd
import argparse

# Function to generate an xlxs file for a specific language pair (en-xx)
def generate_xlxs(language, data_directory):
    # Construct the path to the input JSONL file for the current language
    input_jsonl_file = os.path.join(data_directory, f'{language}.jsonl')

    # Read the JSONL file into a DataFrame
    df = pd.read_json(input_jsonl_file, lines=True)

    # Select only the relevant columns (id, utt, annot_utt)
    selected_columns = ['id', 'utt', 'annot_utt']
    df_selected = df[selected_columns]

    # Define the path to the output Excel file for the current language pair (en-xx)
    output_directory = os.path.join(data_directory, 'q1_py')
    os.makedirs(output_directory, exist_ok=True)
    output_xlxs_file = os.path.join(output_directory, f'en-{language}.xlsx')

    # Save the selected data to the Excel file
    df_selected.to_excel(output_xlxs_file, index=False)

    print(f"Saved '{output_xlxs_file}'")


def main():
    parser = argparse.ArgumentParser(description="Generate xlxs files for language pairs")
    parser.add_argument("data_directory", type=str, help="Path to the data directory")

    args = parser.parse_args()

    # Get a list of all JSONL files in the data directory
    jsonl_files = [file_name for file_name in os.listdir(args.data_directory) if file_name.endswith('.jsonl')]

    # Extract language codes from the file names
    languages = [file_name.split('.')[0] for file_name in jsonl_files]

    # Exclude 'en' (pivot language) from the list if it exists
    languages = [lang for lang in languages if lang != 'en']

    # Iterate through languages and generate xlxs files
    for lang_code in languages:
        generate_xlxs(lang_code, args.data_directory)

    print("Generation of Excel (xlxs) files completed.")


if __name__ == "__main__":
    main()




# import os
# import pandas as pd
# import argparse
#
# # Function to generate an xlxs file for a specific language pair (en-xx)
# def generate_xlxs(language, data_directory):
#     # Construct the path to the input JSONL file for the current language
#     input_jsonl_file = os.path.join(data_directory, f'{language}.jsonl')
#
#     # Read the JSONL file into a DataFrame
#     df = pd.read_json(input_jsonl_file, lines=True)
#
#     # Select only the relevant columns (id, utt, annot_utt)
#     selected_columns = ['id', 'utt', 'annot_utt']
#     df_selected = df[selected_columns]
#
#     # Define the path to the output Excel file for the current language pair (en-xx)
#     output_directory = os.path.join(data_directory, 'q1_py')
#     os.makedirs(output_directory, exist_ok=True)
#     output_xlxs_file = os.path.join(output_directory, f'en-{language}.xlsx')
#
#     # Save the selected data to the Excel file
#     df_selected.to_excel(output_xlxs_file, index=False)
#
#     print(f"Saved '{output_xlxs_file}'")
#
#
# def main():
#     parser = argparse.ArgumentParser(description="Generate xlxs files for language pairs")
#     parser.add_argument("data_directory", type=str, help="Path to the data directory")
#
#     args = parser.parse_args()
#
#     # Automatically identify languages from file names in the data directory
#     languages = [file_name.split('.')[0] for file_name in os.listdir(args.data_directory) if
#                  file_name.endswith('.jsonl')]
#
#     # Exclude 'en' (pivot language) from the list if it exists
#     languages = [lang for lang in languages if lang != 'en']
#
#     # Iterate through languages and generate xlxs files
#     for lang_code in languages:
#         generate_xlxs(lang_code, args.data_directory)
#
#     print("Generation of Excel (xlxs) files completed.")
#
#
# if __name__ == "__main__":
#     main()
