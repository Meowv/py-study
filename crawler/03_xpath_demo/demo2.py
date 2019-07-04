from lxml import etree

parser = etree.HTMLParser(encoding='utf-8')
html = etree.parse('table.html', parser=parser)

# 1. 获取所有的tr标签
# xpath函数返回的是一个列表
trs = html.xpath("//tr")
for tr in trs:
    print(etree.tostring(tr, encoding='utf-8').decode('utf-8'))

# 2. 获取第2个tr标签
tr= html.xpath("//tr[2]")[0]
print(etree.tostring(tr, encoding='utf-8').decode('utf-8'))

# 3. 获取class = success 的tr标签
trs = html.xpath("//tr[@class='success']")
for tr in trs:
    print(etree.tostring(tr, encoding='utf-8').decode('utf-8'))

# 4. 获取所有a标签的href属性
links = html.xpath("//a/@href")
for link in links:
    print(link)

# 5. 获取所有存文本数据
trs = html.xpath("//tr[position()>1]")
result = []
for tr in trs:
    # 在某个标签下执行 xpath函数，获取这个标签下的子孙元素应在 // 之前加一个点. 代表在当前元素下获取
    href = tr.xpath(".//a/@href")
    txt1 = tr.xpath("./td[1]//text()")
    txt2 = tr.xpath("./td[2]//text()")
    txt3 = tr.xpath("./td[3]//text()")

    item = {
        'href': href,
        'txt1': txt1,
        'txt2': txt2,
        'txt3': txt3,
    }
    result.append(item)
print(result)