import requests
from bs4 import BeautifulSoup
import csv

basis_url = 'https://oeis.org/'

with open('sequences.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['ID', 'Sequence'])

    for i in range(1, 10):
        num = "A" + "0" * (6 - len(str(i))) + str(i)
        url = basis_url + num

        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            noisy_out = soup.find('tt')

            if noisy_out:
                sequence_text = noisy_out.string
                integer_sequence = [int(num) for num in sequence_text.split(',')]
                csv_writer.writerow([num, integer_sequence])
            else:
                continue
