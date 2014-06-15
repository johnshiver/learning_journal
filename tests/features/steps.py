from lettuce import *
from _client import Client

@step(u'I have a Client')
def have_a_client(step):
    world.client=Client()

@step(u'I request the page "(.*)"')
def when_i_request_the_page(step, url):
    world.a = world.client.run("GET {} HTTP/1.1\r\n\r\n".format(url))

@step(u'the page loads succesfully')
def check_load(step):
    assert "200 OK" in world.a

#@step(u'the page loads new submission form with old text')
#def check_load(step):
#    print world.a
#    assert "test again agaian" in world.a
#
