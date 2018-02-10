import jinja_env
import logging
import webapp2

from google.appengine.api import users

class HomeStudentHandler(webapp2.RequestHandler):
    def get(self):
    	logging.info("MainHandler")

    	template = jinja_env.env.get_template('/templates/home.html')