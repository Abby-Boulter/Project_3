const ED35 = 'data/EDRates35_wide.csv'
// Fetch the JSON data and console log it

d3.csv(ED35).then(function(data) {
  onsole.log(data);
  });

function buildBarChart(sample) {

    // Use D3 to retrieve all of the data
    d3.json(ED35).then((data) => { 
        year_selected = //needs to be selected from drop down

        county_year = ['Apache','Cochise','Coconino','Gila','Graham','Greenlee','La Paz','Maricopa','Mohave','Navajo','Pima','Pinal','Santa Cruz','Yavapai','Yuma']
        values_year = ED35.
        // Set up the trace for the bar chart
        let trace = {
            x: county,
            y: EDrates,
            text: labels,
            type: "bar",
            orientation: "h"
        };

        // Setup the layout
        let layout = {
            title: "Counties ED 35 Rates"
        };

        // Call Plotly to plot the bar chart
        Plotly.newPlot("bar", [trace], layout)
    });
};

var data = [
    {
      x: [ED35.counties.unique()],
      y: [20, 14, 23],
      type: 'bar'
    }
  ];
  
  Plotly.newPlot('myDiv', data);
