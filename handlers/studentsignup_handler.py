import jinja_env
import logging
import webapp2

from models import newuser
from google.appengine.api import users

class StudentSignUpHandler(webapp2.RequestHandler):
    def get(self):
    	user = users.get_current_user()
    	logging.info("SignSignUp")
    	logging.info(users.get_current_user())

    	template = jinja_env.env.get_template('templates/studentsignup.html')
        self.response.out.write(template.render())