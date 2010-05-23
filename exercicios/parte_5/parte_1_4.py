import cherrypy
import cherrytemplate

form = '<form action="/execute" method="post"><input type="submit"/></form>'

class Root(object):

    @cherrypy.expose
    def index(self, **args):
        return cherrytemplate.renderTemplate(form)

    @cherrypy.expose
    def execute(self, **args):
        return 'Hi!'

cherrypy.quickstart(Root())
