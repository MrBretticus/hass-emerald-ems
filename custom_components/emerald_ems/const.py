from logging import Logger, getLogger

LOGGER: Logger = getLogger(__package__)

NAME = "Emerald EMS"
DOMAIN = "emerald_ems"
VERSION = "0.1.0"
ATTRIBUTION = "Data provided by http://emerald-ems.com.au"
ISSUE_URL = "https://github.com/mrbretticus/hass-emerald-ems/issues"

# API
API_URL = "https://api.emerald-ems.com.au/api/v1/"
FLASHES_API_URL = "https://api.sync.flashdata.ihd.eems.app/"

# Icons
ICON = "mdi:transmission-tower"


STARTUP_MESSAGE = f"""
-------------------------------------------------------------------
{NAME}
Version: {VERSION}
This is a custom integration!
If you have any issues with this you need to open an issue here:
{ISSUE_URL}
-------------------------------------------------------------------
"""