// see data in console 
// console.log(data);

// // return only Apache data

////////////////////////////////
// Create a custom filtering function
function selector(bob) {
  return bob.county == 'Apache';
}

// filter() uses the custom function as its argument
let dataApache = data.filter(selector);

// Print to console
console.log(dataApache);

//////////////////////////////////////////////

// County names
county = dataApache.map(function (row){
  return row.county
});

// 
let trace2 = {
    x: dataApache.map(row => row.year),
    y: dataApache.map(row => row.value),
    type: "line"
  
  };

// Data trace array
let traceData2 = [trace2];

// Apply the group barmode to the layout
let layout2 = {
  title: "ED Rates for Apache County ",
  x: "year",
  y:"value of ed rates"
};

// Render the plot to the div tag with id "plot"
Plotly.newPlot("plot2", traceData2, layout2);