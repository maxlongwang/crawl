import zmail



# import yagmail


# # 定义用户名、授权码、服务器地址且连接服务器

# mail_server = yagmail.SMTP(user='发件人邮箱', passwd='授权码', host='smtp.qq.com')

# # 发送对象列表
# Email_to = ['收件人邮箱']
# subject = '任一填写'
# Email_text = "任一填写内容"
# # 多个附件用逗号隔开
# attachments = ['html报告目录地址']

# # 发送邮件
# mail_server.send(Email_to, subject, Email_text, attachments)



def base_use():
    server = zmail.server('76000892@qq.com', 'dadfds')
    info = {
        'subject': 'test',
        'from': 'fromwho',
        'content_text': 'send test',
        'attachments': ['./tmp/aa.pdf']
    }

    server.send_mail('test@126.com', info)


if __name__ == "__main__":
    base_use()
