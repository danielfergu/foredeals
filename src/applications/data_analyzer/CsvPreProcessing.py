import csv

#Process zillow data taken from https://data.world/zillow-data/median-home-value-per-sq-ft 
#to make it easier to handle sqft-price data

class CsvPreProcessing:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def process_csv(self):
        data = []
        with open(self.input_file, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            for row in csv_reader:
                zip_code = int(row[1].replace('"', ''))
                sqft_price = row[-1]
                data.append([zip_code, sqft_price])

        with open(self.output_file, 'w', newline='') as csv_output:
            csv_writer = csv.writer(csv_output)
            csv_writer.writerow(['zip_code', 'sqft_price'])
            csv_writer.writerows(data)

if __name__ == "__main__":
    processor = CsvPreProcessing('Zip_MedianValuePerSqft_AllHomes.csv', 'sqft_price.csv')
    processor.process_csv()
