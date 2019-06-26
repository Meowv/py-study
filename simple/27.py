# -*- coding: utf-8 -*-

from email.mime.text import MIMEText

msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')

# 输入Email地址和口令
from_addr =  input('From:')
password = input('Password:')

# 输入收件人地址
to_addr = input('To:')
smtp_server = input('SMTP server:')

import smtplib
server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())