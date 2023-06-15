console.log(alled);

// County names
year = alled.map(function (row){
  return row.year
});

// 
let graph = {
    x: alled.map(row => row.county),
    y: alled.map(row => row.value),
    type: "bar"
  };

// Data trace array
let td = [graph];

// Apply the group barmode to the layout
let layout5 = {
  title: "Ed Rates for the last 10 years  ",
  x: "county",
  y:"value of ed rates"
};

// Render the plot to the div tag with id "plot"
Plotly.newPlot("graph", td, layout5);

// function init() {
//   // Use D3 to select the dropdown menu
//       let dropdownMenu = d3.select("#selDataset");
//       // Use D3 to get sample names and populate the drop-down selector
//       d3.json(data).then((data) => {
          
//           // Set a variable for the sample names
//           let year = data.year;
  
//           // Add  samples to dropdown menu
//           county.forEach((id) => {
  
//               // Log the value of id for each iteration of the loop
//               console.log(id);
//               dropdownMenu.append("option")
//               .text(id)
//               .property("value",id);
//           });