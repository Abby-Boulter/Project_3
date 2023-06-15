
// Creating the map object
let myMap = L.map("map", 
{
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

// The function that will determine the color of a county
function chooseColor(ext_heat_days) {
  if (ext_heat_days < 11) return "yellow";
  else if (ext_heat_days < 21) return "red";
  else if (ext_heat_days < 31) return "orange";
  else if (ext_heat_days < 41) return "green";
  else if (ext_heat_days < 51) return "purple";
  else return "black";
}
//Get data with D3
d3.json(geoData).then(function(data){

    //Create Chloropleth layer
    L.geoJson(data, {
      style: function(feature) {
        return {
          color: "white",
          // Call the chooseColor() function to decide which color to color our neighborhood. (The color is based on the borough.)
          fillColor: chooseColor(feature.properties.borough),
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
          // When a feature (neighborhood) is clicked, it enlarges to fit the screen.
          click: function(event) {
            myMap.fitBounds(event.target.getBounds());
          }
        });
        // Giving each feature a popup with information that's relevant to it
        layer.bindPopup("<h1>" + feature.properties.neighborhood + "</h1> <hr> <h2>" + feature.properties.borough + "</h2>");
  
      }
    }).addTo(myMap);
  });

      // Set up the legend.
  let legend = L.control({ position: "bottomright" });
  legend.onAdd = function() {
    let div = L.DomUtil.create("div", "info legend");
    let limits = geojson.options.limits;
    let colors = geojson.options.colors;
    let labels = [];

      // Add the minimum and maximum.
      let legendInfo = "<h1>RELABEL AS NEEDED</h1>" +
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