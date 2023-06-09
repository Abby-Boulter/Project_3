DROP TABLE if exists ed_visits;
DROP TABLE if exists hospitalizations;
DROP TABLE if exists no_heat_days;
DROP TABLE if exists vulnerability;
DROP TABLE if exists hri;

--Create tables and import data--
CREATE TABLE hri (
    county varchar(20) NOT NULL,
    year integer NOT NULL,
    ED_rates float,
    Hosp_rates float,
    SVI float,
    HeatDays float
);
SELECT * FROM hri;

CREATE TABLE ed_visits (
    county varchar(20) NOT NULL,
    year integer NOT NULL,
    ed_rate float
);
SELECT * FROM ed_visits;

CREATE TABLE hospitalizations (
    county varchar(20) NOT NULL,
    year integer NOT NULL,
    hosp_rate float
);
SELECT * FROM hospitalizations;

CREATE TABLE no_heat_days (
    county varchar(20) NOT NULL,
    year integer NOT NULL,
    no_heat_rate float
);
SELECT * FROM no_heat_days;

CREATE TABLE vulnerability (
    county varchar(20) NOT NULL,
    year integer NOT NULL,
    vul_rate float
);
SELECT * FROM vulnerability;
SELECT * FROM hri;
SELECT * FROM ed_visits;
SELECT * FROM hospitalizations;
SELECT * FROM no_heat_days;