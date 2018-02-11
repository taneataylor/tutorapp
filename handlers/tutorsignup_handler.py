import jinja_env
import logging
import webapp2

from models import tutoruser
from google.appengine.api import users

class TutorSignUpHandler(webapp2.RequestHandler):
    def get(self):
    	user = users.get_current_user()
    	logging.info("TutorSignUp")
    	logging.info(users.get_current_user())

    	template = jinja_env.env.get_template('templates/tutorsignup.html')
        self.response.out.write(template.render())