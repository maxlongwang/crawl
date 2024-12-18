
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# 邮件发送相关信息
smtp_server = 'smtp.126.com'
port = 25  # 或者465，取决于服务器要求
username = 'lwp542'
password = 'long123..'

# 邮件接收方和发送方信息
sender_email = 'lwp542@126.com'
receiver_email = '76000892@qq.com'

# 创建邮件对象和附件
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = 'Email with Attachment'

# 邮件正文
message.attach(MIMEText('This is a message with attachment.', 'plain'))

# 添加附件
filename = './output/sql/create_table.sql'  # 要附加的文件路径
attachment = MIMEApplication(open(filename, 'rb').read())
attachment.add_header('Content-Disposition', 'attachment', filename=filename)
message.attach(attachment)

# 发送邮件
session = smtplib.SMTP(smtp_server, port)
session.starttls()  # 启用TLS
session.login(username, password)
session.sendmail(sender_email, receiver_email, message.as_string())
session.quit()
