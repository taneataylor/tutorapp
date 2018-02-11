import jinja_env
import logging
import webapp2

from google.appengine.ext import ndb
from google.appengine.api import users

from models import newuser

class StudentRequestHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user == None: #if they are not logged in 
            self.redirect(users.create_login_url('/signup'))
            return
        user = newuser.UserModel.query(newuser.UserModel.user_email == user.email()).get()
        if user != None: #asks python if the user signed in currently already has an account
            self.redirect("/find")
            return
        template = jinja_env.env.get_template('templates/studentrequest.html')
        self.response.out.write(template.render())
    def post(self):
        user = users.get_current_user()
        if user == None:
            self.redirect("/")
            return

        r_subject = self.request.get("subject")
        r_day = self.request.get("day")
        r_time = self.request.get("time")
        r_price = self.request.get("price")
        

        new_user = newuser.UserModel(
            whichsubject = r_subject,
            whichday = r_day,
            whichtime = r_time,
            whichprice = r_price,
            user_email = user.email()
        )
        new_user.put()
        self.redirect("/studentmatch")
        