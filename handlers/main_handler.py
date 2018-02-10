import jinja_env
import logging
import webapp2

from google.appengine.api import users

class MainHandler(webapp2.RequestHandler):
	def get(self):
		user = users.get_current_user()
		logging.info("MainHandler")
		logging.info(users.get_current_user())
		logging.info(users.create_login_url('/hometutor'))
		logging.info(users.create_login_url('/homestudent'))
			#html_params

		user = user.get_current_user()
		template = jinja_env.env.get_template('templates/tmpl.html')
		#self.response
	