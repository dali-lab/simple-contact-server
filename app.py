import os

import sendgrid
from flask import Flask, request, redirect, abort

app = Flask(__name__)
sengrid_client =  sendgrid.SendGridClient(os.environ['SENDGRID_USERNAME'], os.environ['SENDGRID_PASSWORD'])

@app.route('/')
def index():
    return redirect(os.environ['USER_SITE'])


@app.route('/send', methods=['POST'])
def forward():
    # email_subject = 'Message from ' + request.form['name'] + ' about ' + request.form['subject']
    # email_to = os.environ['USER_EMAIL']
    # email_from = request.form['email']
    # email_txt = request.form['message']
    #
    # message = sendgrid.Mail()
    # message.add_to(email_to)
    # message.set_subject(email_subject)
    # message.set_text(email_txt)
    # message.set_from(email_from)
    #
    # status, msg = sengrid_client.send(message)
    #
    # if status != 'sent':
    #     abort(500)
    return redirect(os.environ['SUCCESS_PAGE'])


@app.errorhandler(500)
def error(e):
    return ('Sorry, something went wrong! %s - %s' % (e.__class__, e), 500)
