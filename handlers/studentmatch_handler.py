
import jinja_env
import logging
import webapp2
from google.appengine.api import users
from models import newuser


class StudentMatchHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user == None: 
            self.redirect("/")
            return
        myUser = newuser.UserModel.query(newuser.UserModel.user_email == user.email()).get()
        #logging.info(myUser)
        new_user = "<div>" + "Here are tutors that can help you with " + str(myUser.whichsubject) + " on " + str(myUser.whichday) + " at " + str(myUser.whichtime) + "div"

        matchedTutors = newuser.UserModel.query().fetch()
        for match in matchedTutors:
            score = 0
            if match.whichsubject == myUser.whichsubject:
                score = score + 1
            if match.whichday == myUser.whichday:
               score = score + 1
            if match.whichtime == myUser.whichtime:
                score = score + 1

                match.score = score

##This sorts the users from highest compatability to lowest
        matchedTutors.sort(key=lambda tutor: tutor.score, reverse = True)
##This takes out the user trying to find a roommate from the list of options
        matchedTutors= matchedTutors[1:]

        match_str = ""
        for match in matchedTutors:
            logging.info(match)
            match_str += "<div> Tutors: " + str(match.whichsubject) + " " + str(match.whichday) + "Email: " + str(match.user_email) 
            match_str+= "</div>"

        template = jinja_env.env.get_template('templates/studentmatch.html')
        parajo = {
            "html_userObject": match_str,
            "html_info": new_user,
            "html_email" : user.email()
            }
        self.response.out.write(template.render(parajo))