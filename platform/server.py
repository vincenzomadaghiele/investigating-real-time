import cherrypy
import json
import requests
import glob

class SimpleServer(object):
    exposed=True

    def GET(self,*uri):

        pin = uri[0]
        # temporary solution
        source_path = 'sensors/*.json'
        sensors = glob.glob(source_path)

        # open catalog
        for path in sensors:
            f = open(path)
            sensor = json.load(f)
            if sensor['sensor_pin'] == int(pin):
                result = json.dumps(sensor)

        return result

if __name__ == '__main__':
    
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True
        }
    }
    cherrypy.tree.mount(SimpleServer(), '/', conf)
    cherrypy.config.update({'server.socket_host': '192.168.43.248'})
    cherrypy.config.update({'server.socket_port': 8080})
    cherrypy.engine.start()
    cherrypy.engine.block()