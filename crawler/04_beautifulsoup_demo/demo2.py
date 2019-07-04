from bs4 import BeautifulSoup

html = """
    <table class="table">
      <tbody>
        <tr class="active">
          <th scope="row">0</th>
          <td><a href="http://meowv.com">meowv</a></td>
          <td>Column content</td>
          <td>Column content</td>
        </tr>
        <tr class="active">
          <th scope="row">1</th>
          <td><a href="http://meowv.com">meowv</a></td>
          <td>Column content</td>
          <td>Column content</td>
        </tr>
        <tr>
          <th scope="row">2</th>
          <td><a href="http://meowv.com">meowv</a></td>
          <td>Column content</td>
          <td>Column content</td>
        </tr>
        <tr class="success">
          <th scope="row">3</th>
          <td><a href="http://meowv.com">meowv</a></td>
          <td>Column content</td>
          <td>Column content</td>
        </tr>
        <tr>
          <th scope="row">4</th>
          <td><a href="http://meowv.com">meowv</a></td>
          <td>Column content</td>
          <td>Column content</td>
        </tr>
        <tr class="info">
          <th scope="row">5</th>
          <td><a href="http://meowv.com">meowv</a></td>
          <td>Column content</td>
          <td>Column content</td>
        </tr>
        <tr>
          <th scope="row">6</th>
          <td><a href="http://meowv.com">meowv</a></td>
          <td>Column content</td>
          <td>Column content</td>
        </tr>
        <tr class="warning">
          <th scope="row">7</th>
          <td><a href="http://meowv.com">meowv</a></td>
          <td>Column content</td>
          <td>Column content</td>
        </tr>
        <tr>
          <th scope="row">8</th>
          <td><a href="http://meowv.com">meowv</a></td>
          <td>Column content</td>
          <td>Column content</td>
        </tr>
        <tr class="danger">
          <th scope="row">9</th>
          <td><a href="http://meowv.com">meowv</a></td>
          <td>Column content</td>
          <td>Column content</td>
        </tr>
      </tbody>
    </table>
"""

soup = BeautifulSoup(html, 'lxml')

# 1. 获取所有的tr标签
trs = soup.find_all('tr')
for tr in trs:
    print(tr)

# 2. 获取第2个tr标签
tr = soup.find_all('tr', limit=2)[1]
print(tr)

# 3. 获取class = success 的tr标签
trs = soup.find_all('tr', class_='success')
print(trs)

trs = soup.find_all('tr', attrs={'class': 'success'})
print(trs)

# 4. 获取所有a标签的href属性
aList = soup.find_all('a')
for a in aList:
    # 1. 通过下标操作的方式
    href = a['href']
    print(href)
    
    # 2. 通过attrs属性的方式
    href = a.attrs['href']
    print(href)

# 5. 获取所有存文本数据,不要第一个
trs = soup.find_all('tr')[1:]
result = []
for tr  in trs:
    # tds = tr.find_all('td')
    # txt1 = tds[0].string
    # txt2 = tds[1].string
    # txt3 = tds[2].string
    # item = {
    #     'txt1': txt1,
    #     'txt2': txt2,
    #     'txt3': txt3
    # }
    # result.append(item)

    infos = list(tr.stripped_strings)
    item = {
        'txt1': infos[0],
        'txt2': infos[1],
        'txt3': infos[2]
    }
    result.append(item)

print(result)

# find
a = soup.find('a')
print(a)

# get_text
tr = soup.find_all('tr')[1]
text = tr.get_text()
print(text)