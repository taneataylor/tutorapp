from google.appengine.ext import ndb

class UserModel(ndb.Model):
    whichsubject = ndb.StringProperty()
    whichday = ndb.StringProperty()
    whichtime = ndb.StringProperty()
    whichprice = ndb.StringProperty()
    user_email = ndb.StringProperty()
    