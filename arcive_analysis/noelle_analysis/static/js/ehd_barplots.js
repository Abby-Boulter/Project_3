const ED35 = 'data/EDRates35.csv'
// Fetch the JSON data and console log it

d3.csv(ED35).then(function(data) {
  onsole.log(data);
  });

function buildBarChart(sample) {

    // Use D3 to retrieve all of the data
    d3.json(ED35).then((data) => { 
        
        // Set up the trace for the bar chart
        let trace = {
            x: xticks,
            y: yticks,
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