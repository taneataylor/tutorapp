import jinja_env
import logging
import webapp2

from models import newuser
from models import tutoruser
from google.appengine.api import users


class HomeTutorHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user == None:
            self.redirect("/")
            return
        logging.info("HomeTutorHandler")
        logging.info(users.get_current_user())
        items = tutoruser.TutorUser.query().fetch()
        student = newuser.NewUser.query(user.email()==newuser.NewUser.student_email).get()
        
        user_str = ""
        for item in items:
            user_str += "<div>"
            user_str += "<h3>Item : " + item.student_whichsubject + "</h3>"
            user_str += "<p>" + item.student_whichday + "</p>"
            user_str += "</div>"

        html_params = {
            "title": "Main Title",
            "html_item": user_str,
            "user_name": student.student_name,
        }

        template = jinja_env.env.get_template('templates/hometutor.html')
        self.response.out.write(template.render(html_params))
    
    def post(self):
        r_subject = self.request.get("form_subject")
        r_day = self.request.get("form_day")
        r_time = self.request.get("form_time")
        r_price = self.request.get("form_price")
        logging.info(r_subject)
        logging.info(r_day)
        logging.info(r_time)
        logging.info(r_price)


        output = newuser.NewUser(
            user_whichsubject = r_subject,
            user_whichday = r_day,
            user_whichtime = r_time,
            user_whichprice = r_price
        )
        output.put()
        self.redirect("/studentmatch")