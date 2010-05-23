#coding:utf-8

"""
3. Implementar uma aplicação web com uma
saudação dependente do horário(exemplos: "Bom dia são 9:00", "Boa tarde são 13:00" e
"Boa noite são 23:00")
"""

import cherrypy
import time

def get_system_hour_and_minute():
    system_time = time.localtime()
    return (system_time.tm_hour, system_time.tm_min)

def get_part_of_the_day(hour, minutes):
    part = ''
    if 0 <= hour < 3:
        part = 'Happy Hacking'
    elif 3 <= hour < 6:
        part = 'Sleep as a rock'
    elif 6 <= hour < 12:
        part = 'Morning'
    elif 12 <= hour < 18:
        part = 'Afternoon'
    else:
        part = 'Night'
    return part

class GoodMorningNewYorkWebApp(object):

    @cherrypy.expose
    def index(self):
        hour, minutes = get_system_hour_and_minute()
        part = get_part_of_the_day(hour, minutes)
        message = "Good %s New York! It's %d:%d!" % (part, hour, minutes)
        return message

cherrypy.quickstart(GoodMorningNewYorkWebApp())
