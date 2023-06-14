let url = "https://ephtracking.cdc.gov/apigateway/api/v1/getCoreHolder/423/82/1/4/1/2021,2020,2019,2018,2017,2016,2015,2014,2013,2012,2011/0/0?TemperatureHeatIndexId=1&RelativeThresholdId=1";
  
  // Getting our GeoJSON data
d3.json(url).then(function(data) {
  // Once we get a response, send the data.features object to the createFeatures function.
  console.log(data.tableResult);
  });

// Create a droupdown menu and sample selection
// Function called by DOM changes

// Create bar chart
let county_names = ['Apache', 'Cochise', 'Coconino', 'Gila', 'Graham', 'Greenlee', 'La Paz',
'Maricopa', 'Mohave', 'Navajo', 'Pima', 'Pinal', 'Santa Cruz', 'Yavapai', 'Yuma'];

// function countyCount(county_names){
//   let count = 0;

//   data.forEach((data) => {
//       if (data.tableResult.geo == county_names){
//           count += 1;
//       };
//   });
//   return count;
// };