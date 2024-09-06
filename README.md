This is a fork from https://github.com/benlbrm/ha-telerupteur-component adding support for back and Forth switch.

**This component will set up the following platforms.**

Platform | Description
-- | --
`light` | Light control with a telerupteur.


## Installation

1. Add this repository to HACS.
2. Click install.


## Configuration is done in the configuration.yaml
```yaml
light:
- platform: advlight
    name: Lumiere Chambre1
    type: impulse # turn_on, wait,turn_off
    light_command: switch.dolightchambre1
    light_state: binary_sensor.dilightchambre1
- platform: advlight
    name: Lumiere Chambre2
    type: backAndForth # toggle
    light_command: switch.dolightchambre2
    light_state: binary_sensor.dilightchambre2
- platform: advlight
    name: Lumiere Chambre3
    type: push # turn_on
    light_command: switch.dolightchambre3
    light_state: binary_sensor.dilightchambre3
```

## Required hardware to use this integration

- Telerupteur to control lights with push buttons [[telerupteur-link]][link] or back anf forth swith
- 24Vdc to 230Vac relay to control the telerupteur, this relay is wired like a push button
- 230Vac to 24vdc relay to get the light status, this relay is wired like a light

<!---->

***

[integration_advlight]: https://github.com/Elwinmage/ha-adv-light-component
[commits-shield]: https://img.shields.io/github/commit-activity/y/Elwinmage/ha-adv-light-component.svg?style=for-the-badge
[commits]: https://github.com/Elwinmage/ha-adv-light-component/commits/master
[hacs]: https://hacs.xyz
[hacsbadge]: https://img.shields.io/badge/HACS-Custom-orange.svg?style=for-the-badge
[exampleimg]: example.png
[forum]: https://community.home-assistant.io/
[license]: https://github.com/Elwinmage/ha-adv-light-component/blob/main/LICENSE
[license-shield]: https://img.shields.io/github/license/Elwinmage/ha-adv-light-component.svg?style=for-the-badge
[maintenance-shield]: https://img.shields.io/badge/maintainer-Elwinmage-blue.svg?style=for-the-badge
[releases-shield]: https://img.shields.io/github/release/Elwinmage/ha-adv-light-component.svg?style=for-the-badge
[releases]: https://github.com/Elwinmage/ha-adv-light-component/releases
[user_profile]: https://github.com/Elwinmage

