// 1.	Get your dataset: 
var results_ed_visit_35 = "http://127.0.0.1:5000/edvisit";


// see data in console 
  console.log(results_ed_visit_35);

<<<<<<< HEAD

// Use an anon function to return only the values for a specific age range variable
var results_ed_visit_35 = results_ed_visit_35.map(function(d) { return d.rate;});



// Filter JSON to return only the years (could use either variable)
var years = results_ed_visit_35.map(function(d) { return d.year;});
console.log(years)


=======
  
// // Use an anon function to return only the values
  // .map reduces data and make another array
var results_ed_visit_35 = results_ed_visit_35.map(
  function(d) {
     return d.value;
    });

// // Filter JSON to return only the years (could use either variable)
var years = results_ed_visit_35.map(
  function(d) { 
    return d.year;
  });
>>>>>>> 1b15d651dfa82a903f0bdcc85d4b1c061c115925

// // Inserting data into Plotly chart 
var data = [
  {
   x: years,
    y: values,
    type: 'bar'
  }
];

Plotly.newPlot('myDiv', data);

