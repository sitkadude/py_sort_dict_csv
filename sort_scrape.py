# SORT SCRAPE

# Dependenices
import csv

# Create object that maps rows to a dictionary.
reader = csv.DictReader(open('scrape.csv', 'r'))
# Sort rows in object by key name 'author' via lambda function.
result = sorted(reader, key=lambda d: d['author'])

# Create object that maps dictionaries onto output rows.
writer = csv.DictWriter(open('sorted_scrape.csv', 'w'), reader.fieldnames)
# Write row with assigned fieldnames in 'analysis.csv'.
writer.writeheader()
# Write newly sorted rows to output file.
writer.writerows(result)
