// 1.	Get your dataset: 
fetch("./data/HRI.json")
.then(response => {
   return response.json();
})
.then(data => console.log(data));


// Functions for plot
function plotFromfile() {
  Plotly.d2.json(HRI, function (err, rows) {
    console.log(rows);
    processData(rows);
  });
}