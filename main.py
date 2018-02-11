import os
import webapp2
import logging

from handlers import jinja_env
from handlers import main_handler
from handlers import tutororstudent_handler
from handlers import hometutor_handler
from handlers import tutorsignup_handler
from handlers import studentsignup_handler
from handlers import studentmatch_handler
from handlers import studentrequest_handler

jinja_env.init(os.path.dirname(__file__))

app = webapp2.WSGIApplication([
	('/', main_handler.MainHandler),
	('/tutororstudent', tutororstudent_handler.TutorOrStudentHandler),
	('/hometutor',hometutor_handler.HomeTutorHandler),
	('/tutorsignup',tutorsignup_handler.TutorSignUpHandler),
	('/studentsignup',studentsignup_handler.StudentSignUpHandler),
	#('/tutornotifs', tutornotifs_handler.TutorNotifsHandler),
	#('/tutorsubjects', tutorsubjects_handler.TutorSubjectsHandler),
	('/studentmatch', studentmatch_handler.StudentMatchHandler),
	('/studentrequest', studentrequest_handler.StudentRequestHandler),

], debug=True)
