import pykka
import Entity

__author__ = 'Abel Navarro <abel.navarro@gmail.com>'

class SwarmManager():
    def init(self):
        actor_ref = Entity.Entity.start()
        actors = pykka.ActorRegistry.get_all()
        print ("num actors: %d" % len(actors))
        actor_ref.ask({'msg': 'hola'})
        actors = pykka.ActorRegistry.get_all()
        print ("num actors: %d" % len(actors))
        actor_ref.stop()
        actors = pykka.ActorRegistry.get_all()
        print ("num actors: %d" % len(actors))

