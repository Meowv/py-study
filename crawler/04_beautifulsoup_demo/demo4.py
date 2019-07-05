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
    <div>123</div>
    <p><!--注释--></p>
"""

soup = BeautifulSoup(html, 'lxml')
print(type(soup))

table = soup.find('table')
print(type(table))

div = soup.find('div')
print(type(div.string))

p = soup.find('p')
print(p.string)
print(type(p.string))
print(p.contents)
print(type(p.contents))

table = soup.find('table')
for element in table.contents:
    print(element)