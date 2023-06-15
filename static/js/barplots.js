// see data in console 
console.log(data);

// // return only 2021 data

////////////////////////////////
// Create a custom filtering function
function selectRecent(bob) {
  return bob.year == 2021;
}

// filter() uses the custom function as its argument
let data2021 = data.filter(selectRecent);

// Print to console
console.log(data2021);

//////////////////////////////////////////////

// County names
county = data2021.map(function (row){
  return row.county
});

// 
let trace1 = {
    x: data2021.map(row => row.county),
    y: data2021.map(row => row.value),
    type: "bar"
  
  };

// Data trace array
let traceData = [trace1];

// Apply the group barmode to the layout
let layout = {
  title: "ED Rates for 2021 ",
  x: "county",
  y:"value of ed rates"
};

// Render the plot to the div tag with id "plot"
Plotly.newPlot("plot1", traceData, layout);