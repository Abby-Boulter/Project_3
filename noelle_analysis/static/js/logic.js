// Part 1: Create the Earthquake Visualization

// 1.	Get your dataset: https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php

let url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson";
  
  // Getting our GeoJSON data
d3.json(url).then(function(data) {
  // Once we get a response, send the data.features object to the createFeatures function.
  createFeatures(data.features);
  });


// 2. Import and visualize the data by doing the following:

    // Your data markers should reflect the magnitude of the earthquake by their size and 
        // the depth of the earthquake by color. 
        // Earthquakes with higher magnitudes should appear larger, 
        // and earthquakes with greater depth should appear darker in color.

function createFeatures(earthquakeData) {
        // Include popups that provide additional information about the earthquake 
        // when its associated marker is clicked.
    function onEachFeature(feature, layer) {
    layer.bindPopup(`<h3>${feature.properties.place}</h3><hr><p>${new Date(feature.properties.time)}</p>`);
  }

    function createCircleMarker(feature, latlng){

    // Loop through features, and create the markers- size/radius is based on magnitude of EQ
        // color should be darker in color- need to figure out this
    let options = {
        radius:feature.properties.mag*5,
        fillColor: chooseColor(feature.geometry.coordinates[2]),
        color: "white",
        weight: 1,
        opacity: 0.8,
        fillOpacity: 0.35
       } 
       return L.circleMarker(latlng,options);
    }

  // Create a GeoJSON layer that contains the features array on the earthquakeData object.
  // Run the onEachFeature function once for each piece of data in the array.
  let earthquakes = L.geoJSON(earthquakeData, {
    onEachFeature: onEachFeature, pointToLayer: createCircleMarker
  });

  // Send our earthquakes layer to the createMap function/
  createMap(earthquakes);
}

function chooseColor(depth) {
    if (depth > 90 ) return "black";
    else if (depth > 70 ) return "red";
    else if (depth > 50) return "orange";
    else if (depth > 30 ) return "yellow";
    else if (depth > 10 ) return "lime";
    else return "green";
  }

  

// Using Leaflet, create a map that plots all the earthquakes from your 
// dataset based on their longitude and latitude.
function createMap(earthquakes) {

    // Create the base layers.
    let street = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    })
      
    let topo = L.tileLayer('https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png', {
      attribution: 'Map data: &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, <a href="http://viewfinderpanoramas.org">SRTM</a> | Map style: &copy; <a href="https://opentopomap.org">OpenTopoMap</a> (<a href="https://creativecommons.org/licenses/by-sa/3.0/">CC-BY-SA</a>)'
    });
      
    // Create a baseMaps object.
    let baseMaps = {
        "Street Map": street,
        "Topographic Map": topo
    };
      
    // Create an overlay object to hold our overlay.
    let overlayMaps = {
        Earthquakes: earthquakes
    };
      
        // Create our map, giving it the streetmap and earthquakes layers to display on load.
    let myMap = L.map("map", {
        center: [
        37.09, -95.71
        ],
        zoom: 5,
        layers: [street, earthquakes]
    });
      
        // Create a layer control.
        // Pass it our baseMaps and overlayMaps.
        // Add the layer control to the map.
        L.control.layers(baseMaps, overlayMaps, {
          collapsed: false
        }).addTo(myMap);

// Set up the legend.
    let legend = L.control({position: "bottomright"});
    legend.onAdd = function() {
        let div = L.DomUtil.create("div", "info legend");
        let depth = [-10, 10, 30, 50, 70, 90];

  div.innerHTML += "<h1>Latest Earthquakes<br/>" +
    "<h2> Earthquake Depth (m) <h2/>"

    // legend boxes
  for (var i = 0; i < depth.length; i++) {
    div.innerHTML +=
    '<i style="background:' + chooseColor(depth[i] + 1) + '"></i> ' + depth[i] + (depth[i + 1] ? '&ndash;' + depth[i + 1] + '<br>' : '+');
  }

  div.innerHTML += 
    "<br> <br> <b>Data Source </b>: U.S. Geological Survey, All Earthquakes-past week</br>"
  return div;
};
legend.addTo(myMap)
};



