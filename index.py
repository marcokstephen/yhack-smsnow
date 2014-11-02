import webapp2

class IndexPage(webapp2.RequestHandler):
   def get(self):
      self.response.write("<a href='index.html'>hello world!!</a>")
