// see data in console 
// console.log(data);

// // return only Gila data

////////////////////////////////
// Create a custom filtering function
function selectorOther(bob) {
    return bob.value > 40 & bob.county == 'Gila';
  }
  
  // filter() uses the custom function as its argument
  let jeezus = data.filter(selectorOther);
  
  // Print to console
  console.log(jeezus);
  
  //////////////////////////////////////////////
  
  // County names
  county = jeezus.map(function (row){
    return row.county
  });
  
  // 
  let trace3 = {
      x: jeezus.map(row => row.year),
      y: jeezus.map(row => row.value),
      type: "bar"
    
    };
  
  // Data trace array
  let traceData3 = [trace3];
  
  // Apply the group barmode to the layout
  let layout3 = {
    title: "Highest ED Rates ",
    x: "year",
    y:"value of ed rates"
  };
  
  // Render the plot to the div tag with id "plot"
  Plotly.newPlot("plot3", traceData3, layout3);