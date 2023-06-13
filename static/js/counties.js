// Creating the map object
var myMap = L.map("map", 
{
  center: [34.4537, -112.0693],
  zoom: 7
});

// Adding the tile layer
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(myMap);


//Arizona county line information from https://cartographyvectors.com/map/1085-arizona-with-county-boundaries
//<<<<<<< HEAD:dakota_analysis/Counties maps/counties.js
let link = 'http://127.0.0.1:5000/countiesjson'
//=======
// let link = 'https://github.com/Abby-Boulter/Project_3/blob/main/resources/arizona-with-county-boundaries_1085.geojson'
//>>>>>>> 5fe6fb7f370fdaee05d85041e348f34224cc2ffa:arcive_analysis/dakota_analysis/Counties maps/counties.js

// Getting our GeoJSON data
d3.json(link).then(function(data) {
  // Creating a GeoJSON layer with the retrieved data
  L.geoJson(data, {
    // Styling each feature (in this case, a neighborhood)
    style: function(feature) {
      return {
        color: "black",
        // Call the chooseColor() function to decide which color to color our neighborhood. (The color is based on the borough.)
        fillColor: 'blue',
        fillOpacity: 0.5,
        weight: 1.5
      };
    },
    // This is called on each feature.
    onEachFeature: function(feature, layer) {
      // Set the mouse events to change the map styling.
      layer.on({
        // When a user's mouse cursor touches a map feature, the mouseover event calls this function, which makes that feature's opacity change to 90% so that it stands out.
        mouseover: function(event) {
          layer = event.target;
          layer.setStyle({
            fillOpacity: 0.9
          });
        },
        // When the cursor no longer hovers over a map feature (that is, when the mouseout event occurs), the feature's opacity reverts back to 50%.
        mouseout: function(event) {
          layer = event.target;
          layer.setStyle({
            fillOpacity: 0.5
          });
        },
      });
      // Giving each feature a popup with information that's relevant to it
      layer.bindPopup("<h1>" + feature.properties.name + "</h1>");

    }
  }).addTo(myMap);
});