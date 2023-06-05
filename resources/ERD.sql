DROP TABLE if exists ed_visits;
DROP TABLE if exists mortality;
DROP TABLE if exists no_heat_days;
DROP TABLE if exists vulnerability;

--Create tables and import data--
CREATE TABLE ed_visits (
    county varchar(20) NOT NULL,
    year integer NOT NULL,
    county_id varchar(10) NOT NULL,
    number_of_visits integer NOT NULL
);
SELECT * FROM ed_visits;

CREATE TABLE "mortality" (
    county varchar(20) NOT NULL,
    year integer NOT NULL,
    county_id varchar(10) NOT NULL,
    number_of_deaths integer NOT NULL,
	FOREIGN KEY (county) REFERENCES ed_visits(county)
);
SELECT * FROM mortality;

CREATE TABLE "no_heat_days" (
    county varchar(20) NOT NULL,
    year integer NOT NULL,
    county_id varchar(10) NOT NULL,
    days_over_90 integer NOT NULL,
	FOREIGN KEY (county) REFERENCES ed_visits(county)
);
SELECT * FROM no_heat_days;

CREATE TABLE "vulnerability" (
    county varchar(20) NOT NULL,
    year integer NOT NULL,
    county_id varchar(10) NOT NULL,
    vulnerability_percentage integer NOT NULL,
	FOREIGN KEY (county) REFERENCES ed_visits(county)
);
SELECT * FROM vulnerability;