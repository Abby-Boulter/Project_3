// Creating the map object
let myMap = L.map("map", {
  center: [34.4537, -112.0693],
  zoom: 7
});

// Adding the tile layer
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(myMap);

// Load the GeoJSON data.
let geoData = 'https://raw.githubusercontent.com/Abby-Boulter/Project_3/main/arcive_analysis/dakota_analysis/Counties%20maps/arizona-with-county-boundaries_1085.geojson'


let geojson;

//Get data with D3
d3.json(geoData).then(function(data){

    //Create choropleth layer
    geojson = L.choropleth(data, {

        //Define value for choropleth
        valueProperty: "XHD_2021",
        //Color scale based on # of values
        scale: ["#ffffcc", "#b10026"],
        
        //Number of breaks in step range
        steps: 10,

    // q for quartile
    mode: "q",
    style: {
      // Border color
      color: "#fff",
      weight: 1,
      fillOpacity: 0.8
    },

    // Binding a popup to each layer
    //RELABEL AS NEEDED
    onEachFeature: function(feature, layer) {
        layer.bindPopup("<strong>" + feature.properties.NAME + "</strong><br /><br />Estimated employed population with children age 6-17: " +
          feature.properties.DP03_16E + "<br /><br />Estimated Total Income and Benefits for Families: $" + feature.properties.DP03_75E);
      }
    });

      // Set up the legend.
  let legend = L.control({ position: "bottomright" });
  legend.onAdd = function() {
    let div = L.DomUtil.create("div", "info legend");
    let limits = geojson.options.limits;
    let colors = geojson.options.colors;
    let labels = [];

      // Add the minimum and maximum.
      let legendInfo = "<h1>Extreme Heat Days</h1>" +
      "<div class=\"labels\">" +
        "<div class=\"min\">" + limits[0] + "</div>" +
        "<div class=\"max\">" + limits[limits.length - 1] + "</div>" +
      "</div>";

    div.innerHTML = legendInfo;

    limits.forEach(function(limit, index) {
      labels.push("<li style=\"background-color: " + colors[index] + "\"></li>");
    });

    div.innerHTML += "<ul>" + labels.join("") + "</ul>";
    return div;
  };

  // Adding the legend to the map
  legend.addTo(myMap);
 
});