import csv

headers = ['username','age','height']

def write_csv_demo1():
    values = [
        ('张三',18,180),
        ('李四',19,170),
        ('王五',20,160),
    ]

    with open('classroom.csv', 'w', encoding='utf-8', newline='') as fp:
        write = csv.writer(fp)
        write.writerow(headers)
        write.writerows(values)

def write_csv_demo2():
    values = [
        {'username':'张三', 'age':18, 'height': 180},
        {'username':'李四', 'age':19, 'height': 170},
        {'username':'王五', 'age':20, 'height': 160}
    ]
    with open('classroom.csv', 'w', encoding='utf-8', newline='') as fp:
        write = csv.DictWriter(fp, headers)
        # 写入表头数据，需要调用writeheader()方法
        write.writeheader()
        write.writerows(values)

if __name__ == "__main__":
    # write_csv_demo1()
    write_csv_demo2()