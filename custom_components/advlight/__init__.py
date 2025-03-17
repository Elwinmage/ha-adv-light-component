"""Custom integration to integrate Telerupteurs with Home Assistant.

For more details about this integration, please refer to
https://github.com/Elwinmage/ha-adv-light-component
"""
from datetime import timedelta
import logging

from homeassistant.core import HomeAssistant
from homeassistant.core_config import Config

from .const import DOMAIN, STARTUP_MESSAGE

SCAN_INTERVAL = timedelta(seconds=30)

_LOGGER: logging.Logger = logging.getLogger(__package__)


async def async_setup(hass: HomeAssistant, Config: Config) -> bool:
    """Set up this integration using YAML is not supported."""
    if hass.data.get(DOMAIN) is None:
        hass.data.setdefault(DOMAIN, {})
        _LOGGER.info(STARTUP_MESSAGE)
    return True
