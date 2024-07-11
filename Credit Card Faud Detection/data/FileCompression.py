'''Since the actual csv file is so large cannot be directly push into github therefore we have to compress it before pushing onto the github
'''

import lzma
import shutil

def compress_csv_xz(file_path, output_path):
    with open(file_path, 'rb') as f_in:
        with lzma.open(output_path, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    print(f'Compressed file saved to {output_path}')

# Usage
input_file = 'fraudTrain.csv'
output_file = 'fraudTrain.csv.xz'
compress_csv_xz(input_file, output_file)

input_file = 'fraudTest.csv'
output_file = 'fraudTest.csv.xz'
compress_csv_xz(input_file, output_file)
