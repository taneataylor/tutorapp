import jinja_env
import logging
import webapp2

from google.appengine.api import users

class TutorSignUpHandler(webapp2.RequestHandler):
    def get(self):
    	logging.info("MainHandler")