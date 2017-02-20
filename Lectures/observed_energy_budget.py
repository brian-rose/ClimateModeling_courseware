'''
This module sets values for the observed global mean planetary energy budget
Based on values reported in Trenberth and Fasullo (2012) Surv. Geophys.

All values in units of W/m2

Four dictionaries are defined:
- SW (the shortwave radiation budget)
- LW (the longwave radiation budget)
- Turbulent (surface turbulent fluxes)
- NetAbsorbed (the net heating rate for atmosphere, surface, and planet)

This module is used in the Lecture Notes for ATM 623, Climate Modeling

Brian Rose
University at Albany
brose@albany.edu
'''

SW = {}
SW['Incoming Solar Radiation'] = 341.3
SW['Reflected by Clouds and Atmosphere'] = 78.9
SW['Reflected by Surface'] = 23.
SW['Reflected Solar Radiation'] = (SW['Reflected by Clouds and Atmosphere'] + 
                                   SW['Reflected by Surface'])
SW['Absorbed by Surface'] = 161.
SW['Absorbed by Atmosphere'] = (SW['Incoming Solar Radiation'] - 
                                SW['Reflected Solar Radiation'] - 
                                SW['Absorbed by Surface'])
SW['Absorbed Solar Radiation'] = (SW['Incoming Solar Radiation'] -
                                      SW['Reflected Solar Radiation'])

LW = {}
LW['Surface Radiation'] = 396.
LW['Downwelling Radiation'] = 333.
LW['Emitted by Atmosphere'] = 187. + 29.5
LW['Absorbed by Atmosphere'] = 374.
LW['Atmospheric Window'] = 22.
LW['Outgoing Longwave Radiation'] = (LW['Emitted by Atmosphere'] + 
                                     LW['Atmospheric Window'])

Turbulent = {}
Turbulent['Thermals'] = 17.1
Turbulent['Evapotranspiration'] = 80.

NetAbsorbed = {}
NetAbsorbed['Atmosphere'] = (SW['Absorbed by Atmosphere'] +
                             LW['Absorbed by Atmosphere'] -
                             LW['Downwelling Radiation'] - 
                             LW['Emitted by Atmosphere'] + 
                             Turbulent['Thermals'] + 
                             Turbulent['Evapotranspiration'])
NetAbsorbed['Surface'] = (SW['Absorbed by Surface'] + 
                          LW['Downwelling Radiation'] - 
                          LW['Surface Radiation'] - 
                          Turbulent['Thermals'] - 
                          Turbulent['Evapotranspiration'])
NetAbsorbed['Planet'] = (SW['Absorbed Solar Radiation'] -
                         LW['Outgoing Longwave Radiation'])