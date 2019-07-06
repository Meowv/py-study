import re

# 分组
text = "apple's price $99,orange's price is $10"
ret = re.search('.*(\$\d+).*(\$\d+)', text)
print(ret.group())
print(ret.group(0))
print(ret.group(1))
print(ret.group(2))
print(ret.group(1,2))
# 所有分组都取出来
print(ret.groups())

# find_all函数
text = "apple's price $99,orange's price is $10"
ret = re.findall('\$\d+', text)
print(ret)

# sub函数
text = "apple's price $99,orange's price is $10"
ret = re.sub('\$\d+',"0", text)
print(ret)

html = """
    <dd class="job_bt">
        <h3 class="description">职位描述：</h3>
        <div class="job-detail">
            工作职责:
            <br>岗位职责：
            <br>1、应用数据挖掘、机器学习、自然语言处理技术解决业务中的挑战性问题
            <br>2、参与后端项目工程开发，提供稳定可用的人工智能服务
            <br>3、负责智能问答系统的研发
            <br>4、负责从文本数据中构建知识图谱的研发
            <br>
            <br>
            <br>任职资格:
            <br>任职要求：
            <br>1、计算机、数理统计、机器学习及相关专业本科以上学历，具有相关岗位3年以上工作经验；
            <br>2、熟悉机器学习、NLP领域常见算法与模型，如SVM、CRF、word2vec、LDA、CNN、LSTM等；
            <br>3、熟练使用python，sklearn，numpy，熟悉Linux开发环境；
            <br>4、具有要素提取、句法分析、语义表示、情感分析、意图识别、智能对话、实体链接、词义消歧等项目落地经验优先；
            <br>5、掌握Tensorflow，Keras，PyTorch等深度学习框架优先
        </div>
    </dd>
"""
ret = re.sub('<.+>', "", html)
print(ret)

# split函数
text = 'hello&world wu shuang'
ret = re.split(' |&',text)
print(ret)
ret = re.split('[^a-zA-Z]',text)
print(ret)

# compile函数
text = 'the number is 20.50'
r = re.compile('\d+\.?\d*')
ret = re.search(r, text)
print(ret.group())

r = re.compile(r"""
    \d+ #小数点前面的数字
    \.? #小数点
    \d* # 小数点后面的数字
""", re.VERBOSE)
ret = re.search(r, text)
print(ret.group())