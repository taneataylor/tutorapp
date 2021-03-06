import jinja_env
import logging
import webapp2

from google.appengine.api import users

class TutorOrStudentHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        logging.info("TutorOrStudentHandler")
        logging.info(users.get_current_user())
        logging.info(users.create_login_url('/hometutor'))
        logging.info(users.create_login_url('/studentrequest'))
        html_params = {
            "html_login":users.create_login_url('/tutorsignup'),
            "html_login2":users.create_login_url('/studentsignup'),
        
        }

        template = jinja_env.env.get_template('templates/tutororstudent.html')
        self.response.out.write(template.render(html_params))