// see data in console 
// console.log(data);

// // return only Gila data

////////////////////////////////
// Create a custom filtering function
function selector(bob) {
  return bob.county == 'Gila';
}

// filter() uses the custom function as its argument
let dataGila = data.filter(selector);

// Print to console
console.log(dataGila);

//////////////////////////////////////////////

// County names
county = dataGila.map(function (row){
  return row.county
});

// 
let trace2 = {
    x: dataGila.map(row => row.year),
    y: dataGila.map(row => row.value),
    type: "line"
  
  };

// Data trace array
let traceData2 = [trace2];

// Apply the group barmode to the layout
let layout2 = {
  title: "ED Rates for Gila County ",
  x: "year",
  y:"value of ed rates"
};

// Render the plot to the div tag with id "plot"
Plotly.newPlot("plot2", traceData2, layout2);