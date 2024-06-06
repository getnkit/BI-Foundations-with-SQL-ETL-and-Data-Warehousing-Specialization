CREATE TABLE dimdate(
    dateid INTEGER NOT NULL PRIMARY KEY,
    date DATE,
    year SMALLINT,
    quarter SMALLINT,
    quartername VARCHAR(30),
    month SMALLINT,
    monthName VARCHAR(30),
    day SMALLINT,
    weekday SMALLINT,
    weekdayname VARCHAR(30)
);

CREATE TABLE dimtruck(
    truckid INTEGER NOT NULL PRIMARY KEY,
    trucktype VARCHAR(30)
);

CREATE TABLE dimstation(
    stationid INTEGER NOT NULL PRIMARY KEY,
    city VARCHAR(30)
);

CREATE TABLE facttrips(
    tripid INTEGER NOT NULL PRIMARY KEY,
    dateid INTEGER,
    stationid INTEGER,
    truckid INTEGER,
    wastecollected NUMERIC(9,2),
    FOREIGN KEY (dateid) REFERENCES dimdate(dateid),
    FOREIGN KEY (truckid) REFERENCES dimtruck(truckid),
    FOREIGN KEY (stationid) REFERENCES dimstation(stationid)
);

SELECT 
   s.stationid AS station_id,
   t.trucktype AS truck_type,
   SUM(f.wastecollected) AS total_waste
FROM 
   facttrips f 
INNER JOIN dimstation s
   ON f.stationid = s.stationid
INNER JOIN dimtruck t
   ON f.truckid = t.truckid
GROUP BY 
GROUPING SETS (station_id, truck_type);

SELECT 
   d.year AS year,
   s.city AS city,
   s.stationid AS station_id,
   SUM(f.wastecollected) AS total_waste
FROM 
   FactTrips f 
INNER JOIN dimdate d 
   ON f.dateid = d.dateid
INNER JOIN dimstation s 
   ON f.stationid = s.stationid
GROUP BY 
ROLLUP (year, city, station_id);

