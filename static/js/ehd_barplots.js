
// another file for the extreme heat days
var results_ext_heat_days = "http://127.0.0.1:5000/ehd"

// see data in console 
console.log(results_ext_heat_days)

// Use an anon function to return only the values
var results_ext_heat_days = results_ext_heat_days.map(function(d) { return d.rate;});

// Filter JSON to return only the years (could use either variable)
var county = results_ext_heat_days.map(function(d) { return d.county;});

// Inserting data into Plotly chart 
var data = [
  {
    x: county,
    y: values,
    type: 'bar'
  }
];

Plotly.newPlot('myDiv', data);