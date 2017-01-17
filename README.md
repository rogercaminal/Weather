**Author:**
  Roger Caminal Armadans (roger.caminal@gmail.com)
**created:**  17-01-2017
**Last modified:** 17-01-2017

# Why Weather package?

The idea of this package is to be able to fastly compute and check variables related to weather forecast, for example the windchill out of the temperature and the wind speed.

# Scripts

The package contains different calculators.

## Wind chill calculator

A surface loses heat through conduction, convection, and radiation. The rate of convection depends on both the difference in temperature between the surface and the fluid surrounding it and the velocity of that fluid with respect to the surface. As convection from a warm surface heats the air around it, an insulating boundary layer of warm air forms against the surface. Moving air disrupts this boundary layer, or epiclimate, allowing for cooler air to replace the warm air against the surface. The faster the wind speed, the more readily the surface cools.

The effect of wind chill is to increase the rate of heat loss and reduce any warmer objects to the ambient temperature more quickly. The attempt to maintain a given surface temperature in an environment of faster heat loss results in both the perception of lower temperatures and an actual greater heat loss. In other words, the air 'feels' colder than it is because of the chilling effect of the wind on the skin.

For more information, check [wikipedia](https://en.wikipedia.org/wiki/Wind_chill)

The wind chill can be computed with the following command:

```bash
python wind_chill_calculator.py
```

## Heat index calculator

The human body normally cools itself by perspiration, or sweating. Heat is removed from the body by evaporation of that sweat. However, high relative humidity reduces the evaporation rate. This results in a lower rate of heat removal from the body, hence the sensation of being overheated. This effect is subjective, with different individuals perceiving heat differently for various reasons (such as obesity, metabolic differences, pregnancy, menopause, effects of drugs and/or drug withdrawal); its measurement has been based on subjective descriptions of how hot subjects feel for a given temperature and humidity. This results in a heat index that relates one combination of temperature and humidity to another.

The heat index is an index that combines air temperature and relative humidity, in shaded areas, as an attempt to determine the human-perceived equivalent temperature, as how hot it would feel if the humidity were some other value in the shade. The result is also known as the "felt air temperature" or "apparent temperature".dd

For more information, check [wikipedia](https://en.wikipedia.org/wiki/Heat_index)

```bash
python heat_index_calculator.py
```

## Dew point calculator

The dew point is the temperature at which the water vapor in a sample of air at constant barometric pressure condenses into liquid water at the same rate at which it evaporates. At temperatures below the dew point, the rate of condensation will be greater than that of evaporation, forming more liquid water. The condensed water is called dew when it forms on a solid surface. The condensed water is called either fog or a cloud, depending on its altitude, when it forms in the air.

A high relative humidity implies that the dew point is closer to the current air temperature. Relative humidity of 100% indicates the dew point is equal to the current temperature and that the air is maximally saturated with water. When the moisture content remains constant and temperature increases, relative humidity decreases.

For more information, check [wikipedia](https://en.wikipedia.org/wiki/Dew_point)

The following script computes the dew point given the air temperature and the relative humidity.

```bash
python dew_point_calculator.py
```
