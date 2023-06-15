 console.log(tdata);

// County names
// county = data.map(function (row){
//   return row.county
// });

// 
let trace1 = {
    x: data.map(row => row.county),
    y: data.map(row => row.value),
    type: "bar"
  };

  let trace2 = {
    x: data.map(row => row.county),
    y: data.map(row => row.value),
    type: "bar"
  };
  let trace3 = {
    x: data.map(row => row.county),
    y: data.map(row => row.value),
    type: "bar"
  };
  let trace4 = {
    x: data.map(row => row.county),
    y: data.map(row => row.value),
    type: "bar"
  };
  let trace5 = {
    x: data.map(row => row.county),
    y: data.map(row => row.value),
    type: "bar"
  };
  let trace6 = {
    x: data.map(row => row.county),
    y: data.map(row => row.value),
    type: "bar"
  };
  let trace7 = {
    x: data.map(row => row.county),
    y: data.map(row => row.value),
    type: "bar"
  };
  let trace8 = {
    x: data.map(row => row.county),
    y: data.map(row => row.value),
    type: "bar"
  };
  let trace9 = {
    x: data.map(row => row.county),
    y: data.map(row => row.value),
    type: "bar"
  };
  let trace10 = {
    x: data.map(row => row.county),
    y: data.map(row => row.value),
    type: "bar"
  };
  let trace11 = {
    x: data.map(row => row.county),
    y: data.map(row => row.value),
    type: "bar"
  };
 

// Data trace array
let traceData = [trace1,trace2,trace3,trace4,trace5,trace6,trace7,trace8,trace9,trace10,trace11];

// Apply the group barmode to the layout
let layout = {
  title: "Ed Rates  ",
  x: "county",
  y:"value of ed rates"
};

// Render the plot to the div tag with id "plot"
Plotly.newPlot("plott", traceData, layout);
