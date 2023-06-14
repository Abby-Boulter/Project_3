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

// got to process data
function processData(allRows){
  let x= []; //want the x to be the key
  let y1=[]; // y axis is the EHD
  let y2=[]; // 2nd y axis is the ED visits
  let row;
  
  let i = 0;
  while (i < allRowsRows.length) {
    row = allRows[i];
    x.push(row["key"]);
    y1.push(row["ext_heat_days"]);
    y2.push(row["ed_rate_35"]);
    i += 1;
  }
  console.log("X", x);
  console.log("Y1", y1);

  makePlotly(x,y1,y2)
}