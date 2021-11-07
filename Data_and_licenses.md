# Data and licenses

Country data (in /tehtävät/data/maatiedot.json):  

Main data source: The World Bank, World Development Indicators 
License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
Terms of use: https://data.worldbank.org/summary-terms-of-use

Secondary data source: restcountries.eu 
Url: https://restcountries.eu/rest/v2/all
License: [MPL 2.0](https://www.mozilla.org/en-US/MPL/2.0/)

Secondary data source: Statistics Finland
Url: https://data.stat.fi/api/classifications/v2/classifications/valtio_1_20120101/classificationItems?content=data&meta=max&lang=fi
License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

Modifications made by Mikko Kotola: 
- Started with World Bank indicator data
- Filtered only a subset of countries, indicators and years
- Dropped keys unit, obs_status, decimal
- Augmented data with numericCode and flag from restcountries.eu
- Augmented data with Finnish country names (nameFinnish) from Statistics Finland