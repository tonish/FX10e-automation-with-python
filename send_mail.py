#!/usr/bin/env python
# -*- coding: utf-8 -*-

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
import os
import glob
import datetime

def send_mail():
    fromaddr = "tonish@gmail.com"
    toaddr = "tonish@gmail.com"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['Subject'] = "FX10_log"
    body = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    msg.attach(MIMEText(body, 'plain'))
    msg['To'] = toaddr
        
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "yonit4525")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

