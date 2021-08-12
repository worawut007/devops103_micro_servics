import smtplib
from email.message import EmailMessage
from nameko.rpc import rpc


def sen(id, firstname, lastname, email):
  msg = EmailMessage()
  text = "สวัสดีครับ คุณ "+ firstname + " " + lastname + " รหัสนักศึกษา " + str(id) + " ได้ลงทะเบียนแล้ว"

  msg['Subject'] = 'Register complete'
  msg['To'] = email

  s = smtplib.SMTP("smtp", 25)
  s.ehlo()
  s.sendmail(from_addr = 'madi.avenger@gmail.com', to_addrs = email, msg = msg.as_string())
  s.quit()

class Email:
  name = "email"

  @rpc
  def send(self, id, firstname, lastname, email):
      send(id, firstname, lastname, email)