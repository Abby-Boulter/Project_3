DROP TABLE if exists hri;
DROP TABLE if exists ed_visits;
DROP TABLE if exists hospitalizations;
DROP TABLE if exists no_heat_days;
DROP TABLE if exists vulnerability;

--Create tables and import data--
CREATE TABLE hri (
    county varchar(20) NOT NULL,
    year integer NOT NULL,
    ed_rates integer NOT NULL UNIQUE,
    hosp_rates integer NOT NULL UNIQUE,
    svi integer NOT NULL UNIQUE,
    headdays integer NOT NULL UNIQUE
);
SELECT * FROM hri;

CREATE TABLE ed_visits (
    county varchar(20) NOT NULL,
    year integer NOT NULL,
    ed_rates integer NOT NULL,
    FOREIGN KEY (ed_rates) REFERENCES hri(ed_rates)
);
SELECT * FROM ed_visits;

CREATE TABLE hospitalizations (
    county varchar(20) NOT NULL,
    year integer NOT NULL,
    hosp_rates integer NOT NULL,
	FOREIGN KEY (hosp_rates) REFERENCES hri(hosp_rates)
);
SELECT * FROM hospitalizations;

CREATE TABLE "no_heat_days" (
    county varchar(20) NOT NULL,
    year integer NOT NULL,
    headdays integer NOT NULL,
    FOREIGN KEY (headdays) REFERENCES hri(headdays)
);
SELECT * FROM no_heat_days;

CREATE TABLE "vulnerability" (
    county varchar(20) NOT NULL,
    year integer NOT NULL,
    svi integer NOT NULL,
    FOREIGN KEY (svi) REFERENCES hri(svi)
);
SELECT * FROM vulnerability;