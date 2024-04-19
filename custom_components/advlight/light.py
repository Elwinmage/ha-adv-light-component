"""Light platform for advanced light."""
import asyncio
import logging

import voluptuous as vol

from homeassistant.components.light import PLATFORM_SCHEMA, LightEntity, ColorMode
from homeassistant.const import (
    ATTR_ENTITY_ID,
    CONF_NAME,
    CONF_UNIQUE_ID,
    SERVICE_TOGGLE,
    SERVICE_TURN_OFF,
    SERVICE_TURN_ON,
)
from homeassistant.core import DOMAIN as HA_DOMAIN
from homeassistant.helpers import entity_platform
import homeassistant.helpers.config_validation as cv
from homeassistant.helpers.event import async_track_state_change
from homeassistant.helpers.reload import async_setup_reload_service
from homeassistant.util import slugify

from .const import (
    CONF_INPUT,
    CONF_OUTPUT,
    CONF_SUBTYPE,
    DEFAULT_NAME,
    DEFAULT_SUBTYPE,
    DOMAIN,
    ICON,
    OUPTUT_DURATION,
    PLATFORMS,
)

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Required(CONF_OUTPUT): cv.entity_id,
        vol.Required(CONF_INPUT): cv.entity_id,
        vol.Optional(CONF_SUBTYPE, default=DEFAULT_SUBTYPE): cv.string,
        vol.Optional(CONF_NAME, default=DEFAULT_NAME): cv.string,
        vol.Optional(CONF_UNIQUE_ID, default="none"): cv.string,
    }
)

_LOGGER: logging.Logger = logging.getLogger(__package__)


async def async_setup_platform(
    hass, config, async_add_entities, discovery_info=None
) -> None:
    """Set up the advlight platform."""
    await async_setup_reload_service(hass, DOMAIN, PLATFORMS)

    platform = entity_platform.current_platform.get()
    assert platform

    parameters = {
        "name": config.get(CONF_NAME),
        "unique_id": config.get(CONF_UNIQUE_ID),
        "light_command_id": config.get(CONF_OUTPUT),
        "light_state_id": config.get(CONF_INPUT),
        "subtype": config.get(CONF_SUBTYPE),
    }

    advlight = AdvLight(**parameters)
    async_add_entities([advlight])


class AdvLight(LightEntity):
    """AdvLight class."""

    def __init__(self, **kwargs):
        """Class init."""
        self._name = kwargs.get("name")
        self._unique_id = kwargs.get("unique_id")
        self._light_command_id = kwargs.get("light_command_id")
        self._light_state_id = kwargs.get("light_state_id")
        self._light_subtype = kwargs.get("subtype")
        if self._light_subtype == "non":
            self._light_subtype = DEFAULT_SUBTYPE
        self._light_s = False
        if self._unique_id == "none":
            self._unique_id = slugify(f"{DOMAIN}_{self._name}_{self._light_command_id}")
        self._attr_supported_color_modes = [ColorMode.ONOFF]

    async def async_added_to_hass(self):
        """Run when entity about to be added."""
        await super().async_added_to_hass()

        # Add listener to check if light state has changed
        async_track_state_change(
            self.hass, self._light_state_id, self._async_light_changed
        )

    async def _async_light_changed(self, entity_id, old_state, new_state):
        """Handle Light State changes."""
        if new_state is None:
            return
        new_state = new_state.state

        if old_state is not None:
            old_state = old_state.state

        _LOGGER.debug("Light state change from %s to %s", old_state, new_state)
        self._light_s = new_state
        self.async_write_ha_state()

    @property
    def name(self):
        """Return the name of the sensor."""
        return f"{self._name}"

    @property
    def is_on(self):
        """Returns if the light entity is on or not."""
        if self._light_s == "on":
            return True
        return False

    @property
    def state(self):
        """Returns state of the light."""
        return self._light_s

    @property
    def icon(self):
        """Return the icon of the sensor."""
        return ICON

    @property
    def unique_id(self):
        """Return a unique_id for this entity."""
        return self._unique_id

    async def _toggle_light(self):
        data = {ATTR_ENTITY_ID: self._light_command_id}
        if self._light_subtype == "impulse":
            await self.hass.services.async_call(HA_DOMAIN, SERVICE_TURN_ON, data)
            await asyncio.sleep(OUPTUT_DURATION)
            await self.hass.services.async_call(HA_DOMAIN, SERVICE_TURN_OFF, data)
        elif self._light_subtype == "backAndForth":
            await self.hass.services.async_call(HA_DOMAIN, SERVICE_TOGGLE, data)

    async def async_turn_on(self, **kwargs):
        """Turn device on."""
        if self.is_on is not True:
            self.hass.async_create_task(self._toggle_light())

    async def async_turn_off(self, **kwargs):
        """Turn device off."""
        if self.is_on is True:
            self.hass.async_create_task(self._toggle_light())
