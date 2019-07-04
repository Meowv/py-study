# xpath

## 使用方式
使用//获取整个页面当中的元素，然后写标签名，然后再写谓词进行提取，比如
```xpath
//div[@class='abc']
```

## 知识点
- / 和 // 的区别：/ 代表只获取直接子节点，// 获取子孙节点。视情况而定
- contains：有时候某个属性中包含了多个值，那块可以使用`contains`函数。
    ```xpath
    //div[contains(@class,'abc')]
    ```
- 谓词中的下标是从1开始的，不是0

## 使用lxml解析xml代码
- 解析HTML字符串，使用`lxml.etree.HTML`进行解析
    ```xpath
    htmlElement = etree.HTML(text)
    print(etree.tostring(htmlElement, encoding='utf-8').decode('utf-8'))
    ```
- 解析html文件，使用`lxml.etree.parse`进行解析
    ```xpath
    htmlElement = etree.parse('table.html')
    print(etree.tostring(htmlElement, encoding='utf-8').decode('utf-8'))
    ```
    如果这个函数默认使用的是`XML`解析器，所以碰到一些不规范的`HTML`代码的时候就会解析错误，这时候就要自己创建`HTML`解析器
    ```xpath
    parser = etree.HTMLParser(encoding='utf-8')
    htmlElement = etree.parse('lagou.html', parser=parser)
    print(etree.tostring(htmlElement, encoding='utf-8').decode('utf-8'))
    ```