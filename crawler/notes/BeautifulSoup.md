# BeautifulSoup

## find_all的使用
- 在提取标签的时候，第一个参数是标签的名字，然后如果在提取标签的时候想要使用标签属性进行过滤，那么可以再这个方法中通过关键字参数的形式，将属性的名字以及对于的值传进去。或者是使用`attrs`属性，将所有的属性以及对于的值放在一个字典中传给`attrs`属性。
- 有些时候，在提取标签的时候，不想提取那马多，可以使用`limit`参数，限制提取的个数

## find与find_all的区别
- `find` : 找到第一个满足条件的标签就返回，只会返回一个元素
- `find_all` : 将所有满足条件的标签都返回，会以列表的形式返回很多标签

## find与find_all的过滤条件
- 关键字参数 : 将属性的名字作为关键字参数的名字，以及属性的值作为关键字参数的值进行过滤
- `attrs`参数 : 将属性条件放到一个字典中，传递给`attrs`参数

## 获取标签的属性
- 通过下标获取
    ```python
    href = a['href']
    ```
- 通过`attrs`属性获取
    ```python
    href = a.attrs['href']
    ```

## strings和stripped_strings、string属性以及get_text方法
- `string` : 获取某个标签下的非标签字符串，返回的是字符串,如果这个标签下有多行字符，就不能获取到了
- `strings` : 获取某个标签下的子孙非标签字符串，返回的是生成器
- `stripped_strings` : 获取某个标签下的子孙非标签字符串，会去掉空白字符，返回的是生成器
- `get_text` : 获取某个标签下的子孙非标签字符串，不是以列表的形式返回，返回的是字符串

## BeautifulSoup中使用css选择器
- 在`BeautifulSoup`中要使用css选择器，应该使用`soup.select()`方法
- 需要传递一个css选择器的字符串给select方法

## BeautifulSoup常见的四种类型
- Tag:BeautifulSoup中所有的标签都是Tag类型，并且BeautifulSoup的对象其实本质上也是一个Tag类型，所以其一些方法如find、find_all并不是BeautifulSoup的，而是Tag
- NavagableString:继承自Python中的str,用起来就和使用Python中的str是一样的
- BeautifulSoup:继承自Tag,用来生成BeautifulSoup树的，对于一些查找方法，比如find、select这些，其实还是Tag的
- Comment:继承自NavigableString

## contents和children
- 返回某个标签下的直接子元素，其中也包括字符串，他们的区别是:contents返回的是一个列表，children返回的是一个迭代器