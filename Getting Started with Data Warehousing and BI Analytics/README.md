# Scenario
You are a data engineer hired by a solid waste management company. The company collects and recycles solid waste across major cities in the country of Brazil. The company operates hundreds of trucks of different types to collect and transport solid waste. The company would like to create a data warehouse so that it can create reports like
- total waste collected per year per city
- total waste collected per month per city
- total waste collected per quarter per city
- total waste collected per year per trucktype
- total waste collected per trucktype per city
- total waste collected per trucktype per station per city
You will use your data warehousing skills to design and implement a data warehouse for the company.
# Objectives
In this assignment you will:
- Design a Data Warehouse
- Load data into Data Warehouse
- Write aggregation queries
- Create MQTs
- Create a Dashboard
# Results
The solid waste management company has provied you the sample data they wish to collect.

![image](https://github.com/getnkit/BI-Foundations-with-SQL-ETL-and-Data-Warehousing-Specialization/blob/6671ec380828d846ce243499ea8fcb5cee5b2b5f/Getting%20Started%20with%20Data%20Warehousing%20and%20BI%20Analytics/images/solid-waste-trips-new.png)

You will start your project by designing a Star Schema warehouse by identifying the columns for the various dimension and fact tables in the schema.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Step 1: Design the dimension table MyDimDate, MyDimWaste, and MyDimZone
### Step 2: Design the fact table MyFactTrips
### Step 3: Create the dimension table MyDimDate, MyDimWaste, and MyDimZone
### Step 4: Create the fact table MyFactTrips

![image](https://github.com/getnkit/BI-Foundations-with-SQL-ETL-and-Data-Warehousing-Specialization/blob/2ec62edd604f9f394ea4e47ef70c2306baae8167/Getting%20Started%20with%20Data%20Warehousing%20and%20BI%20Analytics/images/5-MyDimDate.jpg)

![image](https://github.com/getnkit/BI-Foundations-with-SQL-ETL-and-Data-Warehousing-Specialization/blob/2ec62edd604f9f394ea4e47ef70c2306baae8167/Getting%20Started%20with%20Data%20Warehousing%20and%20BI%20Analytics/images/6-MyDimWaste.jpg)

![image](https://github.com/getnkit/BI-Foundations-with-SQL-ETL-and-Data-Warehousing-Specialization/blob/2ec62edd604f9f394ea4e47ef70c2306baae8167/Getting%20Started%20with%20Data%20Warehousing%20and%20BI%20Analytics/images/7-MyDimZone.jpg)

![image](https://github.com/getnkit/BI-Foundations-with-SQL-ETL-and-Data-Warehousing-Specialization/blob/2ec62edd604f9f394ea4e47ef70c2306baae8167/Getting%20Started%20with%20Data%20Warehousing%20and%20BI%20Analytics/images/8-MyFactTrips.jpg)

![image](https://github.com/getnkit/BI-Foundations-with-SQL-ETL-and-Data-Warehousing-Specialization/blob/6671ec380828d846ce243499ea8fcb5cee5b2b5f/Getting%20Started%20with%20Data%20Warehousing%20and%20BI%20Analytics/images/ERD.png)

### Step 5: Load data into the dimension table DimDate, DimTruck, and DimStation
### Step 6: Load data into the fact table FactTrips
### Step 7: Create a grouping sets query using the columns stationid, trucktype, total waste collected.

![image](https://github.com/getnkit/BI-Foundations-with-SQL-ETL-and-Data-Warehousing-Specialization/blob/2ec62edd604f9f394ea4e47ef70c2306baae8167/Getting%20Started%20with%20Data%20Warehousing%20and%20BI%20Analytics/images/13-groupingsets.jpg)

### Step 8: Create a rollup query using the columns year, city, stationid, and total waste collected.

![image](https://github.com/getnkit/BI-Foundations-with-SQL-ETL-and-Data-Warehousing-Specialization/blob/2ec62edd604f9f394ea4e47ef70c2306baae8167/Getting%20Started%20with%20Data%20Warehousing%20and%20BI%20Analytics/images/14-rollup.jpg)

### Step 9: Create a cube query using the columns year, city, stationid, and average waste collected.

![image](https://github.com/getnkit/BI-Foundations-with-SQL-ETL-and-Data-Warehousing-Specialization/blob/2ec62edd604f9f394ea4e47ef70c2306baae8167/Getting%20Started%20with%20Data%20Warehousing%20and%20BI%20Analytics/images/15-cube.jpg)

### Step 10: Create an MQT named max_waste_stats using the columns city, stationid, trucktype, and max waste collected.

![image](https://github.com/getnkit/BI-Foundations-with-SQL-ETL-and-Data-Warehousing-Specialization/blob/35f1cbed26f6bf4b22e547dd892766e1eaacbad0/Getting%20Started%20with%20Data%20Warehousing%20and%20BI%20Analytics/images/16-mqt.jpg)

### Step 11: Create a pie chart that shows the waste collected by truck type.

![image](https://github.com/getnkit/BI-Foundations-with-SQL-ETL-and-Data-Warehousing-Specialization/blob/35f1cbed26f6bf4b22e547dd892766e1eaacbad0/Getting%20Started%20with%20Data%20Warehousing%20and%20BI%20Analytics/images/17-pie.jpg)

### Step 12: Create a bar chart that shows the waste collected station wise.

![image](https://github.com/getnkit/BI-Foundations-with-SQL-ETL-and-Data-Warehousing-Specialization/blob/35f1cbed26f6bf4b22e547dd892766e1eaacbad0/Getting%20Started%20with%20Data%20Warehousing%20and%20BI%20Analytics/images/18-bar.jpg)

### Step 13: Create a line chart that shows the waste collected by month wise.

![image](https://github.com/getnkit/BI-Foundations-with-SQL-ETL-and-Data-Warehousing-Specialization/blob/35f1cbed26f6bf4b22e547dd892766e1eaacbad0/Getting%20Started%20with%20Data%20Warehousing%20and%20BI%20Analytics/images/19-line.jpg)

### Step 14: Create a pie chart that shows the waste collected by city.

![image](https://github.com/getnkit/BI-Foundations-with-SQL-ETL-and-Data-Warehousing-Specialization/blob/35f1cbed26f6bf4b22e547dd892766e1eaacbad0/Getting%20Started%20with%20Data%20Warehousing%20and%20BI%20Analytics/images/20-pie.jpg)






