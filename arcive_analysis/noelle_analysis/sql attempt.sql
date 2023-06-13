DROP TABLE IF EXISTS heat CASCADE;


-- create a new table
create table heat (
	county varchar(30) not NULL,
	year int,
	ed_rate int,
	hosp_rate INT,
	vul_rate INT,
	ext_heat_days INT,
	ed_rate35 INT,
	index INT, 
	PRIMARY KEY (index)
);

-- query all fields from the table
SELECT *
FROM heat