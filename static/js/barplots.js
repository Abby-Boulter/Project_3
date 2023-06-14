// 1.	Get your dataset: 
var HRI = require('data/HRI.json')

// Fetch the JSON data and console log it
d3.json(HRI).then(function(data) {
    console.log(data);
  });