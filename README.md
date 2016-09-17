# Salary-Predictor

Contributers: Hung-wei Chuang, Edward Doyle, Tony Zhao, Austen Zhu

This program is intended to predict the median salary of a software developer in a specific county/city within the United States. Some of the variables used in our algorithm are land area, population, and average salary of the location's state. Below is some sample data. Actual data is taken from Glassdoor.com and other sources.


San Francisco
> Predicted: $115,995.48

> Actual: $110,554

San Diego
> Predicted: $95,443.30

> Actual: $92,016

Ventura
> Predicted: $89,235.85

> Actual: $87,279

Houston
> Predicted: $68,313.08

> Actual: $75,053

St. Louis
> Predicted: $87,469.17

> Actual: $75,000

Somserset
> Predicted: $95,705.28

> Actual: $94,946




Predictor.py
------------
This is the main component. When you run this program, you will be prompted for the name of a location. The first letter should be capitalized, and extra information such as "County" or "City" or "Borrough" should be ommited. A typical request would be "Marin" or "San Francisco." Then, the predicted salary and Glassdoor data should be displayed.

Dataset.py
-----------
Data scraped and written to this file to prevent slow runtime. In contrast with Glassdoor.py, in which we pull data only when needed because the size of the data is overwhelming, the data for the average salaries of the 50 states is relatively small and always needed.

Glassdoor.py
-----------
Gives the information of companies near a specific location.

Census.py
-----------
Allows user to pull Census data when needed.
