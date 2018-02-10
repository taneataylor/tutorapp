import jinja_env
import logging
import webapp2



class HomeTutorHandler(webapp2.RequestHandler):
    def get(self):
    	logging.info("MainHandler")

    	template - jinja_env.env.get_template('/templates/home.html')