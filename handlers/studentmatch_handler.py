
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
<<<<<<< HEAD

        template = jinja_env.env.get_template('templates/studentmatch.html')
        self.response.out.write(template.render())

=======
        template = jinja_env.env.get_template('templates/studentmatch.html')
>>>>>>> 6d02cfcb7720afc1076d5e4ea4d7a79f70eda487
        user = users.get_current_user()
        if user == None: 
            self.redirect("/")
            return
        myUser = tutoruser.UserModel.query(newuser.UserModel.user_email == user.email()).get()
<<<<<<< HEAD
        new_user = "div" + "Here are tutors that can help you with " + str(myUser.subject) + " on " + str(myUser.day) + " at " + str(myUser.time) + "div"
=======
<<<<<<< HEAD
<<<<<<< HEAD
        new_user = "<div>" + "Here are tutors that can help you with " + str(myUser.subject) + " on " + str(myUser.day) + " at " + str(myUser.time) + "</div>"

=======
        new_user = "div" + "Here are tutors that can help you with " + str(myUser.subject) + " on " + str(myUser.day) + " at " + str(myUser.time) + "div"
>>>>>>> 6d02cfcb7720afc1076d5e4ea4d7a79f70eda487
=======
        new_user = "Here are tutors that can help you with " + str(myUser.subject) + " on " + str(myUser.day) + " at " + str(myUser.time)
>>>>>>> 26ed5cda8168c9bbe0be4fc4187b9e339713a491
>>>>>>> bca6d2d6cea3b5d1afdb07cedaa7fcd2adca7751

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
<<<<<<< HEAD
        matchedTutors = matchedTutors[1:]
=======
        matchedTutors= matchedTutors[1:]
        self.response.out.write(template.render())
>>>>>>> 6d02cfcb7720afc1076d5e4ea4d7a79f70eda487
