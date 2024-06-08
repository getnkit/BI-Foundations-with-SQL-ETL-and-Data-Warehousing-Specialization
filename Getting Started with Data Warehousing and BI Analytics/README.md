# Solid Waste Data Warehousing and Analytics with PostgreSQL and Looker Studio

## Scenario
You are a data engineer hired by a solid waste management company. The company collects and recycles solid waste across major cities in the country of Brazil. The company operates hundreds of trucks of different types to collect and transport solid waste. The company would like to create a data warehouse so that it can create reports like
- total waste collected per year per city
- total waste collected per month per city
- total waste collected per quarter per city
- total waste collected per year per trucktype
- total waste collected per trucktype per city
- total waste collected per trucktype per station per city
You will use your data warehousing skills to design and implement a data warehouse for the company.

## Objectives
In this assignment you will:
- Design a Data Warehouse
- Load data into Data Warehouse
- Write aggregation queries
- Create MQTs
- Create a Dashboard

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Project Overview
This project will involve designing a Star Schema architecture for data storage, followed by creating the data warehouse structure, loading data, analyzing it with various queries, creating MQTs for improved processing efficiency, and finally, presenting the data through a dashboard with various types of charts.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Relevant Theories and Concepts
### Data Models
#### Conceptual Data Model
- **Objective:** To provide an overview of the data relevant to the business, emphasizing the relationships between entities (the things we are interested in storing data about).
- **Characteristics:** It is a high-level model that does not concern itself with the technical details of data storage.
- **Creation method:** Often uses an Entity-Relationship Diagram (ERD) to illustrate the relationships between entities.

In this project, I will identify key entities such as dateid, truckid, stationid, tripid and the relationships between them.

#### Logical Data Model
- **Objective:** Outline the structure of the data to be stored in the database, focusing on tables, columns, and the relationships between tables.
- **Characteristic:** It is a more detailed model than the Conceptual Data Model but does not concern itself with the finer details of implementation.
- **Creation method:** Often, the Relational Model is used for design, which represents tables and relationships in the form of primary keys and foreign keys.

In this project, I will design a Star Schema with MyFactTrips as the Fact Table and MyDimDate, MyDimTruck, and MyDimStation as Dimension Tables.

#### Physical Data Model
- **Objective:** To detail the storage of actual data in the database system, specifying data types, data lengths, constraints, indexes, and other technical details.
- **Characteristic:** The most detailed model, specific to the chosen database system (in this case, PostgreSQL).
- **Creation method:** Typically uses SQL DDL (Data Definition Language) to create tables and define various constraints.

In this project, I will use SQL DDL in PostgreSQL to create tables, define data types, constraints, and indexes as designed.

### Data Warehousing
- **Concept:** A Data Warehouse is a database system designed specifically for data analysis, not for real-time transactions. It gathers data from various sources, such as operational databases, log files, or other external sources. The data is then transformed into a consistent format and stored in a structure suitable for analysis, such as a Star Schema or Snowflake Schema.
### Star Schema Architecture
- **Fact Table:** The main table that stores the quantitative data we want to analyze, such as the amount of garbage collected on each trip.

- **Dimension Tables:** Tables that store qualitative data used to describe the information in the fact table, such as date, time, location, and truck type.
### Aggregation Queries
- **Concept:** Aggregation Queries are queries used to calculate statistical values from data, such as sum, average, maximum, and minimum.

- **Types:** This project will utilize Grouping Sets, Rollup, and Cube queries to analyze data across various dimensions.

- **Importance:** Aggregation Queries help summarize large datasets into easily understandable formats, providing a clearer overview of the data.
### Materialized Query Tables (MQT):
- **Concept:** MQTs are tables that store the results of queries in advance to improve the efficiency of subsequent queries.

- **Benefits:** They help reduce the processing time for complex queries and decrease the load on the database system.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Implementation
The solid waste management company has provied you the sample data they wish to collect.

![image](https://github.com/getnkit/BI-Foundations-with-SQL-ETL-and-Data-Warehousing-Specialization/blob/6671ec380828d846ce243499ea8fcb5cee5b2b5f/Getting%20Started%20with%20Data%20Warehousing%20and%20BI%20Analytics/images/solid-waste-trips-new.png)

You will start your project by designing a Star Schema warehouse by identifying the columns for the various dimension and fact tables in the schema.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Step 1: Design the dimension table MyDimDate, MyDimTruck, and MyDimStation
- **MyDimDate:** This table will store information about time, such as day, month, year, week, etc. to be used in analyzing data over different time periods.
- **MyDimTruck:** This table will store information about garbage trucks, such as truckid and trucktype to be used in analyzing the amount of garbage collected by truck type.
- **MyDimStation:** This table will store information about zones or areas, such as stationid and city to be used in analyzing the amount of garbage by area.
### Step 2: Design the fact table MyFactTrips
- **MyFactTrips:** This table will be the heart of the Data Warehouse, storing information about each garbage collection trip, such as the date of collection, the station where it was collected, the type of waste, the truck used for collection, and the amount of waste collected. It will be linked to various dimension tables to enable analysis of the data from multiple perspectives.
### Step 3: Create the dimension table MyDimDate, MyDimTruck, and MyDimStation

![image](https://github.com/getnkit/BI-Foundations-with-SQL-ETL-and-Data-Warehousing-Specialization/blob/2ec62edd604f9f394ea4e47ef70c2306baae8167/Getting%20Started%20with%20Data%20Warehousing%20and%20BI%20Analytics/images/5-MyDimDate.jpg)

![image](https://github.com/getnkit/BI-Foundations-with-SQL-ETL-and-Data-Warehousing-Specialization/blob/2ec62edd604f9f394ea4e47ef70c2306baae8167/Getting%20Started%20with%20Data%20Warehousing%20and%20BI%20Analytics/images/6-MyDimWaste.jpg)

![image](https://github.com/getnkit/BI-Foundations-with-SQL-ETL-and-Data-Warehousing-Specialization/blob/2ec62edd604f9f394ea4e47ef70c2306baae8167/Getting%20Started%20with%20Data%20Warehousing%20and%20BI%20Analytics/images/7-MyDimZone.jpg)

### Step 4: Create the fact table MyFactTrips

![image](https://github.com/getnkit/BI-Foundations-with-SQL-ETL-and-Data-Warehousing-Specialization/blob/2ec62edd604f9f394ea4e47ef70c2306baae8167/Getting%20Started%20with%20Data%20Warehousing%20and%20BI%20Analytics/images/8-MyFactTrips.jpg)

![image](https://github.com/getnkit/BI-Foundations-with-SQL-ETL-and-Data-Warehousing-Specialization/blob/6671ec380828d846ce243499ea8fcb5cee5b2b5f/Getting%20Started%20with%20Data%20Warehousing%20and%20BI%20Analytics/images/ERD.png)

### Step 5: Load data into the dimension table DimDate, DimTruck, and DimStation
### Step 6: Load data into the fact table FactTrips
### Step 7: Create a grouping sets query using the columns stationid, trucktype, total waste collected.

**Grouping Sets:** Use GROUPING SETS to create a query that combines the results of multiple group by sets, such as finding the total amount of garbage by station, by truck type, and by both combined.

![image](https://github.com/getnkit/BI-Foundations-with-SQL-ETL-and-Data-Warehousing-Specialization/blob/2ec62edd604f9f394ea4e47ef70c2306baae8167/Getting%20Started%20with%20Data%20Warehousing%20and%20BI%20Analytics/images/13-groupingsets.jpg)

### Step 8: Create a rollup query using the columns year, city, stationid, and total waste collected.

**Rollup:** Use ROLLUP to create a query that shows subtotals and grand totals of data, such as finding the total amount of garbage by year, city, station, and the overall total.

![image](https://github.com/getnkit/BI-Foundations-with-SQL-ETL-and-Data-Warehousing-Specialization/blob/2ec62edd604f9f394ea4e47ef70c2306baae8167/Getting%20Started%20with%20Data%20Warehousing%20and%20BI%20Analytics/images/14-rollup.jpg)

### Step 9: Create a cube query using the columns year, city, stationid, and average waste collected.

**Cube:** Use CUBE to create a query that shows subtotals and grand totals for all possible combinations of data, such as finding the average amount of garbage by year, city, station, and all possible combinations.

![image](https://github.com/getnkit/BI-Foundations-with-SQL-ETL-and-Data-Warehousing-Specialization/blob/2ec62edd604f9f394ea4e47ef70c2306baae8167/Getting%20Started%20with%20Data%20Warehousing%20and%20BI%20Analytics/images/15-cube.jpg)

### Step 10: Create an MQT named max_waste_stats using the columns city, stationid, trucktype, and max waste collected.

Create Materialized Query Tables (MQTs) to store the results of frequently used queries to improve the efficiency of querying data in subsequent times. For example, create an MQT that stores the maximum garbage amount by city, station, and truck type.

![image](https://github.com/getnkit/BI-Foundations-with-SQL-ETL-and-Data-Warehousing-Specialization/blob/35f1cbed26f6bf4b22e547dd892766e1eaacbad0/Getting%20Started%20with%20Data%20Warehousing%20and%20BI%20Analytics/images/16-mqt.jpg)

### Step 11: Create a pie chart that shows the waste collected by truck type.

![image](https://github.com/getnkit/BI-Foundations-with-SQL-ETL-and-Data-Warehousing-Specialization/blob/35f1cbed26f6bf4b22e547dd892766e1eaacbad0/Getting%20Started%20with%20Data%20Warehousing%20and%20BI%20Analytics/images/17-pie.jpg)

### Step 12: Create a bar chart that shows the waste collected station wise.

![image](https://github.com/getnkit/BI-Foundations-with-SQL-ETL-and-Data-Warehousing-Specialization/blob/35f1cbed26f6bf4b22e547dd892766e1eaacbad0/Getting%20Started%20with%20Data%20Warehousing%20and%20BI%20Analytics/images/18-bar.jpg)

### Step 13: Create a line chart that shows the waste collected by month wise.

![image](https://github.com/getnkit/BI-Foundations-with-SQL-ETL-and-Data-Warehousing-Specialization/blob/35f1cbed26f6bf4b22e547dd892766e1eaacbad0/Getting%20Started%20with%20Data%20Warehousing%20and%20BI%20Analytics/images/19-line.jpg)

### Step 14: Create a pie chart that shows the waste collected by city.
 
![image](https://github.com/getnkit/BI-Foundations-with-SQL-ETL-and-Data-Warehousing-Specialization/blob/35f1cbed26f6bf4b22e547dd892766e1eaacbad0/Getting%20Started%20with%20Data%20Warehousing%20and%20BI%20Analytics/images/20-pie.jpg)

## Summary
This project will enable the waste management company to utilize data for making more informed decisions and improving operational efficiency. This includes optimizing collection routes, allocating garbage trucks effectively, enhancing recycling efficiency, and minimizing environmental impact.



