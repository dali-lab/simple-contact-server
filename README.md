Simple Server for Static Website Contact Forms
----------------------------------

A simple contact form for static websites.  This is a simple Flask app that uses Heroku with the Sengrid addon. 



1. Create a heroku app and add sendgrid
---------------------

    bash
    $ git clone https://github.com/ousenko/simple-contact-form.git
    $ heroku create <YOUR_HEROKU_APP>
    $ heroku addons:create sendgrid:starter
    $ heroku config:set USER_EMAIL=<YOUR EMAIL>
    $ heroku config:set USER_SITE=<YOUR SITE>
    $ heroku config:set SUCCESS_PAGE=<A SUCCESS PAGE TO REDIRECT USER TO AFTER THE MESSAGE IS SENT>

2. Front-end setup
-------------------

In your form html code specify the following:

    html
    <form action="https://<YOUR_HEROKU_APP>.herokuapp.com/send">
      Email: <input type="text" name="name"><br>
      Name: <input type="text" name="email"><br>
      Subject: <input type="text" name="subject"><br>
      Message: <textarea name="message" cols="40" rows="5"></textarea>
      <input type="submit" value="Send Message">
    </form> 

