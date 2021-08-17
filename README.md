# Analysis of Weather Data in Oahu

## Overview

This project is about analyzing weather data e.g., temperature, precipitation etc. of Oahu, an island in Hawaii. Specifically, we'll analyze temperature data for the months of June and December in Oahu, in order to determine if the surf and ice cream shop business is sustainable year-round.

## Statistical Data Analysis

In this project, the weather data of Hawaii is stored in a SQLite database i.e., `hawaii.sqlite` which is a light-weight version of PostgreSQL run from local host. SQLAlchemy is used to connect to and query the SQLite database.

At first all the necesary **dependencies** are imported in a Jupyter Notebook `SurfsUp_Challenge` as shown below:

![import dependencies](https://user-images.githubusercontent.com/58155187/129668759-cab5ce8b-9702-45dc-bbce-e7054a73cde7.png)

In the next step, an applications instance and session is created to set up a link between Python and the SQLite database so that we can query and extract required information from the database. The sequence of codes required in this purpose is shown below:

![session create](https://user-images.githubusercontent.com/58155187/129668988-20db2001-d1ef-4f4e-a691-f9c6ff1eae81.png)

An example of the query process is shown below where we extracted the summary information on temperature for the month of December in Oahu.

![Query example](https://user-images.githubusercontent.com/58155187/129669177-0ce4b080-a817-4713-9402-9895411f1614.png)

## Results

We extracted the summary of temperature for the months of June and December in Oahu, as shown below:

### Temperature Summary in June

![june temp](https://user-images.githubusercontent.com/58155187/129669368-9bd6e306-aea2-4f1f-8b65-c946774cb233.png)

### Temperature Summary in December

![dec temp](https://user-images.githubusercontent.com/58155187/129669459-98b21679-540d-4854-975e-e84fe0b61e22.png)

### Key Differences in June and December Temperature 

- Average temperature in June is almost 4 degrees F higher than December;
- The minimum temperature in December is almost 8 degrees F lower than that in June;
- The maximum temperature in December is pretty close to that of June, i.e., 85 and 83 degree fahrenheit respectively.

## Summary

Overall spread of temperatue is pretty close in December and June. So it seems very favorable weather pattern all the year round to start a surf and ice cream shop business in Oahu.



