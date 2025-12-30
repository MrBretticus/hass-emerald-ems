# Home Assistant custom integration to fetch data from Emerald EMS

[![GitHub Release][releases-shield]][releases]
[![GitHub Activity][commits-shield]][commits]
[![License][license-shield]](LICENSE)

![Project Maintenance][maintenance-shield]
[![BuyMeCoffee][buymecoffeebadge]][buymecoffee]

[![Discord][discord-shield]][discord]
[![Community Forum][forum-shield]][forum]

[![hacs][hacsbadge]][hacs]

> [!WARNING]  
> This integration is not ready for use.

_[Emerald EMS][emerald-ems] integration for [Home Assistant][home-assistant]._

**This integration will set up the following platforms.**

Platform | Description
-- | --
`sensor` | Show info from the Emerald EMS API.

## Automatic Installation

1. Install HACS
2. Within HA go to HACS > Integrations > ... (in top right corner) > Custom Repositories
3. Add URL: `https://github.com/mrbretticus/hass-emerald-ems`, Category: `Integration`
4. Go to the integrations page inside your home assistant install
5. Search for `Emerald EMS`
6. Install, enter your Emerald EMS username and password.

## Manual Installation

1. Using the tool of choice open the directory (folder) for your HA configuration (where you find `configuration.yaml`).
1. If you do not have a `custom_components` directory (folder) there, you need to create it.
1. In the `custom_components` directory (folder) create a new folder called `emerald_ems`.
1. Download _all_ the files from the `custom_components/emerald_ems/` directory (folder) in this repository.
1. Place the files you downloaded in the new directory (folder) you created.
1. Restart Home Assistant
1. In the HA UI go to "Configuration" -> "Integrations" click "+" and search for "Emerald EMS"

## Configuration is done in the UI

<!---->

## Contributions are welcome

If you want to contribute to this please read the [Contribution guidelines](CONTRIBUTING.md)

***

[emerald-ems]: http://emerald-ems.com.au/
[buymecoffee]: https://www.buymeacoffee.com/mrbretticus
[buymecoffeebadge]: https://img.shields.io/badge/buy%20me%20a%20coffee-donate-yellow.svg?style=for-the-badge
[commits-shield]: https://img.shields.io/github/commit-activity/y/mrbretticus/hass-emerald-ems.svg?style=for-the-badge
[commits]: https://github.com/mrbretticus/hass-emerald-ems/commits/main
[discord]: https://discord.gg/BW2tZZVH
[discord-shield]: https://img.shields.io/discord/330944238910963714.svg?style=for-the-badge
[forum-shield]: https://img.shields.io/badge/community-forum-brightgreen.svg?style=for-the-badge
[home-assistant]: https://home-assistant.io
[forum]: https://community.home-assistant.io/
[license-shield]: https://img.shields.io/github/license/mrbretticus/hass-emerald-ems.svg?style=for-the-badge
[maintenance-shield]: https://img.shields.io/badge/maintainer-Brett%20Errington%20%40mrbretticus-blue.svg?style=for-the-badge
[releases-shield]: https://img.shields.io/github/release/mrbretticus/hass-emerald-ems.svg?style=for-the-badge
[releases]: https://github.com/mrbretticus/hass-emerald-ems/releases
[hacs]: https://hacs.xyz
[hacsbadge]: https://img.shields.io/badge/HACS-Custom-orange.svg?style=for-the-badge
