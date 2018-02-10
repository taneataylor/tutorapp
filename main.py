import os
import webapp2

from handlers import jinja_env

jinja_env.init(os.path.dirname(__file__))

app = webapp2.WSGIApplication([
	('/', main_handler.MainHandler),
	('/hometutor',hometutor_handler.HomeTutorHandler),
	('/homestudent',homestudent_handler.HomeStudentHandler),
	('/tutorsignup',tutorsignup_handler.TutorSignUpHandler),
	('/studentsignup',studentsignup_handler.StudentSignUpHandler),
	('/tutornotifs', tutornotifs_handler.TutorNotifsHandler),
	#('/tutorsubjects', tutorsubjects_handler.TutorSubjectsHandler),
	('/studentmatch', studentmatch_handler.StudentMatchHandler),
	('/studentrequest', studentrequest_handler.StudentRequestHandler),

], debug=True)
