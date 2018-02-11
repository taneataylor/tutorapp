from google.appengine.ext import ndb

class TutorModel(ndb.Model):
    whichsubject = ndb.StringProperty()
    whichday = ndb.StringProperty()
    whichtime = ndb.StringProperty()
    whichprice = ndb.StringProperty()