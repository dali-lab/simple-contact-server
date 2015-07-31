Simple Server for Static Website Contact Forms
----------------------------------

A simple contact form for static websites.  This is a simple Flask app that uses Heroku with the Sendgrid addon.  Based on Mandrill version from: https://github.com/ousenko/simple-contact-form



1. Create a heroku app and add sendgrid
-------------------

    bash
    $ git clone git@github.com:dali-lab/simple-contact-server.git
    $ heroku create <YOUR_HEROKU_APP>
    $ heroku addons:create sendgrid:starter
    $ heroku config:set USER_EMAIL=<YOUR EMAIL>
    $ heroku config:set USER_SITE=<YOUR SITE>
    $ heroku config:set SUCCESS_PAGE=<A SUCCESS PAGE TO REDIRECT USER TO AFTER THE MESSAGE IS SENT>

note heroku automatically configures the sendgrid username and password

2. Front-end setup
-------------------

Your form html can be something like this:

    html
    <form action="https://<YOUR_HEROKU_APP>.herokuapp.com/send">
      Email: <input type="text" name="name"><br>
      Name: <input type="text" name="email"><br>
      Subject: <input type="text" name="subject"><br>
      Message: <textarea name="message" cols="40" rows="5"></textarea>
      <input type="submit" value="Send Message">
    </form> 

