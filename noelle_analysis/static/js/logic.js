// 1.	Get your dataset: 

let myMap = L.map("map", {
  center: [-34.0, 111.1],
  zoom: 7
});

// Adding the tile layer
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(myMap);

// let url = "https://ephtracking.cdc.gov/apigateway/api/v1/getCoreHolder/423/82/1/4/1/2021,2020,2019,2018,2017,2016,2015,2014,2013,2012,2011/0/0?TemperatureHeatIndexId=1&RelativeThresholdId=1";

// d3.json(url).then(function(response) {

//  console.log(response);
//  features = response.tableResult;

//});

// Load the GeoJSON data.
let geoData = "https://2u-data-curriculum-team.s3.amazonaws.com/dataviz-classroom/v1.1/15-Mapping-Web/ACS-ED_2014-2018_Economic_Characteristics_FL.geojson";

let geojson;

// Get the data with d3.
d3.json(geoData).then(function(data) {

  console.log(data);