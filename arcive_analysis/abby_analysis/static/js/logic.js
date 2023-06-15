function chooseColor(value) {
    if (value == "Brooklyn") return "yellow";
    else if (value == "Bronx") return "red";
    else if (value == "Manhattan") return "orange";
    else if (value == "Queens") return "blue";
    else return "black";
  }
  let link = 
  // Getting our GeoJSON data
  d3.json(link).then(function(data) {
    // Creating a GeoJSON layer with the retrieved data
    L.geoJson(data, {
      // Styling each feature (in this case, a neighborhood)
      style: function(feature) {
        return {
          color: "white",
          // Call the chooseColor() function to decide which color to color our neighborhood. (The color is based on the borough.)
          fillColor: chooseColor(feature.properties.borough),
          fillOpacity: 0.5,
          weight: 1.5
        };
      },





//       session = Session(engine)

//       #Return a DataFrame to buid a choropleth map
//       df = session.query(ed_visit2.GeogID, ed_visit2.year, ed_visit2.ed_rate)
  
//       session.close()
  
//       data = [dict(type='choropleth', 
//               locations = df['GeogID'].astype(str),
//               z=df['ED_rates'].astype(float),
//               geojson='../data/arizona-with-county-boundaries_1085.geojson')]
//       steps = []
  
//       for i in range(len(data)):
//           step = dict(method='restyle',
//                       args=['visible', [False] * len(data)],
//                       label='Year {}'.format(i + 2011))
//           step['args'][1][i] = True
//           steps.append(step)
  
//   sliders = [dict(active=0, pad={"t": 1}, steps=steps)]



//////////////////////////////
////////LINE GRAPH///////////
/////////////////////////////

// Initializes the page with a default plot
function init() {
    data = [{
      x: [1, 2, 3, 4, 5],
      y: [1, 2, 4, 8, 16] }];
  
    Plotly.newPlot("plot", data);
  }
  
  // Call updatePlotly() when a change takes place to the DOM
  d3.selectAll("#selDataset").on("change", updatePlotly);
  
  // This function is called when a dropdown menu item is selected
  function updatePlotly() {
    // Use D3 to select the dropdown menu
    let dropdownMenu = d3.select("#selDataset");
    // Assign the value of the dropdown menu option to a variable
    let dataset = dropdownMenu.property("value");
    console.log("Dataset: ", dataset)
    
    // Initialize x and y arrays
    let x = [];
    let y = [];
  
    if (dataset === 'dataset1') {
      x = [1, 2, 3, 4, 5];
      y = [1, 2, 4, 8, 16];
    }
  
    else if (dataset === 'dataset2') {
      x = [10, 20, 30, 40, 50];
      y = [1, 10, 100, 1000, 10000];
    }
  
    // Note the extra brackets around 'x' and 'y'
    Plotly.restyle("plot", "x", [x]);
    Plotly.restyle("plot", "y", [y]);
  }
  
  init();