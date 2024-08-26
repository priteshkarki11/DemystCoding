
import csv
import faker as fk
import hashlib

"""
Here i am using faker api to generate random data
sha256 to generate anonymzed data for given csv
"""
def generate_random_csv(input_file_name, total_records):
    fkr = fk.Faker()
    header = ['first_name','last_name','address','date_of_birth']

    with open(input_file_name, 'w', newline='') as csvfile1:
        writer = csv.writer(csvfile1)
        writer.writerow(header)

        for _ in range(total_records):
            writer.writerow([fkr.first_name(), fkr.last_name(), fkr.address(), fkr.date_of_birth()])


def anonymize_csv_data(input_csv_file, output_csv_file):
    with open(input_csv_file, 'r') as csvfile, open (output_csv_file, 'w', newline='') as outfile:
        reader = csv.DictReader(csvfile)
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            row['first_name'] = hashlib.sha256(row['first_name'].encode()).hexdigest()
            row['last_name'] = hashlib.sha256(row['last_name'].encode()).hexdigest()
            row['address'] = hashlib.sha256(row['address'].encode()).hexdigest()
            writer.writerow(row)

if __name__=='__main__':
    generate_random_csv('random_data.csv',1000)
    anonymize_csv_data('random_data.csv','anonymized_output_data.csv')