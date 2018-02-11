
import jinja_env
import logging
import webapp2
from google.appengine.ext import ndb
from google.appengine.api import users
from models import newuser
from models import tutoruser

class StudentMatchHandler(webapp2.RequestHandler):
    def get(self):
        logging.info("MainHandler")

        template = jinja_env.env.get_template('templates/studentmatch.html')
        self.response.out.write(template.render())

        user = users.get_current_user()
        if user == None: 
            self.redirect("/")
            return
        myUser = tutoruser.UserModel.query(newuser.UserModel.user_email == user.email()).get()
        new_user = "<div>" + "Here are tutors that can help you with " + str(myUser.subject) + " on " + str(myUser.day) + " at " + str(myUser.time) + "</div>"


        matchedTutors = tutoruser.UserModel.query().fetch()
        for match in matchedTutors:
            score = 0
            if match.subject == myUser.subject:
                score = score + 1
            if match.day == myUser.day:
                score = score + 1
            if match.time == myUser.time:
                score = score + 1

                match.score = score

##This sorts the users from highest compatability to lowest
        matchedTutors.sort(key=lambda tutor: tutor.score, reverse = True)
##This takes out the user trying to find a roommate from the list of options
        matchedTutors = matchedTutors[1:]