import csv
import random

with open('sequences_hundred_thousand.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['ID', 'Sequence'])

    for step in range(1, 100001):
        num = "A" + "0" * (6 - len(str(step))) + str(step)
        a_previous = random.randint(1, 1000000)
        sequence = [a_previous]
        for size in range(1, 101):
            a_next = a_previous + step
            sequence.append(a_next)
            a_previous = a_next
        csv_writer.writerow([num, sequence])