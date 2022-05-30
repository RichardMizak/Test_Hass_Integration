from hassapi import Hass
from homeassistant.components.button import ButtonEntity

DOMAIN = "hi_mark_service"

ATTR_NAME = "hi"
DEFAULT_NAME = "hi_mark"


from homeassistant.components.switch import SwitchEntity


class MySwitch(SwitchEntity):
    def __init__(self):
        self._is_on = False

    @property
    def name(self):
        """Name of the entity."""
        return "My Switch"

    @property
    def is_on(self):
        """If the switch is currently on or off."""
        return self._is_on

    def turn_on(self, **kwargs):
        """Turn the switch on."""
        self._is_on = True

    def turn_off(self, **kwargs):
        """Turn the switch off."""
        self._is_on = False

def setup(hass, config):
    config = Hass(hassurl="http://IP_ADDRESS:8123/", token="YOUR_HASS_TOKEN")

    def handle(call):

        name = call.data.get(ATTR_NAME, DEFAULT_NAME)

        hass.states.set("hi_mark_service.hello", name)

    hass.services.register(DOMAIN, "hello", handle)


    print("Oh, Hi Mark!")
    return True