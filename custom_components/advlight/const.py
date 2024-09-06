"""Constants for integration_blueprint."""

# Base component constants
NAME = "Advanced Light"
DOMAIN = "advlight"
DOMAIN_DATA = f"{DOMAIN}_data"
VERSION = "2024.09.06"
ISSUE_URL = "https://github.com/Elwinmage/ha-adv-light-component/issues"

LIGHT = "light"
PLATFORMS = [LIGHT]

# Defaults
DEFAULT_NAME = DOMAIN

CONF_OUTPUT = "light_command"
CONF_INPUT = "light_state"

CONF_SUBTYPE = "subtype"
DEFAULT_SUBTYPE = "impulse"

OUPTUT_DURATION = 1

ICON = "mdi:lightbulb"

STARTUP_MESSAGE = f"""
-------------------------------------------------------------------
{NAME}
Version: {VERSION}
This is a custom integration!
If you have any issues with this you need to open an issue here:
{ISSUE_URL}
-------------------------------------------------------------------
"""
