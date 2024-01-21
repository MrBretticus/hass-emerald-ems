from homeassistant.components.sensor import SensorEntity, SensorEntityDescription

from .const import DOMAIN
from .coordinator import EmeraldDataUpdateCoordinator
from .entity import EmeraldEntity

ENTITY_DESCRIPTIONS = (
    SensorEntityDescription(
        key="emerald_ems",
        name="Emerald EMS Sensor",
        icon="mdi:format-quote-close",
    ),
)


async def setup_sensor(hass, entry, async_add_devices):
    """Set up the sensor platform."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_devices(
        EmeraldSensor(
            coordinator=coordinator,
            entity_description=entity_description,
        )
        for entity_description in ENTITY_DESCRIPTIONS
    )


class EmeraldSensor(EmeraldEntity, SensorEntity):
    def __init__(
        self,
        coordinator: EmeraldDataUpdateCoordinator,
        entity_description: SensorEntityDescription,
    ) -> None:
        super().__init__(coordinator)
        self.entity_description = entity_description

    @property
    def native_value(self) -> str:
        """Return the native value of the sensor."""
        return self.coordinator.data.get("body")
