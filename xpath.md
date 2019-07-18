# xpath

## 使用方式

使用//获取整个页面当中的元素，然后写标签名，然后再写谓词进行提取，比如

```text
//div[@class='abc']
```

## 知识点

* / 和 // 的区别：/ 代表只获取直接子节点，// 获取子孙节点。视情况而定
* contains：有时候某个属性中包含了多个值，那块可以使用`contains`函数。

  ```text
    //div[contains(@class,'abc')]
  ```

* 谓词中的下标是从1开始的，不是0

## 使用lxml解析xml代码

* 解析HTML字符串，使用`lxml.etree.HTML`进行解析

  ```text
    htmlElement = etree.HTML(text)
    print(etree.tostring(htmlElement, encoding='utf-8').decode('utf-8'))
  ```

* 解析html文件，使用`lxml.etree.parse`进行解析

  ```text
    htmlElement = etree.parse('table.html')
    print(etree.tostring(htmlElement, encoding='utf-8').decode('utf-8'))
  ```

    如果这个函数默认使用的是`XML`解析器，所以碰到一些不规范的`HTML`代码的时候就会解析错误，这时候就要自己创建`HTML`解析器

  ```text
    parser = etree.HTMLParser(encoding='utf-8')
    htmlElement = etree.parse('lagou.html', parser=parser)
    print(etree.tostring(htmlElement, encoding='utf-8').decode('utf-8'))
  ```

## lxml结合xpath注意事项

* 使用`xpath`语法，应该使用`Element.xpath`方法来执行xpath的选择，代码如下

  ```python
    trs = html.xpath("//tr[position()>1]")
  ```

    `xpath`函数返回永远是一个列表

* 获取某个标签的属性

  ```python
    html.xpath("//a/@href")
    # 获取a标签的href属性对应的值
  ```

* 获取文本，使用过`xpath`红豆`text()`函数，代码如下
* 在某个标签下执行 xpath函数，获取这个标签下的子孙元素应在 // 之前加一个点`.` 代表在当前元素下获取

  ```python
    txt = tr.xpath("./td[1]//text()")
  ```

