// 1.	Get your dataset: 
// 1.	Use the D3 library to read in samples.json from the URL https://2u-data-curriculum-team.s3.amazonaws.com/dataviz-classroom/v1.1/14-Interactive-Web-Visualizations/02-Homework/samples.json.
let url = "https://ephtracking.cdc.gov/apigateway/api/v1/getCoreHolder/423/82/1/4/1/2021,2020,2019,2018,2017,2016,2015,2014,2013,2012,2011/0/0?TemperatureHeatIndexId=1&RelativeThresholdId=1";

  // Getting our GeoJSON data
  d3.json(url).then(function(data) {
    // Once we get a response, send the data.features object to the createFeatures function.
    createFeatures(data.features);
    });

