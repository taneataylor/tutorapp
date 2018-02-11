import jinja_env
import logging
import webapp2

from google.appengine.api import users

from models import newuser

class studentRequestHandler(webapp2.RequestHandler):
	def get(self):
		user = users.get_current_user()




def post(self):
        user = users.get_current_user()
        if user == None:
            self.redirect("/")
            return
		r_subject = self.request.get("subject")
        r_day = self.request.get("day")
        r_time = self.request.get("time")
        


        new_user = newuser.UserModel(whichsubject = r_subject,
        whichday = r_day,
        whichtime = r_time
        )
        new_user.put()
        self.redirect("/studentmatch")