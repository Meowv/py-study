import json
import math
import os
import random
import time
from urllib.parse import parse_qs

import matplotlib.pyplot as plt
import numpy as np
import PIL.Image as Image
import requests
from lxml import etree
from PIL import Image as Image
from wordcloud import ImageColorGenerator, WordCloud

# 接口
URL = 'https://weibo.com/aj/v6/comment/big'

# 文件夹存放路径
img_file_path = os.path.join(os.path.abspath(''), 'images')

# 请求头
HEADERS = {
    'Cookie': 'SINAGLOBAL=2351236110673.731.1559836709873; YF-V5-G0=4358a4493c1ebf8ed493ef9c46f04cae; login_sid_t=41e60bb96e17ec56cfe4d3b3394447b1; cross_origin_proto=SSL; Ugrow-G0=cf25a00b541269674d0feadd72dce35f; WBStorage=edfd723f2928ec64|undefined; _s_tentry=-; wb_view_log=1920*10801; Apache=5556090106616.01.1564629875410; ULV=1564629875415:20:1:1:5556090106616.01.1564629875410:1563863991103; ALF=1596165895; SSOLoginState=1564629896; SUB=_2A25wRivYDeRhGeVN6loY-SjNzj2IHXVTMhoQrDV8PUNbmtBeLRDakW9NTJVf41bJlrWiU9bk6Jp04NN9wmbMSHuw; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W57FpaQRv2BuG4HB3pHDHAp5JpX5KzhUgL.Foe0eKn41KqpSK22dJLoIpqLxK.L1KnLB.qLxKqL1KnL1-9BdGH0; SUHB=0nluYXC48vqhiC; wvr=6; UOR=,,login.sina.com.cn; wb_view_log_3318996151=1920*10801; YF-Page-G0=5161d669e1ac749e79d0f9c1904bc7bf|1564629905|1564629899; webim_unReadCount=%7B%22time%22%3A1564629916506%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22allcountNum%22%3A0%2C%22msgbox%22%3A0%7D'
}

# 获取子评论
def get_child_comment(root_comment_id):
    # 获取子评论所需参数
    comment_params = {
        'ajwvr': 6,
        'more_comment': 'big',
        'is_child_comment': 'true',
        'id': '4367970740108457',
        'from': 'singleWeiBo',
        'last_child_comment_id': '',
        'root_comment_id': '',
        'root_comment_max_id': ''
    }

    comment_params['root_comment_id'] = root_comment_id
    resp = requests.get(URL, params=comment_params, headers=HEADERS)
    print(resp.url)
    resp = json.loads(resp.text)

    if resp['code'] == '100000':
        html = resp['data']['html']
        from lxml import etree
        html = etree.HTML(html)

        # 每个子评论的节点
        data = html.xpath('//div[@class="WB_text"]')

        for i in data:
            nick_name = ''.join(i.xpath('./a/text()')
                                ).strip().replace('\n', '')
            comment = ''.join(i.xpath('./text()')).strip().replace('\n', '')

            write_comment(comment)

            # 获取图片对应的html节点
            pic = i.xpath('.//a[@action-type="widget_photoview"]/@action-data')
            pic = pic[0] if pic else ''

            if pic:
                # 拼接另外两个必要参数
                pic = pic + 'ajwvr=6&uid=5648894345'
                # 构造出一个完整的图片url
                url = 'https://weibo.com/aj/photo/popview?' + pic
                resp = requests.get(url, headers=HEADERS)
                resp = resp.json()
                if resp.get('code') == '100000':
                    url = resp['data']['pic_list'][0]['clear_picSrc']
                    url = 'https:' + url if url else ''
                    # 下载图片
                    download_pic(url, nick_name)
        print("子评论抓取完毕...")

# 写入评论内容
def write_comment(comment_txt):
    comment_txt += '\n'
    with open('comment.txt', 'a', encoding='utf-8') as f:
        f.write(comment_txt.replace('回复', '').replace(
            '等人', '').replace('图片评论', ''))

# 下载图片
def download_pic(url, nick_name):
    if not url:
        return
    if not os.path.exists(img_file_path):
        os.mkdir(img_file_path)
    resp = requests.get(url)
    if resp.status_code == 200:
        with open(img_file_path + f'/{nick_name}.jpg', 'wb') as f:
            f.write(resp.content)

# 获取评论数据
def get_comments():
    # 获取评论数据参数
    params = {
        'ajwvr': 6,
        'id': '4367970740108457',
        'from': 'singleWeiBo',
        'root_comment_max_id': ''
    }

    for page in range(83, 100):
        print(f'~~~~~ 正在读取第 {page + 1} 页 ~~~~~')

        resp = requests.get(URL, params=params, headers=HEADERS)
        print(resp.url)
        resp = json.loads(resp.text)

        if resp['code'] == '100000':
            html = resp['data']['html']
            html = etree.HTML(html)

            max_id_json = html.xpath(
                '//div[@node-type="comment_loading"]/@action-data')[0]

            node_params = parse_qs(max_id_json)

            max_id = node_params['root_comment_max_id'][0]
            params['root_comment_max_id'] = max_id

            data = html.xpath('//div[@node-type="root_comment"]')

            for i in data:
                # 昵称
                nick_name = i.xpath('.//div[@class="WB_text"]/a/text()')[0]

                # 内容
                wb_text = i.xpath('.//div[@class="WB_text"][1]/text()')
                comment_txt = ''.join(wb_text).strip().replace('\n', '')

                write_comment(comment_txt)

                # 评论id 用于获取评论内容
                comment_id = i.xpath('./@comment_id')[0]

                # 评论的图片
                pic_url = i.xpath(
                    './/li[@class="WB_pic S_bg2 bigcursor"]/img/@src')
                pic_url = 'https:' + pic_url[0] if pic_url else ''

                download_pic(pic_url, nick_name)

                # 查看评论
                get_child_comment(root_comment_id=comment_id)

        time.sleep(1)

# 生成图片墙
def denerate_img():
    x = 0
    y = 0
    # 获取pic下 图像列表
    imgs = os.listdir("images")
    random.shuffle(imgs)
    # 创建640*640的图片用于填充各小图片
    newImg = Image.new('RGBA', (2048, 2048))
    # 以640*640来拼接图片，math.sqrt()开平方根计算每张小图片的宽高，
    width = int(math.sqrt(2048 * 2048 / len(imgs)))
    # 每行图片数
    numLine = int(2048 / width)

    for i in imgs:
        if not i.endswith('jpg'):
            continue
        img = Image.open("images/" + i)
        # 缩小图片
        img = img.resize((width, width), Image.ANTIALIAS)
        # 拼接图片，一行排满，换行拼接
        newImg.paste(img, (x * width, y * width))
        x += 1
        if x >= numLine:
            x = 0
            y += 1
    newImg.save("mimi.png")

# 生成词云图
def denerate_img_cloud():
    path = os.getcwd() + '/comment.txt'
    content = open(path, encoding='utf-8').read().replace('图片评论', '').replace('回复', '').replace('等人', '')
    coloring = np.array(Image.open('bg.jpg'))

    wordcloud = WordCloud(background_color="white", max_words=2000, mask=coloring, max_font_size=40, random_state=42,font_path='C:\\Windows\\fonts\\simsun.ttc').generate(content)

    image_colors = ImageColorGenerator(coloring)
    plt.imshow(wordcloud.recolor(color_func=image_colors))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()

if __name__ == "__main__":
    get_comments()
    # denerate_img()
    # denerate_img_cloud()
