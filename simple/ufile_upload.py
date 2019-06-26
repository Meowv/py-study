# -*- coding: utf-8 -*-

from ufile import config, logger, filemanager

#设置上传host后缀
config.set_default(uploadsuffix='.cn-bj.ufileos.com')
#设置下载host后缀，普通下载后缀即上传后缀，CDN下载后缀为
config.set_default(downloadsuffix='.ufile.ucloud.com.cn')
#设置请求连接超时时间，单位为秒
config.set_default(connection_timeout=60)
#设置私有bucket下载链接有效期,单位为秒
config.set_default(expires=60)

locallogname = 'log.txt'
logger.set_log_file(locallogname)

public_key = ''
private_key = ''

public_bucket = 'tob'
put_key = '360/xml/gaokao_score3.xml'
localfile = 'gaokao_score3.xml'

uploadhitufile_handler = filemanager.FileManager(public_key, private_key)

ret, resp = uploadhitufile_handler.putfile(public_bucket, put_key, localfile, header = None)
if resp.status_code == 200:
    print(resp._ResponseInfo__response.url)