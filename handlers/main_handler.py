import jinja_env
import logging
import webapp2



class MainHandler(webapp2.RequestHandler):
	def get(self):
		logging.info("MainHandler")
		
		html_params = {
        	"title": "Main Title",
            "content": "Hello"
            
        }


		##user = user.get_current_user()

		template = jinja_env.env.get_template('templates/tmpl.html')
		self.response.out.write(template.render(html_params))
		
	