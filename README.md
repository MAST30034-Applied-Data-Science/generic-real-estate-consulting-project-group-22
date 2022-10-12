# Generic Real Estate Consulting Project

## Meet Our Team

- Team Number: 22
- Team Members: 
1. Daozhu Wu 1170374
2. Anhui Situ 1173962
3. Jingchen Shi 1135824
4. Xiaohan Deng 1166088
5. Zhaoyang Zhang 1118906


## Research Goal

Our project aims to predict rental prices of properties across Victoria for the future 3 years and investigate the livability and affordability of our chosen granularity Statistical Area 2(SA2). Moreover, we attempt to find out the top 10 most potential SA2 with the greatest predicted rent growth rate and evaluate multiple essential features that cause a specific region to have high growth rate.

## How to use our code

**To download raw data sets, please visit the `scripts` directory and run the files in order:**

*[google drive link]() to store some raw data*(to save time, since some data requires few hours to run notebook and get)

1. run ```external.ipynb``` to download some external dataset
2. run ```scrape.ipynb``` to scrape the property data from the Domain website (this would take around 2 hours to scrape, so it was added to the google drive to save the time for others. After extraction, put ```example.json``` into ```/data/raw``` directory)
3. To obtain coordinates of train station:
   - go to website http://overpass-turbo.eu/
   - copy the code below and past it into the code box on left
     ```
     [out:json][timeout:600]; // gather results
     {{geocodeArea:Victoria}}->.searchArea;
     (
      // query part for: “building=train_station”
      node[building=train_station](area.searchArea);
      way[building=train_station](area.searchArea);
      relation[building=train_station](area.searchArea);
     );
     // print results
     out body;
     >;
     out skel qt; 
     ```
   - press press ```run``` button on the top left
   - press ```export``` button on top left
   - press ```download``` button right of ```GeoJSON```
   - rename the file as ```train.geojson``` and put it under the path ```/data/raw```

4. To obtain coordinates of shopping center:
   - go to website http://overpass-turbo.eu/
   - copy the code below and paste it into the code box on left
   
   ```
   [out:json][timeout:600];
   // gather results
   {{geocodeArea:Victoria}}->.searchArea;
   (
   // query part for: “shop=mall”
   node[shop=mall](area.searchArea);
   way[shop=mall](area.searchArea);
   relation[shop=mall](area.searchArea);
   );
   // print results
   out body;
   >;
   out skel qt;
   ```
  
   - press ```run``` button on the top left
   - press ```export``` button on top left
   - press ```download``` button right of ```GeoJSON```
   - rename the file as ```shopping.geojson``` and put it under the path ```/data/raw```


**To preprocess our data sets, please visit the `notebooks` directory and run the files in order:**

1. run ```preprocess.ipynb```, this does preprocess to postcode, property, unemployment, and school datasets.
2. run ```population_preprocess.ipynb```, this does preprocess to population dataset
3. run ```income_preprocess.ipynb```, this does preprocess to income dataset
4. get driving route data and apply preprocess:
	 - run ```overpass.ipynb```
	 
   _The following 4 notebook would require an api key from_ ***openrouteservice***
   
   - run ```ors_cbd.ipynb```
   
	_The following 3 will require a lot of time to download, so we also upload an version of dataset to googledrive, after extracting put ```property_school.csv```, ```property_sc.csv```, and ```property_train.csv``` under ```/data/curated``` directory_
   
	  - run ```openrouteservice_school.ipynb```
    - run ```ors_sc.ipynb```
    - run ```ors_train.ipynb```
    - run ```property_preprocess.ipynb``` to merge route data and other external datasets for each property

**To analyse and visualise our data sets, please visit the `notebooks` directory and run the files in order:**

1. run ```ors_route_visualisation.ipynb``` to get visualizations of the routes
2. run ```analyze.ipynb``` to visualize relationship between rental price and other features
3. run ```population_analyze.ipynb```, analyze and predict future population for each suburb
4. run ```income_unemployment_predict.ipynb```, analyze and predict the number of jobs, income rate, and unemployment rate of each suburb.
5. run ```linear_predict.ipynb``` to predict suburb with highest rent price growth with linear model
6. run ```rf-model.ipynb``` to predict suburb with highest rent price growth with random forest
7. run ```livable_suburb_avg.ipynb``` to find most livable suburbs
8. run ```livable_suburb_rank.ipynb``` to find most livable suburbs
9. run ```affordable_suburb.ipynb``` to find most affordable suburbs
10. run ```rent_all.ipynb``` to find the mean rental price of each SA2
11. run ```visualization.ipynb``` to draw choropleth maps to show the mean population, income, property rental price of each zone(SA2) in Victoria

**To discover our overall findings of our project, please visit the `notebooks` directory**

Check ```summary.ipynb```
