# IoT Air Quality Dashboard

## Description

This website will display historical air quality information for US cities from the year 2000 to 2021, through graphs. The website will track the pollutants Carbon Monoxide, Nitrogen Dioxide, Ozone, and Sulphur Dioxide (CO, NO2, O3, SO2). This will serve to inform the public about the increasing pollution in US cities and hopefully make them more aware of not only their impact but also of the collective impact of the industries they support. This information could also be shown to school children to make them aware of the rapidly changing world they inhabit and the potential threats that come with the status quo lifestyle of the US general population. 

- The stack that we used:
  - Flask and Django → web frameworks
  - SQLite → database
  - leaflet.js → maps 
  - Twilio (free credits),
  - Contextual menu bar (account, map, contact us, analysis, pages)

## Usage

Our website displays a map of the US, with pinpoints on major cities. Click on the cities to display a dashboard of graphs displaying the pollution data. Toggle the individual pollutants and adjust the time scale using the taskbar on the right. 


## Credits

Our data was sourced from a dataset found on Kaggle, with the title US Pollution 2000-2021, by Angle Kim,
which was originally sourced from US EPA data: https://www.kaggle.com/datasets/alpacanonymous/us-pollution-20002021.


## Features

- Users can register by using username and password, they also need to put their city, state, country, name and email information.
- Users can modify their account information.
- Users can access the cleanest city and best-improvement cities
- Users can access maps with pollution visualization on it.
- Users can access graph visualization of the pollution.
- Users can see the historical dashboard by date.
- Users can comment on the graphs.
