# First thing we'll do is import the requests library
import requests
import csv
results = []
with open('/urls.csv', newline='' ) as read_obj:
    for row in csv.reader(read_obj):
        results.append(row[0])
for x in results:
    response = requests.get(x)
    print(f"{x};{response.status_code}")

