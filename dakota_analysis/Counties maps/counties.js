// Creating the map object
let myMap = L.map("map", {
  center: [34.4537, -112.0693],
  zoom: 7
});

// Adding the tile layer
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(myMap);

//Array to hold all AZ counties info
azCounties = [];

//read geojson (reference https://www.freecodecamp.org/news/how-to-read-json-file-in-javascript/)
// fetch('AZ-04-arizona-counties.json')
//   .then((response) => response.json())
//   .then((geojson) => console.log(geojson))

