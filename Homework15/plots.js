/*
function populate_select(){
    var dataoption = []
    var dataset = document.getElementById('selDataset');

    var datanames = ["BB_940","BB_941","BB_943"];//$.getJSON($SCRIPT_ROOT + '/names', { name: name });
    for (i=0; i<datanames.length; i++){
        var opt = document.createElement("option");
        opt.setAttribute("value", datanames(i));
        document.getElementById("selDataset").appendChild(opt);
    }
}
populate_select();
*/

function init(){
    var data = [{
        values: [
            163, 126, 113, 78, 71, 51, 50, 47, 40, 40
        ],
        labels: [
            "1167", "2859", "482", "2264", "41", "1189", "352", "189", "2318", "1977"
        ],
        type: "pie"
    }];

    var layout = {
        height: 600,
        width: 800
    };
    //var $pie = document.getElementById("pie");
    Plotly.plot("pie", data, layout);
}

function updatePlotly(newdata, newotu) {
    // Update the pie chart with the newdata array
    var $pie = document.getElementById("pie");
    Plotly.restyle($pie, "values", [newdata]);
}

function optionChanged(optsample) {
    var data = [];
    var sampleURL = '/samples/<optsample>';
    Plotly.d3.json(sampleURL, function(error, response) {
        if (error) {
            return console.warn(error);
        }   
        var otuid = response.otu_ids;
        var samplevalue = response.sample_values;
        data = samplevalue;
        // Update plot with new data
        updatePlotly(data);
    });
}

init();
