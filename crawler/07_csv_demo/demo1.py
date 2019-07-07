import csv

def read_csv_demo1():
    with open('users.csv', 'r', encoding='utf-8') as fp:
        # reader是一个迭代器
        reader = csv.reader(fp)
        # 不取第一行
        next(reader)
        for x in reader:
            print(x)
            id = x[1]
            user = x[2]
            print({'id':id,'user':user})

def read_csv_demo2():
    with open('users.csv', 'r', encoding='utf-8') as fp:
        # DictReader 创建的对象不会包含第一行标题的数据
        reader = csv.DictReader(fp)
        for x in reader:
            value = {'id':x['id'],'user':x['user']}
            print(value)

if __name__ == "__main__":
    # read_csv_demo1()
    read_csv_demo2()