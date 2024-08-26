import csv
import json


def parseFixedWidth_file(spec_file, input_file, output_file):
    spec_dict = {}
    with open(spec_file, 'r', encoding='utf-8') as f_spec:
        spec_dict = json.load(f_spec)

    column_name = spec_dict["ColumnNames"]
    offsets = spec_dict["Offsets"]

    columns_positions = []
    start_pos = 0

    for offset in offsets:
        end_pos = start_pos + int(offset)
        columns_positions.append((start_pos, end_pos))
        start_pos = end_pos

    with open(input_file, 'r', encoding=spec_dict.get("FixedWidthEncoding", "utf-8")) as f_in, \
            open(output_file, 'w', newline='', encoding=spec_dict.get("DelimitedEncoding", "utf-8")) as f_out:
        csv_writer = csv.writer(f_out)

        if spec_dict.get("IncludeHeader", "True").lower() == "true":
            csv_writer.writerow(column_name)
            for line in f_in:
                row = [line[start:end].strip() for start, end in columns_positions]
                csv_writer.writerow(row)


if __name__ == '__main__':
    parseFixedWidth_file('data.json', '../DemystCoding/sample_fixed_width.txt', 'output_data.csv')
