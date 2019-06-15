import smtplib
import datetime

def send_mail(cond):
    if cond == 'good':
        TO = 'tonish@gmail.com'
        SUBJECT = '"FX10_log - ALL GOOD"'
        TEXT = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Gmail Sign In
        gmail_sender = 'tonish@gmail.com'
        gmail_passwd = 'Yonit4525'
        
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_sender, gmail_passwd)
        
        BODY = '\r\n'.join(['To: %s' % TO,
                            'From: %s' % gmail_sender,
                            'Subject: %s' % SUBJECT,
                            '', TEXT])
        
        try:
            server.sendmail(gmail_sender, [TO], BODY)
            print ('email sent')
        except:
            print ('error sending mail')
        
        server.quit()
    else:
        if cond == 'start':
            TO = 'tonish@gmail.com'
            SUBJECT = '"Script started"'
            TEXT = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Gmail Sign In
            gmail_sender = 'tonish@gmail.com'
            gmail_passwd = 'Yonit4525'

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login(gmail_sender, gmail_passwd)

            BODY = '\r\n'.join(['To: %s' % TO,
                                'From: %s' % gmail_sender,
                                'Subject: %s' % SUBJECT,
                                '', TEXT])

            try:
                server.sendmail(gmail_sender, [TO], BODY)
                print('email sent')
            except:
                print('error sending mail')

            server.quit()
        else:
            if cond == 'red screen':
                TO = 'tonish@gmail.com'
                SUBJECT = '"FX10_log - red screen"'
                TEXT = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                # Gmail Sign In
                gmail_sender = 'tonish@gmail.com'
                gmail_passwd = 'Yonit4525'

                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.ehlo()
                server.starttls()
                server.login(gmail_sender, gmail_passwd)

                BODY = '\r\n'.join(['To: %s' % TO,
                                    'From: %s' % gmail_sender,
                                    'Subject: %s' % SUBJECT,
                                    '', TEXT])

                try:
                    server.sendmail(gmail_sender, [TO], BODY)
                    print ('email sent')
                except:
                    print ('error sending mail')

                server.quit()
            else:
                if cond == 'bad':
                    TO = 'tonish@gmail.com'
                    SUBJECT = '"FX10_log - error unknown"'
                    TEXT = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                    # Gmail Sign In
                    gmail_sender = 'tonish@gmail.com'
                    gmail_passwd = 'Yonit4525'

                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login(gmail_sender, gmail_passwd)

                    BODY = '\r\n'.join(['To: %s' % TO,
                                        'From: %s' % gmail_sender,
                                        'Subject: %s' % SUBJECT,
                                        '', TEXT])

                    try:
                        server.sendmail(gmail_sender, [TO], BODY)
                        print ('email sent')
                    except:
                        print ('error sending mail')

                    server.quit()