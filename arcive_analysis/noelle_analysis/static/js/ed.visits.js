// 1.	Get your dataset: 
var results_ed_visit_35 = "http://127.0.0.1:5000/edvisit";


// see data in console 
  console.log(results_ed_visit_35);

// Use an anon function to return only the birth rates for a specific age range variable
var results_ed_visit_35 = results_ed_visit_35.map(function(d) { return d.rate;});

// Filter JSON to return only the years (could use either variable)
var years = results_ed_visit_35.map(function(d) { return d.year;});

// Inserting data into Plotly chart 
var data = [
  {
    x: years,
    y: values,
    type: 'bar'
  }
];

Plotly.newPlot('myDiv', data);

// another file for the extreme heat days
var results_ext_heat_days = "http://127.0.0.1:5000/ehd"
// see data in console 
console.log(results_ext_heat_days);

// Use an anon function to return only the birth rates for a specific age range variable
var results_ext_heat_days = results_ext_heat_days.map(function(d) { return d.rate;});

// Filter JSON to return only the years (could use either variable)
var years = results_ext_heat_days.map(function(d) { return d.year;});

// Inserting data into Plotly chart 
var data = [
  {
    x: years,
    y: values,
    type: 'bar'
  }
];

Plotly.newPlot('myDiv', data);