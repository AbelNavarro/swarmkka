import pykka

__author__ = 'Abel Navarro <abel.navarro@gmail.com>'

class Entity(pykka.ThreadingActor):

    @classmethod
    def register(cls):
        pass

    def on_receive(self, message):
        print("Hi!")
