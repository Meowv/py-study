# -*- coding: utf-8 -*-

from xml.parsers.expat import ParserCreate

class DefaultSaxHandler(object):
    def start_element(self,name,attrs):
        print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))

    def end_element(self,name):
        print('sax:end_element:%s' % name)

    def char_data(self,text):
        print('sax:char_data:%s' % text)

xml = r'''<?xml version="1.0" encoding="utf-8"?>
<DOCUMENT>
	<item>
		<key>
			<![CDATA[ 高考 ]]>
		</key>
		<city>
			<![CDATA[ 江苏 ]]>
		</city>
		<display>
			<zh_type>
				<![CDATA[ 查分 ]]>
			</zh_type>
			<zh_year>
				<![CDATA[ 2019 ]]>
			</zh_year>
			<title>
				<![CDATA[ 2019年江苏高考成绩查询时间_优志愿 ]]>
			</title>
			<titleurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</titleurl>
			<mbtitleurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</mbtitleurl>
			<moretxt>
				<![CDATA[ 各地区成绩查询时间 ]]>
			</moretxt>
			<moreurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</moreurl>
			<mbmoreurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</mbmoreurl>
			<showurl>
				<![CDATA[ www.youzy.cn ]]>
			</showurl>
			<table>
				<head>
					<tr>
						<th>
							<text>
								<![CDATA[ 省市 ]]>
							</text>
						</th>
						<th>
							<text>
								<![CDATA[ 查分参考时间 ]]>
							</text>
						</th>
						<th>
							<text>
								<![CDATA[ 查分入口 ]]>
							</text>
						</th>
						<th>
							<text>
								<![CDATA[ 查分电话 ]]>
							</text>
						</th>
					</tr>
				</head>
				<body>
					<tr>
						<td>
							<adapt>
								<name>
									<![CDATA[ 江苏 ]]>
								</name>
							</adapt>
						</td>
						<td>
							<adapt>
								<name>
									<![CDATA[ 6月24日 ]]>
								</name>
							</adapt>
						</td>
						<td>
							<adapt>
								<name>
									<![CDATA[ 江苏教育考试院 ]]>
								</name>
								<link>
									<![CDATA[ http://www.jseea.cn ]]>
								</link>
								<mblink>
									<![CDATA[ http://www.jseea.cn ]]>
								</mblink>
							</adapt>
						</td>
						<td>
							<adapt>
								<name>
									<![CDATA[ 16887799 ]]>
								</name>
							</adapt>
						</td>
					</tr>
				</body>
			</table>
			<source>
				<![CDATA[ 优志愿 ]]>
			</source>
		</display>
	</item>
	<item>
		<key>
			<![CDATA[ 高考 ]]>
		</key>
		<city>
			<![CDATA[ 北京 ]]>
		</city>
		<display>
			<zh_type>
				<![CDATA[ 查分 ]]>
			</zh_type>
			<zh_year>
				<![CDATA[ 2019 ]]>
			</zh_year>
			<title>
				<![CDATA[ 2019年北京高考成绩查询时间_优志愿 ]]>
			</title>
			<titleurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</titleurl>
			<mbtitleurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</mbtitleurl>
			<moretxt>
				<![CDATA[ 各地区成绩查询时间 ]]>
			</moretxt>
			<moreurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</moreurl>
			<mbmoreurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</mbmoreurl>
			<showurl>
				<![CDATA[ www.youzy.cn ]]>
			</showurl>
			<table>
				<head>
					<tr>
						<th>
							<text>
								<![CDATA[ 省市 ]]>
							</text>
						</th>
						<th>
							<text>
								<![CDATA[ 查分参考时间 ]]>
							</text>
						</th>
						<th>
							<text>
								<![CDATA[ 查分入口 ]]>
							</text>
						</th>
						<th>
							<text>
								<![CDATA[ 查分电话 ]]>
							</text>
						</th>
					</tr>
				</head>
				<body>
					<tr>
						<td>
							<adapt>
								<name>
									<![CDATA[ 北京 ]]>
								</name>
							</adapt>
						</td>
						<td>
							<adapt>
								<name>
									<![CDATA[ 6月23日 ]]>
								</name>
							</adapt>
						</td>
						<td>
							<adapt>
								<name>
									<![CDATA[ 北京教育考试院 ]]>
								</name>
								<link>
									<![CDATA[ https://www.bjeea.cn ]]>
								</link>
								<mblink>
									<![CDATA[ https://www.bjeea.cn ]]>
								</mblink>
							</adapt>
						</td>
						<td>
							<adapt>
								<name>
									<![CDATA[ 12580 ]]>
								</name>
							</adapt>
						</td>
					</tr>
				</body>
			</table>
			<source>
				<![CDATA[ 优志愿 ]]>
			</source>
		</display>
	</item>
	<item>
		<key>
			<![CDATA[ 高考 ]]>
		</key>
		<city>
			<![CDATA[ 天津 ]]>
		</city>
		<display>
			<zh_type>
				<![CDATA[ 查分 ]]>
			</zh_type>
			<zh_year>
				<![CDATA[ 2019 ]]>
			</zh_year>
			<title>
				<![CDATA[ 2019年天津高考成绩查询时间_优志愿 ]]>
			</title>
			<titleurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</titleurl>
			<mbtitleurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</mbtitleurl>
			<moretxt>
				<![CDATA[ 各地区成绩查询时间 ]]>
			</moretxt>
			<moreurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</moreurl>
			<mbmoreurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</mbmoreurl>
			<showurl>
				<![CDATA[ www.youzy.cn ]]>
			</showurl>
			<table>
				<head>
					<tr>
						<th>
							<text>
								<![CDATA[ 省市 ]]>
							</text>
						</th>
						<th>
							<text>
								<![CDATA[ 查分参考时间 ]]>
							</text>
						</th>
						<th>
							<text>
								<![CDATA[ 查分入口 ]]>
							</text>
						</th>
					</tr>
				</head>
				<body>
					<tr>
						<td>
							<adapt>
								<name>
									<![CDATA[ 天津 ]]>
								</name>
							</adapt>
						</td>
						<td>
							<adapt>
								<name>
									<![CDATA[ 6月23日 ]]>
								</name>
							</adapt>
						</td>
						<td>
							<adapt>
								<name>
									<![CDATA[ 天津招考资讯网 ]]>
								</name>
								<link>
									<![CDATA[ http://www.zhaokao.net ]]>
								</link>
								<mblink>
									<![CDATA[ http://www.zhaokao.net ]]>
								</mblink>
							</adapt>
						</td>
					</tr>
				</body>
			</table>
			<source>
				<![CDATA[ 优志愿 ]]>
			</source>
		</display>
	</item>
	<item>
		<key>
			<![CDATA[ 高考 ]]>
		</key>
		<city>
			<![CDATA[ 重庆 ]]>
		</city>
		<display>
			<zh_type>
				<![CDATA[ 查分 ]]>
			</zh_type>
			<zh_year>
				<![CDATA[ 2019 ]]>
			</zh_year>
			<title>
				<![CDATA[ 2019年重庆高考成绩查询时间_优志愿 ]]>
			</title>
			<titleurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</titleurl>
			<mbtitleurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</mbtitleurl>
			<moretxt>
				<![CDATA[ 各地区成绩查询时间 ]]>
			</moretxt>
			<moreurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</moreurl>
			<mbmoreurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</mbmoreurl>
			<showurl>
				<![CDATA[ www.youzy.cn ]]>
			</showurl>
			<table>
				<head>
					<tr>
						<th>
							<text>
								<![CDATA[ 省市 ]]>
							</text>
						</th>
						<th>
							<text>
								<![CDATA[ 查分参考时间 ]]>
							</text>
						</th>
						<th>
							<text>
								<![CDATA[ 查分入口 ]]>
							</text>
						</th>
					</tr>
				</head>
				<body>
					<tr>
						<td>
							<adapt>
								<name>
									<![CDATA[ 重庆 ]]>
								</name>
							</adapt>
						</td>
						<td>
							<adapt>
								<name>
									<![CDATA[ 6月23日 ]]>
								</name>
							</adapt>
						</td>
						<td>
							<adapt>
								<name>
									<![CDATA[ 重庆市教育考试院 ]]>
								</name>
								<link>
									<![CDATA[ http://www.cqksy.cn/site/default ]]>
								</link>
								<mblink>
									<![CDATA[ http://www.cqksy.cn/site/default ]]>
								</mblink>
							</adapt>
						</td>
					</tr>
				</body>
			</table>
			<source>
				<![CDATA[ 优志愿 ]]>
			</source>
		</display>
	</item>
	<item>
		<key>
			<![CDATA[ 高考 ]]>
		</key>
		<city>
			<![CDATA[ 广西 ]]>
		</city>
		<display>
			<zh_type>
				<![CDATA[ 查分 ]]>
			</zh_type>
			<zh_year>
				<![CDATA[ 2019 ]]>
			</zh_year>
			<title>
				<![CDATA[ 2019年广西高考成绩查询时间_优志愿 ]]>
			</title>
			<titleurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</titleurl>
			<mbtitleurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</mbtitleurl>
			<moretxt>
				<![CDATA[ 各地区成绩查询时间 ]]>
			</moretxt>
			<moreurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</moreurl>
			<mbmoreurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</mbmoreurl>
			<showurl>
				<![CDATA[ www.youzy.cn ]]>
			</showurl>
			<table>
				<head>
					<tr>
						<th>
							<text>
								<![CDATA[ 省市 ]]>
							</text>
						</th>
						<th>
							<text>
								<![CDATA[ 查分参考时间 ]]>
							</text>
						</th>
						<th>
							<text>
								<![CDATA[ 查分入口 ]]>
							</text>
						</th>
						<th>
							<text>
								<![CDATA[ 查分电话 ]]>
							</text>
						</th>
					</tr>
				</head>
				<body>
					<tr>
						<td>
							<adapt>
								<name>
									<![CDATA[ 广西 ]]>
								</name>
							</adapt>
						</td>
						<td>
							<adapt>
								<name>
									<![CDATA[ 6月23日 ]]>
								</name>
							</adapt>
						</td>
						<td>
							<adapt>
								<name>
									<![CDATA[ 广西招生考试院 ]]>
								</name>
								<link>
									<![CDATA[ http://www.gxeea.cn ]]>
								</link>
								<mblink>
									<![CDATA[ http://www.gxeea.cn ]]>
								</mblink>
							</adapt>
						</td>
						<td>
							<adapt>
								<name>
									<![CDATA[ 114 ]]>
								</name>
							</adapt>
						</td>
					</tr>
				</body>
			</table>
			<source>
				<![CDATA[ 优志愿 ]]>
			</source>
		</display>
	</item>
	<item>
		<key>
			<![CDATA[ 高考 ]]>
		</key>
		<city>
			<![CDATA[ 宁夏 ]]>
		</city>
		<display>
			<zh_type>
				<![CDATA[ 查分 ]]>
			</zh_type>
			<zh_year>
				<![CDATA[ 2019 ]]>
			</zh_year>
			<title>
				<![CDATA[ 2019年宁夏高考成绩查询时间_优志愿 ]]>
			</title>
			<titleurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</titleurl>
			<mbtitleurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</mbtitleurl>
			<moretxt>
				<![CDATA[ 各地区成绩查询时间 ]]>
			</moretxt>
			<moreurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</moreurl>
			<mbmoreurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</mbmoreurl>
			<showurl>
				<![CDATA[ www.youzy.cn ]]>
			</showurl>
			<table>
				<head>
					<tr>
						<th>
							<text>
								<![CDATA[ 省市 ]]>
							</text>
						</th>
						<th>
							<text>
								<![CDATA[ 查分参考时间 ]]>
							</text>
						</th>
						<th>
							<text>
								<![CDATA[ 查分入口 ]]>
							</text>
						</th>
					</tr>
				</head>
				<body>
					<tr>
						<td>
							<adapt>
								<name>
									<![CDATA[ 宁夏 ]]>
								</name>
							</adapt>
						</td>
						<td>
							<adapt>
								<name>
									<![CDATA[ 6月23日 ]]>
								</name>
							</adapt>
						</td>
						<td>
							<adapt>
								<name>
									<![CDATA[ 宁夏教育考试院 ]]>
								</name>
								<link>
									<![CDATA[ https://www.nxjyks.cn ]]>
								</link>
								<mblink>
									<![CDATA[ https://www.nxjyks.cn ]]>
								</mblink>
							</adapt>
						</td>
					</tr>
				</body>
			</table>
			<source>
				<![CDATA[ 优志愿 ]]>
			</source>
		</display>
	</item>
	<item>
		<key>
			<![CDATA[ 高考 ]]>
		</key>
		<city>
			<![CDATA[ 四川 ]]>
		</city>
		<display>
			<zh_type>
				<![CDATA[ 查分 ]]>
			</zh_type>
			<zh_year>
				<![CDATA[ 2019 ]]>
			</zh_year>
			<title>
				<![CDATA[ 2019年四川高考成绩查询时间_优志愿 ]]>
			</title>
			<titleurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</titleurl>
			<mbtitleurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</mbtitleurl>
			<moretxt>
				<![CDATA[ 各地区成绩查询时间 ]]>
			</moretxt>
			<moreurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</moreurl>
			<mbmoreurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</mbmoreurl>
			<showurl>
				<![CDATA[ www.youzy.cn ]]>
			</showurl>
			<table>
				<head>
					<tr>
						<th>
							<text>
								<![CDATA[ 省市 ]]>
							</text>
						</th>
						<th>
							<text>
								<![CDATA[ 查分参考时间 ]]>
							</text>
						</th>
						<th>
							<text>
								<![CDATA[ 查分入口 ]]>
							</text>
						</th>
					</tr>
				</head>
				<body>
					<tr>
						<td>
							<adapt>
								<name>
									<![CDATA[ 四川 ]]>
								</name>
							</adapt>
						</td>
						<td>
							<adapt>
								<name>
									<![CDATA[ 6月22日 ]]>
								</name>
							</adapt>
						</td>
						<td>
							<adapt>
								<name>
									<![CDATA[ 四川省教育考试院 ]]>
								</name>
								<link>
									<![CDATA[ http://www.sceea.cn ]]>
								</link>
								<mblink>
									<![CDATA[ http://www.sceea.cn ]]>
								</mblink>
							</adapt>
						</td>
					</tr>
				</body>
			</table>
			<source>
				<![CDATA[ 优志愿 ]]>
			</source>
		</display>
	</item>
	<item>
		<key>
			<![CDATA[ 高考 ]]>
		</key>
		<city>
			<![CDATA[ 江西 ]]>
		</city>
		<display>
			<zh_type>
				<![CDATA[ 查分 ]]>
			</zh_type>
			<zh_year>
				<![CDATA[ 2019 ]]>
			</zh_year>
			<title>
				<![CDATA[ 2019年江西高考成绩查询时间_优志愿 ]]>
			</title>
			<titleurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</titleurl>
			<mbtitleurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</mbtitleurl>
			<moretxt>
				<![CDATA[ 各地区成绩查询时间 ]]>
			</moretxt>
			<moreurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</moreurl>
			<mbmoreurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</mbmoreurl>
			<showurl>
				<![CDATA[ www.youzy.cn ]]>
			</showurl>
			<table>
				<head>
					<tr>
						<th>
							<text>
								<![CDATA[ 省市 ]]>
							</text>
						</th>
						<th>
							<text>
								<![CDATA[ 查分参考时间 ]]>
							</text>
						</th>
						<th>
							<text>
								<![CDATA[ 查分入口 ]]>
							</text>
						</th>
					</tr>
				</head>
				<body>
					<tr>
						<td>
							<adapt>
								<name>
									<![CDATA[ 江西 ]]>
								</name>
							</adapt>
						</td>
						<td>
							<adapt>
								<name>
									<![CDATA[ 6月23日 ]]>
								</name>
							</adapt>
						</td>
						<td>
							<adapt>
								<name>
									<![CDATA[ 江西省教育考试院 ]]>
								</name>
								<link>
									<![CDATA[ http://www.jxeea.cn ]]>
								</link>
								<mblink>
									<![CDATA[ http://www.jxeea.cn ]]>
								</mblink>
							</adapt>
						</td>
					</tr>
				</body>
			</table>
			<source>
				<![CDATA[ 优志愿 ]]>
			</source>
		</display>
	</item>
	<item>
		<key>
			<![CDATA[ 高考 ]]>
		</key>
		<city>
			<![CDATA[ 浙江 ]]>
		</city>
		<display>
			<zh_type>
				<![CDATA[ 查分 ]]>
			</zh_type>
			<zh_year>
				<![CDATA[ 2019 ]]>
			</zh_year>
			<title>
				<![CDATA[ 2019年浙江高考成绩查询时间_优志愿 ]]>
			</title>
			<titleurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</titleurl>
			<mbtitleurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</mbtitleurl>
			<moretxt>
				<![CDATA[ 各地区成绩查询时间 ]]>
			</moretxt>
			<moreurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</moreurl>
			<mbmoreurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</mbmoreurl>
			<showurl>
				<![CDATA[ www.youzy.cn ]]>
			</showurl>
			<table>
				<head>
					<tr>
						<th>
							<text>
								<![CDATA[ 省市 ]]>
							</text>
						</th>
						<th>
							<text>
								<![CDATA[ 查分参考时间 ]]>
							</text>
						</th>
						<th>
							<text>
								<![CDATA[ 查分入口 ]]>
							</text>
						</th>
					</tr>
				</head>
				<body>
					<tr>
						<td>
							<adapt>
								<name>
									<![CDATA[ 浙江 ]]>
								</name>
							</adapt>
						</td>
						<td>
							<adapt>
								<name>
									<![CDATA[ 6月22日 ]]>
								</name>
							</adapt>
						</td>
						<td>
							<adapt>
								<name>
									<![CDATA[ 浙江教育考试院 ]]>
								</name>
								<link>
									<![CDATA[ https://www.zjzs.net ]]>
								</link>
								<mblink>
									<![CDATA[ https://www.zjzs.net ]]>
								</mblink>
							</adapt>
						</td>
					</tr>
				</body>
			</table>
			<source>
				<![CDATA[ 优志愿 ]]>
			</source>
		</display>
	</item>
	<item>
		<key>
			<![CDATA[ 高考 ]]>
		</key>
		<city>
			<![CDATA[ 新疆 ]]>
		</city>
		<display>
			<zh_type>
				<![CDATA[ 查分 ]]>
			</zh_type>
			<zh_year>
				<![CDATA[ 2019 ]]>
			</zh_year>
			<title>
				<![CDATA[ 2019年新疆高考成绩查询时间_优志愿 ]]>
			</title>
			<titleurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</titleurl>
			<mbtitleurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</mbtitleurl>
			<moretxt>
				<![CDATA[ 各地区成绩查询时间 ]]>
			</moretxt>
			<moreurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</moreurl>
			<mbmoreurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</mbmoreurl>
			<showurl>
				<![CDATA[ www.youzy.cn ]]>
			</showurl>
			<table>
				<head>
					<tr>
						<th>
							<text>
								<![CDATA[ 省市 ]]>
							</text>
						</th>
						<th>
							<text>
								<![CDATA[ 查分参考时间 ]]>
							</text>
						</th>
						<th>
							<text>
								<![CDATA[ 查分入口 ]]>
							</text>
						</th>
					</tr>
				</head>
				<body>
					<tr>
						<td>
							<adapt>
								<name>
									<![CDATA[ 新疆 ]]>
								</name>
							</adapt>
						</td>
						<td>
							<adapt>
								<name>
									<![CDATA[ 6月24日 ]]>
								</name>
							</adapt>
						</td>
						<td>
							<adapt>
								<name>
									<![CDATA[ 新疆招生网 ]]>
								</name>
								<link>
									<![CDATA[ http://www.xjzk.gov.cn ]]>
								</link>
								<mblink>
									<![CDATA[ http://www.xjzk.gov.cn ]]>
								</mblink>
							</adapt>
						</td>
					</tr>
				</body>
			</table>
			<source>
				<![CDATA[ 优志愿 ]]>
			</source>
		</display>
	</item>
	<item>
		<key>
			<![CDATA[ 高考 ]]>
		</key>
		<city>
			<![CDATA[ 河南 ]]>
		</city>
		<display>
			<zh_type>
				<![CDATA[ 查分 ]]>
			</zh_type>
			<zh_year>
				<![CDATA[ 2019 ]]>
			</zh_year>
			<title>
				<![CDATA[ 2019年河南高考成绩查询时间_优志愿 ]]>
			</title>
			<titleurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</titleurl>
			<mbtitleurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</mbtitleurl>
			<moretxt>
				<![CDATA[ 各地区成绩查询时间 ]]>
			</moretxt>
			<moreurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</moreurl>
			<mbmoreurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</mbmoreurl>
			<showurl>
				<![CDATA[ www.youzy.cn ]]>
			</showurl>
			<table>
				<head>
					<tr>
						<th>
							<text>
								<![CDATA[ 省市 ]]>
							</text>
						</th>
						<th>
							<text>
								<![CDATA[ 查分参考时间 ]]>
							</text>
						</th>
						<th>
							<text>
								<![CDATA[ 查分入口 ]]>
							</text>
						</th>
					</tr>
				</head>
				<body>
					<tr>
						<td>
							<adapt>
								<name>
									<![CDATA[ 河南 ]]>
								</name>
							</adapt>
						</td>
						<td>
							<adapt>
								<name>
									<![CDATA[ 6月25日零时 ]]>
								</name>
							</adapt>
						</td>
						<td>
							<adapt>
								<name>
									<![CDATA[ 河南省招生办公室 ]]>
								</name>
								<link>
									<![CDATA[ http://www.heao.gov.cn ]]>
								</link>
								<mblink>
									<![CDATA[ http://www.heao.gov.cn ]]>
								</mblink>
							</adapt>
						</td>
					</tr>
				</body>
			</table>
			<source>
				<![CDATA[ 优志愿 ]]>
			</source>
		</display>
	</item>
	<item>
		<key>
			<![CDATA[ 高考 ]]>
		</key>
		<city>
			<![CDATA[ 辽宁 ]]>
		</city>
		<display>
			<zh_type>
				<![CDATA[ 查分 ]]>
			</zh_type>
			<zh_year>
				<![CDATA[ 2019 ]]>
			</zh_year>
			<title>
				<![CDATA[ 2019年辽宁高考成绩查询时间_优志愿 ]]>
			</title>
			<titleurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</titleurl>
			<mbtitleurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</mbtitleurl>
			<moretxt>
				<![CDATA[ 各地区成绩查询时间 ]]>
			</moretxt>
			<moreurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</moreurl>
			<mbmoreurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</mbmoreurl>
			<showurl>
				<![CDATA[ www.youzy.cn ]]>
			</showurl>
			<table>
				<head>
					<tr>
						<th>
							<text>
								<![CDATA[ 省市 ]]>
							</text>
						</th>
						<th>
							<text>
								<![CDATA[ 查分参考时间 ]]>
							</text>
						</th>
						<th>
							<text>
								<![CDATA[ 查分入口 ]]>
							</text>
						</th>
					</tr>
				</head>
				<body>
					<tr>
						<td>
							<adapt>
								<name>
									<![CDATA[ 辽宁 ]]>
								</name>
							</adapt>
						</td>
						<td>
							<adapt>
								<name>
									<![CDATA[ 6月23日 ]]>
								</name>
							</adapt>
						</td>
						<td>
							<adapt>
								<name>
									<![CDATA[ 辽宁招生考试之窗 ]]>
								</name>
								<link>
									<![CDATA[ http://www.lnzsks.com ]]>
								</link>
								<mblink>
									<![CDATA[ http://www.lnzsks.com ]]>
								</mblink>
							</adapt>
						</td>
					</tr>
				</body>
			</table>
			<source>
				<![CDATA[ 优志愿 ]]>
			</source>
		</display>
	</item>
	<item>
		<key>
			<![CDATA[ 高考 ]]>
		</key>
		<city>
			<![CDATA[ 湖北 ]]>
		</city>
		<display>
			<zh_type>
				<![CDATA[ 查分 ]]>
			</zh_type>
			<zh_year>
				<![CDATA[ 2019 ]]>
			</zh_year>
			<title>
				<![CDATA[ 2019年湖北高考成绩查询时间_优志愿 ]]>
			</title>
			<titleurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</titleurl>
			<mbtitleurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</mbtitleurl>
			<moretxt>
				<![CDATA[ 各地区成绩查询时间 ]]>
			</moretxt>
			<moreurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</moreurl>
			<mbmoreurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</mbmoreurl>
			<showurl>
				<![CDATA[ www.youzy.cn ]]>
			</showurl>
			<table>
				<head>
					<tr>
						<th>
							<text>
								<![CDATA[ 省市 ]]>
							</text>
						</th>
						<th>
							<text>
								<![CDATA[ 查分参考时间 ]]>
							</text>
						</th>
						<th>
							<text>
								<![CDATA[ 查分入口 ]]>
							</text>
						</th>
					</tr>
				</head>
				<body>
					<tr>
						<td>
							<adapt>
								<name>
									<![CDATA[ 湖北 ]]>
								</name>
							</adapt>
						</td>
						<td>
							<adapt>
								<name>
									<![CDATA[ 6月23日 ]]>
								</name>
							</adapt>
						</td>
						<td>
							<adapt>
								<name>
									<![CDATA[ 湖北招生考试网 ]]>
								</name>
								<link>
									<![CDATA[ http://www.hbksw.com ]]>
								</link>
								<mblink>
									<![CDATA[ http://www.hbksw.com ]]>
								</mblink>
							</adapt>
						</td>
					</tr>
				</body>
			</table>
			<source>
				<![CDATA[ 优志愿 ]]>
			</source>
		</display>
	</item>
	<item>
		<key>
			<![CDATA[ 高考 ]]>
		</key>
		<city>
			<![CDATA[ 黑龙江 ]]>
		</city>
		<display>
			<zh_type>
				<![CDATA[ 查分 ]]>
			</zh_type>
			<zh_year>
				<![CDATA[ 2019 ]]>
			</zh_year>
			<title>
				<![CDATA[ 2019年黑龙江高考成绩查询时间_优志愿 ]]>
			</title>
			<titleurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</titleurl>
			<mbtitleurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</mbtitleurl>
			<moretxt>
				<![CDATA[ 各地区成绩查询时间 ]]>
			</moretxt>
			<moreurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</moreurl>
			<mbmoreurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</mbmoreurl>
			<showurl>
				<![CDATA[ www.youzy.cn ]]>
			</showurl>
			<table>
				<head>
					<tr>
						<th>
							<text>
								<![CDATA[ 省市 ]]>
							</text>
						</th>
						<th>
							<text>
								<![CDATA[ 查分参考时间 ]]>
							</text>
						</th>
						<th>
							<text>
								<![CDATA[ 查分入口 ]]>
							</text>
						</th>
					</tr>
				</head>
				<body>
					<tr>
						<td>
							<adapt>
								<name>
									<![CDATA[ 黑龙江 ]]>
								</name>
							</adapt>
						</td>
						<td>
							<adapt>
								<name>
									<![CDATA[ 6月24日 ]]>
								</name>
							</adapt>
						</td>
						<td>
							<adapt>
								<name>
									<![CDATA[ 黑龙江招生考试信息港 ]]>
								</name>
								<link>
									<![CDATA[ http://www.lzk.hl.cn ]]>
								</link>
								<mblink>
									<![CDATA[ http://www.lzk.hl.cn ]]>
								</mblink>
							</adapt>
						</td>
					</tr>
				</body>
			</table>
			<source>
				<![CDATA[ 优志愿 ]]>
			</source>
		</display>
	</item>
	<item>
		<key>
			<![CDATA[ 高考 ]]>
		</key>
		<city>
			<![CDATA[ 吉林 ]]>
		</city>
		<display>
			<zh_type>
				<![CDATA[ 查分 ]]>
			</zh_type>
			<zh_year>
				<![CDATA[ 2019 ]]>
			</zh_year>
			<title>
				<![CDATA[ 2019年吉林高考成绩查询时间_优志愿 ]]>
			</title>
			<titleurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</titleurl>
			<mbtitleurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</mbtitleurl>
			<moretxt>
				<![CDATA[ 各地区成绩查询时间 ]]>
			</moretxt>
			<moreurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</moreurl>
			<mbmoreurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</mbmoreurl>
			<showurl>
				<![CDATA[ www.youzy.cn ]]>
			</showurl>
			<table>
				<head>
					<tr>
						<th>
							<text>
								<![CDATA[ 省市 ]]>
							</text>
						</th>
						<th>
							<text>
								<![CDATA[ 查分参考时间 ]]>
							</text>
						</th>
						<th>
							<text>
								<![CDATA[ 查分入口 ]]>
							</text>
						</th>
					</tr>
				</head>
				<body>
					<tr>
						<td>
							<adapt>
								<name>
									<![CDATA[ 吉林 ]]>
								</name>
							</adapt>
						</td>
						<td>
							<adapt>
								<name>
									<![CDATA[ 6月23日 ]]>
								</name>
							</adapt>
						</td>
						<td>
							<adapt>
								<name>
									<![CDATA[ 吉林省教育信息网 ]]>
								</name>
								<link>
									<![CDATA[ http://www.jlipedu.cn ]]>
								</link>
								<mblink>
									<![CDATA[ http://www.jlipedu.cn ]]>
								</mblink>
							</adapt>
						</td>
					</tr>
				</body>
			</table>
			<source>
				<![CDATA[ 优志愿 ]]>
			</source>
		</display>
	</item>
	<item>
		<key>
			<![CDATA[ 高考 ]]>
		</key>
		<city>
			<![CDATA[ 上海 ]]>
		</city>
		<display>
			<zh_type>
				<![CDATA[ 查分 ]]>
			</zh_type>
			<zh_year>
				<![CDATA[ 2019 ]]>
			</zh_year>
			<title>
				<![CDATA[ 2019年上海高考成绩查询时间_优志愿 ]]>
			</title>
			<titleurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</titleurl>
			<mbtitleurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</mbtitleurl>
			<moretxt>
				<![CDATA[ 各地区成绩查询时间 ]]>
			</moretxt>
			<moreurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</moreurl>
			<mbmoreurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</mbmoreurl>
			<showurl>
				<![CDATA[ www.youzy.cn ]]>
			</showurl>
			<table>
				<head>
					<tr>
						<th>
							<text>
								<![CDATA[ 省市 ]]>
							</text>
						</th>
						<th>
							<text>
								<![CDATA[ 查分参考时间 ]]>
							</text>
						</th>
						<th>
							<text>
								<![CDATA[ 查分入口 ]]>
							</text>
						</th>
					</tr>
				</head>
				<body>
					<tr>
						<td>
							<adapt>
								<name>
									<![CDATA[ 上海 ]]>
								</name>
							</adapt>
						</td>
						<td>
							<adapt>
								<name>
									<![CDATA[ 6月23日 20:00  ]]>
								</name>
							</adapt>
						</td>
						<td>
							<adapt>
								<name>
									<![CDATA[ 上海招考热线 ]]>
								</name>
								<link>
									<![CDATA[ http://www.shmeea.edu.cn ]]>
								</link>
								<mblink>
									<![CDATA[ http://www.shmeea.edu.cn ]]>
								</mblink>
							</adapt>
						</td>
					</tr>
				</body>
			</table>
			<source>
				<![CDATA[ 优志愿 ]]>
			</source>
		</display>
	</item>
	<item>
		<key>
			<![CDATA[ 高考 ]]>
		</key>
		<city>
			<![CDATA[ 广东 ]]>
		</city>
		<display>
			<zh_type>
				<![CDATA[ 查分 ]]>
			</zh_type>
			<zh_year>
				<![CDATA[ 2019 ]]>
			</zh_year>
			<title>
				<![CDATA[ 2019年广东高考成绩查询时间_优志愿 ]]>
			</title>
			<titleurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</titleurl>
			<mbtitleurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</mbtitleurl>
			<moretxt>
				<![CDATA[ 各地区成绩查询时间 ]]>
			</moretxt>
			<moreurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</moreurl>
			<mbmoreurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</mbmoreurl>
			<showurl>
				<![CDATA[ www.youzy.cn ]]>
			</showurl>
			<table>
				<head>
					<tr>
						<th>
							<text>
								<![CDATA[ 省市 ]]>
							</text>
						</th>
						<th>
							<text>
								<![CDATA[ 查分参考时间 ]]>
							</text>
						</th>
						<th>
							<text>
								<![CDATA[ 查分入口 ]]>
							</text>
						</th>
					</tr>
				</head>
				<body>
					<tr>
						<td>
							<adapt>
								<name>
									<![CDATA[ 广东 ]]>
								</name>
							</adapt>
						</td>
						<td>
							<adapt>
								<name>
									<![CDATA[ 6月25日 ]]>
								</name>
							</adapt>
						</td>
						<td>
							<adapt>
								<name>
									<![CDATA[ 广东教育考试院 ]]>
								</name>
								<link>
									<![CDATA[ http://eea.gd.gov.cn ]]>
								</link>
								<mblink>
									<![CDATA[ http://eea.gd.gov.cn ]]>
								</mblink>
							</adapt>
						</td>
					</tr>
				</body>
			</table>
			<source>
				<![CDATA[ 优志愿 ]]>
			</source>
		</display>
	</item>
	<item>
		<key>
			<![CDATA[ 高考 ]]>
		</key>
		<city>
			<![CDATA[ 河北 ]]>
		</city>
		<display>
			<zh_type>
				<![CDATA[ 查分 ]]>
			</zh_type>
			<zh_year>
				<![CDATA[ 2019 ]]>
			</zh_year>
			<title>
				<![CDATA[ 2019年河北高考成绩查询时间_优志愿 ]]>
			</title>
			<titleurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</titleurl>
			<mbtitleurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</mbtitleurl>
			<moretxt>
				<![CDATA[ 各地区成绩查询时间 ]]>
			</moretxt>
			<moreurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</moreurl>
			<mbmoreurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</mbmoreurl>
			<showurl>
				<![CDATA[ www.youzy.cn ]]>
			</showurl>
			<table>
				<head>
					<tr>
						<th>
							<text>
								<![CDATA[ 省市 ]]>
							</text>
						</th>
						<th>
							<text>
								<![CDATA[ 查分参考时间 ]]>
							</text>
						</th>
						<th>
							<text>
								<![CDATA[ 查分入口 ]]>
							</text>
						</th>
					</tr>
				</head>
				<body>
					<tr>
						<td>
							<adapt>
								<name>
									<![CDATA[ 河北 ]]>
								</name>
							</adapt>
						</td>
						<td>
							<adapt>
								<name>
									<![CDATA[ 6月23日 ]]>
								</name>
							</adapt>
						</td>
						<td>
							<adapt>
								<name>
									<![CDATA[ 河北省教育考试院 ]]>
								</name>
								<link>
									<![CDATA[ http://www.hebeea.edu.cn ]]>
								</link>
								<mblink>
									<![CDATA[ http://www.hebeea.edu.cn ]]>
								</mblink>
							</adapt>
						</td>
					</tr>
				</body>
			</table>
			<source>
				<![CDATA[ 优志愿 ]]>
			</source>
		</display>
	</item>
	<item>
		<key>
			<![CDATA[ 高考 ]]>
		</key>
		<city>
			<![CDATA[ 福建 ]]>
		</city>
		<display>
			<zh_type>
				<![CDATA[ 查分 ]]>
			</zh_type>
			<zh_year>
				<![CDATA[ 2019 ]]>
			</zh_year>
			<title>
				<![CDATA[ 2019年福建高考成绩查询时间_优志愿 ]]>
			</title>
			<titleurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</titleurl>
			<mbtitleurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</mbtitleurl>
			<moretxt>
				<![CDATA[ 各地区成绩查询时间 ]]>
			</moretxt>
			<moreurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</moreurl>
			<mbmoreurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</mbmoreurl>
			<showurl>
				<![CDATA[ www.youzy.cn ]]>
			</showurl>
			<table>
				<head>
					<tr>
						<th>
							<text>
								<![CDATA[ 省市 ]]>
							</text>
						</th>
						<th>
							<text>
								<![CDATA[ 查分参考时间 ]]>
							</text>
						</th>
						<th>
							<text>
								<![CDATA[ 查分入口 ]]>
							</text>
						</th>
					</tr>
				</head>
				<body>
					<tr>
						<td>
							<adapt>
								<name>
									<![CDATA[ 福建 ]]>
								</name>
							</adapt>
						</td>
						<td>
							<adapt>
								<name>
									<![CDATA[ 6月24日 ]]>
								</name>
							</adapt>
						</td>
						<td>
							<adapt>
								<name>
									<![CDATA[ 福建省教育考试院 ]]>
								</name>
								<link>
									<![CDATA[ http://www.eeafj.cn ]]>
								</link>
								<mblink>
									<![CDATA[ http://www.eeafj.cn ]]>
								</mblink>
							</adapt>
						</td>
					</tr>
				</body>
			</table>
			<source>
				<![CDATA[ 优志愿 ]]>
			</source>
		</display>
	</item>
	<item>
		<key>
			<![CDATA[ 高考 ]]>
		</key>
		<city>
			<![CDATA[ 安徽 ]]>
		</city>
		<display>
			<zh_type>
				<![CDATA[ 查分 ]]>
			</zh_type>
			<zh_year>
				<![CDATA[ 2019 ]]>
			</zh_year>
			<title>
				<![CDATA[ 2019年安徽高考成绩查询时间_优志愿 ]]>
			</title>
			<titleurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</titleurl>
			<mbtitleurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</mbtitleurl>
			<moretxt>
				<![CDATA[ 各地区成绩查询时间 ]]>
			</moretxt>
			<moreurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</moreurl>
			<mbmoreurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</mbmoreurl>
			<showurl>
				<![CDATA[ www.youzy.cn ]]>
			</showurl>
			<table>
				<head>
					<tr>
						<th>
							<text>
								<![CDATA[ 省市 ]]>
							</text>
						</th>
						<th>
							<text>
								<![CDATA[ 查分参考时间 ]]>
							</text>
						</th>
						<th>
							<text>
								<![CDATA[ 查分入口 ]]>
							</text>
						</th>
					</tr>
				</head>
				<body>
					<tr>
						<td>
							<adapt>
								<name>
									<![CDATA[ 安徽 ]]>
								</name>
							</adapt>
						</td>
						<td>
							<adapt>
								<name>
									<![CDATA[ 6月24日 ]]>
								</name>
							</adapt>
						</td>
						<td>
							<adapt>
								<name>
									<![CDATA[ 安徽招生考试院 ]]>
								</name>
								<link>
									<![CDATA[ http://cx.ahzsks.cn ]]>
								</link>
								<mblink>
									<![CDATA[ http://cx.ahzsks.cn ]]>
								</mblink>
							</adapt>
						</td>
					</tr>
				</body>
			</table>
			<source>
				<![CDATA[ 优志愿 ]]>
			</source>
		</display>
	</item>
	<item>
		<key>
			<![CDATA[ 高考 ]]>
		</key>
		<city>
			<![CDATA[ 山东 ]]>
		</city>
		<display>
			<zh_type>
				<![CDATA[ 查分 ]]>
			</zh_type>
			<zh_year>
				<![CDATA[ 2019 ]]>
			</zh_year>
			<title>
				<![CDATA[ 2019年山东高考成绩查询时间_优志愿 ]]>
			</title>
			<titleurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</titleurl>
			<mbtitleurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</mbtitleurl>
			<moretxt>
				<![CDATA[ 各地区成绩查询时间 ]]>
			</moretxt>
			<moreurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</moreurl>
			<mbmoreurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</mbmoreurl>
			<showurl>
				<![CDATA[ www.youzy.cn ]]>
			</showurl>
			<table>
				<head>
					<tr>
						<th>
							<text>
								<![CDATA[ 省市 ]]>
							</text>
						</th>
						<th>
							<text>
								<![CDATA[ 查分参考时间 ]]>
							</text>
						</th>
						<th>
							<text>
								<![CDATA[ 查分入口 ]]>
							</text>
						</th>
						<th>
							<text>
								<![CDATA[ 查分电话 ]]>
							</text>
						</th>
					</tr>
				</head>
				<body>
					<tr>
						<td>
							<adapt>
								<name>
									<![CDATA[ 山东 ]]>
								</name>
							</adapt>
						</td>
						<td>
							<adapt>
								<name>
									<![CDATA[ 6月24日 ]]>
								</name>
							</adapt>
						</td>
						<td>
							<adapt>
								<name>
									<![CDATA[ 山东省教育招生考试院 ]]>
								</name>
								<link>
									<![CDATA[ http://www.sdzk.cn ]]>
								</link>
								<mblink>
									<![CDATA[ http://www.sdzk.cn ]]>
								</mblink>
							</adapt>
						</td>
						<td>
							<adapt>
								<name>
									<![CDATA[ 16866 ]]>
								</name>
							</adapt>
						</td>
					</tr>
				</body>
			</table>
			<source>
				<![CDATA[ 优志愿 ]]>
			</source>
		</display>
	</item>
	<item>
		<key>
			<![CDATA[ 高考 ]]>
		</key>
		<city>
			<![CDATA[ 湖南 ]]>
		</city>
		<display>
			<zh_type>
				<![CDATA[ 查分 ]]>
			</zh_type>
			<zh_year>
				<![CDATA[ 2019 ]]>
			</zh_year>
			<title>
				<![CDATA[ 2019年湖南高考成绩查询时间_优志愿 ]]>
			</title>
			<titleurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</titleurl>
			<mbtitleurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</mbtitleurl>
			<moretxt>
				<![CDATA[ 各地区成绩查询时间 ]]>
			</moretxt>
			<moreurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</moreurl>
			<mbmoreurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</mbmoreurl>
			<showurl>
				<![CDATA[ www.youzy.cn ]]>
			</showurl>
			<table>
				<head>
					<tr>
						<th>
							<text>
								<![CDATA[ 省市 ]]>
							</text>
						</th>
						<th>
							<text>
								<![CDATA[ 查分参考时间 ]]>
							</text>
						</th>
						<th>
							<text>
								<![CDATA[ 查分入口 ]]>
							</text>
						</th>
						<th>
							<text>
								<![CDATA[ 查分电话 ]]>
							</text>
						</th>
					</tr>
				</head>
				<body>
					<tr>
						<td>
							<adapt>
								<name>
									<![CDATA[ 湖南 ]]>
								</name>
							</adapt>
						</td>
						<td>
							<adapt>
								<name>
									<![CDATA[ 6月25日 ]]>
								</name>
							</adapt>
						</td>
						<td>
							<adapt>
								<name>
									<![CDATA[ 湖南教育考试院 ]]>
								</name>
								<link>
									<![CDATA[ http://www.hneao.edu.cn/ ]]>
								</link>
								<mblink>
									<![CDATA[ http://www.hneao.edu.cn/ ]]>
								</mblink>
							</adapt>
						</td>
						<td>
							<adapt>
								<name>
									<![CDATA[ 16885168 ]]>
								</name>
							</adapt>
						</td>
					</tr>
				</body>
			</table>
			<source>
				<![CDATA[ 优志愿 ]]>
			</source>
		</display>
	</item>
	<item>
		<key>
			<![CDATA[ 高考 ]]>
		</key>
		<city>
			<![CDATA[ 陕西 ]]>
		</city>
		<display>
			<zh_type>
				<![CDATA[ 查分 ]]>
			</zh_type>
			<zh_year>
				<![CDATA[ 2019 ]]>
			</zh_year>
			<title>
				<![CDATA[ 2019年陕西高考成绩查询时间_优志愿 ]]>
			</title>
			<titleurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</titleurl>
			<mbtitleurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</mbtitleurl>
			<moretxt>
				<![CDATA[ 各地区成绩查询时间 ]]>
			</moretxt>
			<moreurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</moreurl>
			<mbmoreurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</mbmoreurl>
			<showurl>
				<![CDATA[ www.youzy.cn ]]>
			</showurl>
			<table>
				<head>
					<tr>
						<th>
							<text>
								<![CDATA[ 省市 ]]>
							</text>
						</th>
						<th>
							<text>
								<![CDATA[ 查分参考时间 ]]>
							</text>
						</th>
						<th>
							<text>
								<![CDATA[ 查分入口 ]]>
							</text>
						</th>
					</tr>
				</head>
				<body>
					<tr>
						<td>
							<adapt>
								<name>
									<![CDATA[ 陕西 ]]>
								</name>
							</adapt>
						</td>
						<td>
							<adapt>
								<name>
									<![CDATA[ 6月24日 ]]>
								</name>
							</adapt>
						</td>
						<td>
							<adapt>
								<name>
									<![CDATA[ 陕西招生考试信息网 ]]>
								</name>
								<link>
									<![CDATA[ http://www.sneac.com ]]>
								</link>
								<mblink>
									<![CDATA[ http://www.sneac.com ]]>
								</mblink>
							</adapt>
						</td>
					</tr>
				</body>
			</table>
			<source>
				<![CDATA[ 优志愿 ]]>
			</source>
		</display>
	</item>
	<item>
		<key>
			<![CDATA[ 高考 ]]>
		</key>
		<city>
			<![CDATA[ 山西 ]]>
		</city>
		<display>
			<zh_type>
				<![CDATA[ 查分 ]]>
			</zh_type>
			<zh_year>
				<![CDATA[ 2019 ]]>
			</zh_year>
			<title>
				<![CDATA[ 2019年山西高考成绩查询时间_优志愿 ]]>
			</title>
			<titleurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</titleurl>
			<mbtitleurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</mbtitleurl>
			<moretxt>
				<![CDATA[ 各地区成绩查询时间 ]]>
			</moretxt>
			<moreurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</moreurl>
			<mbmoreurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</mbmoreurl>
			<showurl>
				<![CDATA[ www.youzy.cn ]]>
			</showurl>
			<table>
				<head>
					<tr>
						<th>
							<text>
								<![CDATA[ 省市 ]]>
							</text>
						</th>
						<th>
							<text>
								<![CDATA[ 查分参考时间 ]]>
							</text>
						</th>
						<th>
							<text>
								<![CDATA[ 查分入口 ]]>
							</text>
						</th>
						<th>
							<text>
								<![CDATA[ 查分电话 ]]>
							</text>
						</th>
					</tr>
				</head>
				<body>
					<tr>
						<td>
							<adapt>
								<name>
									<![CDATA[ 山西 ]]>
								</name>
							</adapt>
						</td>
						<td>
							<adapt>
								<name>
									<![CDATA[ 6月24日 ]]>
								</name>
							</adapt>
						</td>
						<td>
							<adapt>
								<name>
									<![CDATA[ 山西招生考试网 ]]>
								</name>
								<link>
									<![CDATA[ http://www.sxkszx.cn ]]>
								</link>
								<mblink>
									<![CDATA[ http://www.sxkszx.cn ]]>
								</mblink>
							</adapt>
						</td>
						<td>
							<adapt>
								<name>
									<![CDATA[ 12580 ]]>
								</name>
							</adapt>
						</td>
					</tr>
				</body>
			</table>
			<source>
				<![CDATA[ 优志愿 ]]>
			</source>
		</display>
	</item>
	<item>
		<key>
			<![CDATA[ 高考 ]]>
		</key>
		<city>
			<![CDATA[ 甘肃 ]]>
		</city>
		<display>
			<zh_type>
				<![CDATA[ 查分 ]]>
			</zh_type>
			<zh_year>
				<![CDATA[ 2019 ]]>
			</zh_year>
			<title>
				<![CDATA[ 2019年甘肃高考成绩查询时间_优志愿 ]]>
			</title>
			<titleurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</titleurl>
			<mbtitleurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</mbtitleurl>
			<moretxt>
				<![CDATA[ 各地区成绩查询时间 ]]>
			</moretxt>
			<moreurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</moreurl>
			<mbmoreurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</mbmoreurl>
			<showurl>
				<![CDATA[ www.youzy.cn ]]>
			</showurl>
			<table>
				<head>
					<tr>
						<th>
							<text>
								<![CDATA[ 省市 ]]>
							</text>
						</th>
						<th>
							<text>
								<![CDATA[ 查分参考时间 ]]>
							</text>
						</th>
						<th>
							<text>
								<![CDATA[ 查分入口 ]]>
							</text>
						</th>
						<th>
							<text>
								<![CDATA[ 查分电话 ]]>
							</text>
						</th>
					</tr>
				</head>
				<body>
					<tr>
						<td>
							<adapt>
								<name>
									<![CDATA[ 甘肃 ]]>
								</name>
							</adapt>
						</td>
						<td>
							<adapt>
								<name>
									<![CDATA[ 6月22日 ]]>
								</name>
							</adapt>
						</td>
						<td>
							<adapt>
								<name>
									<![CDATA[ 甘肃省教育考试院 ]]>
								</name>
								<link>
									<![CDATA[ http://gaokao.ganseea.cn ]]>
								</link>
								<mblink>
									<![CDATA[ http://gaokao.ganseea.cn ]]>
								</mblink>
							</adapt>
						</td>
						<td>
							<adapt>
								<name>
									<![CDATA[ 12580 ]]>
								</name>
							</adapt>
						</td>
					</tr>
				</body>
			</table>
			<source>
				<![CDATA[ 优志愿 ]]>
			</source>
		</display>
	</item>
	<item>
		<key>
			<![CDATA[ 高考 ]]>
		</key>
		<city>
			<![CDATA[ 云南 ]]>
		</city>
		<display>
			<zh_type>
				<![CDATA[ 查分 ]]>
			</zh_type>
			<zh_year>
				<![CDATA[ 2019 ]]>
			</zh_year>
			<title>
				<![CDATA[ 2019年云南高考成绩查询时间_优志愿 ]]>
			</title>
			<titleurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</titleurl>
			<mbtitleurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</mbtitleurl>
			<moretxt>
				<![CDATA[ 各地区成绩查询时间 ]]>
			</moretxt>
			<moreurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</moreurl>
			<mbmoreurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</mbmoreurl>
			<showurl>
				<![CDATA[ www.youzy.cn ]]>
			</showurl>
			<table>
				<head>
					<tr>
						<th>
							<text>
								<![CDATA[ 省市 ]]>
							</text>
						</th>
						<th>
							<text>
								<![CDATA[ 查分参考时间 ]]>
							</text>
						</th>
						<th>
							<text>
								<![CDATA[ 查分入口 ]]>
							</text>
						</th>
					</tr>
				</head>
				<body>
					<tr>
						<td>
							<adapt>
								<name>
									<![CDATA[ 云南 ]]>
								</name>
							</adapt>
						</td>
						<td>
							<adapt>
								<name>
									<![CDATA[ 6月23日 ]]>
								</name>
							</adapt>
						</td>
						<td>
							<adapt>
								<name>
									<![CDATA[ 云南省招考频道 ]]>
								</name>
								<link>
									<![CDATA[ http://www.ynzs.cn/ ]]>
								</link>
								<mblink>
									<![CDATA[ http://www.ynzs.cn/ ]]>
								</mblink>
							</adapt>
						</td>
					</tr>
				</body>
			</table>
			<source>
				<![CDATA[ 优志愿 ]]>
			</source>
		</display>
	</item>
	<item>
		<key>
			<![CDATA[ 高考 ]]>
		</key>
		<city>
			<![CDATA[ 贵州 ]]>
		</city>
		<display>
			<zh_type>
				<![CDATA[ 查分 ]]>
			</zh_type>
			<zh_year>
				<![CDATA[ 2019 ]]>
			</zh_year>
			<title>
				<![CDATA[ 2019年贵州高考成绩查询时间_优志愿 ]]>
			</title>
			<titleurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</titleurl>
			<mbtitleurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</mbtitleurl>
			<moretxt>
				<![CDATA[ 各地区成绩查询时间 ]]>
			</moretxt>
			<moreurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</moreurl>
			<mbmoreurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</mbmoreurl>
			<showurl>
				<![CDATA[ www.youzy.cn ]]>
			</showurl>
			<table>
				<head>
					<tr>
						<th>
							<text>
								<![CDATA[ 省市 ]]>
							</text>
						</th>
						<th>
							<text>
								<![CDATA[ 查分参考时间 ]]>
							</text>
						</th>
						<th>
							<text>
								<![CDATA[ 查分入口 ]]>
							</text>
						</th>
					</tr>
				</head>
				<body>
					<tr>
						<td>
							<adapt>
								<name>
									<![CDATA[ 贵州 ]]>
								</name>
							</adapt>
						</td>
						<td>
							<adapt>
								<name>
									<![CDATA[ 6月23日 ]]>
								</name>
							</adapt>
						</td>
						<td>
							<adapt>
								<name>
									<![CDATA[ 贵州省招生考试院 ]]>
								</name>
								<link>
									<![CDATA[ http://www.eaagz.org.cn ]]>
								</link>
								<mblink>
									<![CDATA[ http://www.eaagz.org.cn ]]>
								</mblink>
							</adapt>
						</td>
					</tr>
				</body>
			</table>
			<source>
				<![CDATA[ 优志愿 ]]>
			</source>
		</display>
	</item>
	<item>
		<key>
			<![CDATA[ 高考 ]]>
		</key>
		<city>
			<![CDATA[ 内蒙古 ]]>
		</city>
		<display>
			<zh_type>
				<![CDATA[ 查分 ]]>
			</zh_type>
			<zh_year>
				<![CDATA[ 2019 ]]>
			</zh_year>
			<title>
				<![CDATA[ 2019年内蒙古高考成绩查询时间_优志愿 ]]>
			</title>
			<titleurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</titleurl>
			<mbtitleurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</mbtitleurl>
			<moretxt>
				<![CDATA[ 各地区成绩查询时间 ]]>
			</moretxt>
			<moreurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</moreurl>
			<mbmoreurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</mbmoreurl>
			<showurl>
				<![CDATA[ www.youzy.cn ]]>
			</showurl>
			<table>
				<head>
					<tr>
						<th>
							<text>
								<![CDATA[ 省市 ]]>
							</text>
						</th>
						<th>
							<text>
								<![CDATA[ 查分参考时间 ]]>
							</text>
						</th>
						<th>
							<text>
								<![CDATA[ 查分入口 ]]>
							</text>
						</th>
					</tr>
				</head>
				<body>
					<tr>
						<td>
							<adapt>
								<name>
									<![CDATA[ 内蒙古 ]]>
								</name>
							</adapt>
						</td>
						<td>
							<adapt>
								<name>
									<![CDATA[ 6月23日 ]]>
								</name>
							</adapt>
						</td>
						<td>
							<adapt>
								<name>
									<![CDATA[ 内蒙古招生考试信息网 ]]>
								</name>
								<link>
									<![CDATA[ http://www.nm.zsks.cn/ ]]>
								</link>
								<mblink>
									<![CDATA[ http://www.nm.zsks.cn/ ]]>
								</mblink>
							</adapt>
						</td>
					</tr>
				</body>
			</table>
			<source>
				<![CDATA[ 优志愿 ]]>
			</source>
		</display>
	</item>
	<item>
		<key>
			<![CDATA[ 高考 ]]>
		</key>
		<city>
			<![CDATA[ 青海 ]]>
		</city>
		<display>
			<zh_type>
				<![CDATA[ 查分 ]]>
			</zh_type>
			<zh_year>
				<![CDATA[ 2019 ]]>
			</zh_year>
			<title>
				<![CDATA[ 2019年青海高考成绩查询时间_优志愿 ]]>
			</title>
			<titleurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</titleurl>
			<mbtitleurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</mbtitleurl>
			<moretxt>
				<![CDATA[ 各地区成绩查询时间 ]]>
			</moretxt>
			<moreurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</moreurl>
			<mbmoreurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</mbmoreurl>
			<showurl>
				<![CDATA[ www.youzy.cn ]]>
			</showurl>
			<table>
				<head>
					<tr>
						<th>
							<text>
								<![CDATA[ 省市 ]]>
							</text>
						</th>
						<th>
							<text>
								<![CDATA[ 查分参考时间 ]]>
							</text>
						</th>
						<th>
							<text>
								<![CDATA[ 查分入口 ]]>
							</text>
						</th>
					</tr>
				</head>
				<body>
					<tr>
						<td>
							<adapt>
								<name>
									<![CDATA[ 青海 ]]>
								</name>
							</adapt>
						</td>
						<td>
							<adapt>
								<name>
									<![CDATA[ 6月25日 ]]>
								</name>
							</adapt>
						</td>
						<td>
							<adapt>
								<name>
									<![CDATA[ 青海省教育招生考试院 ]]>
								</name>
								<link>
									<![CDATA[ http://118.213.59.8 ]]>
								</link>
								<mblink>
									<![CDATA[ http://118.213.59.8 ]]>
								</mblink>
							</adapt>
						</td>
					</tr>
				</body>
			</table>
			<source>
				<![CDATA[ 优志愿 ]]>
			</source>
		</display>
	</item>
	<item>
		<key>
			<![CDATA[ 高考 ]]>
		</key>
		<city>
			<![CDATA[ 海南 ]]>
		</city>
		<display>
			<zh_type>
				<![CDATA[ 查分 ]]>
			</zh_type>
			<zh_year>
				<![CDATA[ 2019 ]]>
			</zh_year>
			<title>
				<![CDATA[ 2019年海南高考成绩查询时间_优志愿 ]]>
			</title>
			<titleurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</titleurl>
			<mbtitleurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</mbtitleurl>
			<moretxt>
				<![CDATA[ 各地区成绩查询时间 ]]>
			</moretxt>
			<moreurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</moreurl>
			<mbmoreurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</mbmoreurl>
			<showurl>
				<![CDATA[ www.youzy.cn ]]>
			</showurl>
			<table>
				<head>
					<tr>
						<th>
							<text>
								<![CDATA[ 省市 ]]>
							</text>
						</th>
						<th>
							<text>
								<![CDATA[ 查分参考时间 ]]>
							</text>
						</th>
						<th>
							<text>
								<![CDATA[ 查分入口 ]]>
							</text>
						</th>
					</tr>
				</head>
				<body>
					<tr>
						<td>
							<adapt>
								<name>
									<![CDATA[ 海南 ]]>
								</name>
							</adapt>
						</td>
						<td>
							<adapt>
								<name>
									<![CDATA[ 6月24日 ]]>
								</name>
							</adapt>
						</td>
						<td>
							<adapt>
								<name>
									<![CDATA[ 海南省考试局 ]]>
								</name>
								<link>
									<![CDATA[ http://ea.hainan.gov.cn/index ]]>
								</link>
								<mblink>
									<![CDATA[ http://ea.hainan.gov.cn/index ]]>
								</mblink>
							</adapt>
						</td>
					</tr>
				</body>
			</table>
			<source>
				<![CDATA[ 优志愿 ]]>
			</source>
		</display>
	</item>
	<item>
		<key>
			<![CDATA[ 高考 ]]>
		</key>
		<city>
			<![CDATA[ 西藏 ]]>
		</city>
		<display>
			<zh_type>
				<![CDATA[ 查分 ]]>
			</zh_type>
			<zh_year>
				<![CDATA[ 2019 ]]>
			</zh_year>
			<title>
				<![CDATA[ 2019年西藏高考成绩查询时间_优志愿 ]]>
			</title>
			<titleurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</titleurl>
			<mbtitleurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</mbtitleurl>
			<moretxt>
				<![CDATA[ 各地区成绩查询时间 ]]>
			</moretxt>
			<moreurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</moreurl>
			<mbmoreurl>
				<![CDATA[ https://www.youzy.cn/op/360?tw=news&newsId=68256 ]]>
			</mbmoreurl>
			<showurl>
				<![CDATA[ www.youzy.cn ]]>
			</showurl>
			<table>
				<head>
					<tr>
						<th>
							<text>
								<![CDATA[ 省市 ]]>
							</text>
						</th>
						<th>
							<text>
								<![CDATA[ 查分参考时间 ]]>
							</text>
						</th>
						<th>
							<text>
								<![CDATA[ 查分入口 ]]>
							</text>
						</th>
					</tr>
				</head>
				<body>
					<tr>
						<td>
							<adapt>
								<name>
									<![CDATA[ 西藏 ]]>
								</name>
							</adapt>
						</td>
						<td>
							<adapt>
								<name>
									<![CDATA[ 6月25日 ]]>
								</name>
							</adapt>
						</td>
						<td>
							<adapt>
								<name>
									<![CDATA[ 西藏教育 ]]>
								</name>
								<link>
									<![CDATA[ http://www.xzedu.com.cn/ ]]>
								</link>
								<mblink>
									<![CDATA[ http://www.xzedu.com.cn/ ]]>
								</mblink>
							</adapt>
						</td>
					</tr>
				</body>
			</table>
			<source>
				<![CDATA[ 优志愿 ]]>
			</source>
		</display>
	</item>
</DOCUMENT>
'''

handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)