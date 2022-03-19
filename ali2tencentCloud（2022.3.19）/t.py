





import itchat

# 登录并获得QR码
itchat.login()
# 通过手机扫描QR码登录的微信号给“文件传输助手”发送消息“您好”
itchat.send(u'您好,祝您三八妇女节，快乐！我在做测试！', 'filehelper')
