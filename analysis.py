import csv

reader = csv.DictReader(open('scrape.csv', 'r'))
result = sorted(reader, key=lambda d: d['author'])

writer = csv.DictWriter(open('analysis.csv', 'w'), reader.fieldnames)
writer.writeheader()
writer.writerows(result)
