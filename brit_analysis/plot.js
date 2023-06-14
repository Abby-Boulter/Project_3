console.log(data);

// County names
year = data.map(function (row){
  return row.year
});

// 
let trace1 = {
    x: data.map(row => row.year),
    y: data.map(row => row.value),
    type: "bar"
  };

// Data trace array
let traceData = [trace1];

// Apply the group barmode to the layout
let layout = {
  title: "Ed Rates  ",
  x: "county",
  y:"value of ed rates"
};

// Render the plot to the div tag with id "plot"
Plotly.newPlot("plot", traceData, layout);
