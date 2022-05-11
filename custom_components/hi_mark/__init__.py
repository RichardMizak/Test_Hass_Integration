from hassapi import Hass
DOMAIN = "hi_mark_service"

ATTR_NAME = "hi"
DEFAULT_NAME = "hi_mark"


def setup(hass, config):
    config = Hass(hassurl="http://IP_ADDRESS:8123/", token="YOUR_HASS_TOKEN")

    def handle(call):

        name = call.data.get(ATTR_NAME, DEFAULT_NAME)

        hass.states.set("hi_mark_service.hello", name)

    hass.services.register(DOMAIN, "hello", handle)


    print("Oh, Hi Mark!")
    return True