

    Highcharts.getJSON('https://demo-live-data.highcharts.com/aapl-c.json', function (data) {
    // Create the chart
    Highcharts.stockChart('container', {


        rangeSelector: {
        selected: 1
        },

        title: {
        text: 'AAPL Stock Price'
        },

        series: [{
        name: 'AAPL',
        data: data,
        tooltip: {
            valueDecimals: 2
        }
        }]
    });
});


// function init() {
//     // Populate dropdown
//     d3.json("samples.json").then((data) => {
  
//       // Selector
//       var selector = d3.select("#selDataset");
  
//       // Html is appended
//       data.names.forEach((result) => {
//       selector
//           .append("option")
//           .text(result)
//           .property("value", result)
//       });
  
//       makePage(data.names[0])
//     });
//   }
  
//   // Listen for a change in the dropdown
//   function optionChanged(selection){
//     makePage(selection);
//   };
  
//   init()