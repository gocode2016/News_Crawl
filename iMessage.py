# coding:utf-8
from smtplib import SMTP_SSL
from email.header import Header
from email.mime.text import MIMEText

#kvpxjetukhnjbihj
#mtyksxcuytsdbicj
def send_Message(News = '卧槽',sub = '不明来历'):
	mail_info = {
		"from": "392285478@qq.com",
		"to": "392285478@qq.com",
		"hostname": "smtp.qq.com",
		"username": "392285478@qq.com",
		"password": "mtyksxcuytsdbicj",
		"mail_subject": sub,
		"mail_text": News,
		"mail_encoding": "utf-8"
	}

	try:
		smtp = SMTP_SSL(mail_info["hostname"])
		smtp.set_debuglevel(1)
		
		smtp.ehlo(mail_info["hostname"])
		smtp.login(mail_info["username"], mail_info["password"])

		msg = MIMEText(mail_info["mail_text"], "plain", mail_info["mail_encoding"])
		msg["Subject"] = Header(mail_info["mail_subject"], mail_info["mail_encoding"])
		msg["from"] = mail_info["from"]
		msg["to"] = mail_info["to"]
		
		smtp.sendmail(mail_info["from"], mail_info["to"], msg.as_string())

		smtp.quit()
		print ("suceess")
	except Exception,e:
		print ("failed")

#if __name__ == "__main__":
#    send_Message('hhh', '123');