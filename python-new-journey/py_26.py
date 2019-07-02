# 读写csv数据

import csv

with open('python-new-journey/files/demo.csv', 'r', encoding='utf8') as rf:
    reader = csv.reader(rf)
    with open('python-new-journey/files/demo_copy.csv', 'w', encoding='utf8') as wf:
        writer = csv.writer(wf)
        headers = next(reader)
        writer.writerow(headers)
        for row in reader:
            if int(row[2]) < 20:
                break
            if row[3] == '男':
                writer.writerow(row)