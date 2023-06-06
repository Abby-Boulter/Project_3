//Array to hold all AZ counties info
azCounties = [];


//Arrays to hold county info 
apache =  [];
cochise = [];
coconino = [];
gila = [];
graham = [];
greenlee = [];
laPaz = [];
maricopa = [];
mojave = [];
navajo = [];
pima = [];
pinal = [];
sataCruz = [];
yavapai = [];
yuma = [];







// Creating the map object
let myMap = L.map("map", {
    center: [34.4537, -112.0693],
    zoom: 7
  });
  
  // Adding the tile layer
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  }).addTo(myMap);
  
//   // Use this link to get the GeoJSON data.
//   let link = "https://2u-data-curriculum-team.s3.amazonaws.com/dataviz-classroom/v1.1/15-Mapping-Web/nyc.geojson";
  
//   // Getting our GeoJSON data
//   d3.json(link).then(function(data) {
//     // Creating a GeoJSON layer with the retrieved data
//     L.geoJson(data).addTo(myMap);
//   });
  