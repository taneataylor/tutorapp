import jinja_env
import logging
import webapp2

from google.appengine.ext import ndb
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
        r_price = self.request.get("price")
        logging.info(r_subject)
        logging.info(r_day)
        logging.info(r_time)
        logging.info(r_price)


        new_user = newuser.UserModel(
            whichsubject = r_subject,
            whichday = r_day,
            whichtime = r_time,
            whichprice = r_price
        )
        new_user.put()
        elf.redirect("/studentmatch")