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

function updatePlotly(newsample, newotu) {
    // Update the pie chart with the newdata array
    var $pie = document.getElementById("pie");
    Plotly.restyle($pie, { values : [newsample], labels : [newotu] } );
    //
    // Update the bubble chart with the new data sample 
    var $bubble = document.getElementById("divbuble");
    Plotly.restyle($bubble, [ {x: [newotu], y: [newsample], marker: {size: [newsample], color:[newotu]} }]);
}

function optionChanged(optsample) {
    var datasample = [];
    var dataotuid = [];
    var otuURL = '/otu';
    var metaURL = '/metadata/'+optsample;
    var sampleURL = '/samples/'+optsample;
    Plotly.d3.json(sampleURL, function(error, response) {
        if (error) {
            return console.warn(error);
        }   
        var samplevalue = response[0].sample_values.slice(0,10);
        var otuid = response[0].otu_ids.slice(0,10);
        // Update plot with new data
        updatePlotly(samplevalue,otuid);
    });
    Plotly.d3.json(metaURL, function(error, metaresponse) {
        if (error) {
            return console.warn(error);
        }  
        console.log(metaresponse);
        var metaAge = metaresponse[0].AGE;
        var metaBbtype = metaresponse[0].BBTYPE;
        var metaGender = metaresponse[0].GENDER;
        var metaEthnic = metaresponse[0].ETHNICITY;
        var metaLocat = metaresponse[0].LOCATION;
        var metaSampId = metaresponse[0].SAMPLEID;
        var dataDict = { "AGE:": metaAge,
                         "BBTYPE:": metaBbtype,
                         "GENDER:": metaGender,
                         "ETHNICITY": metaEthnic,
                         "LOCATION:": metaLocat,
                         "SAMPLEID:": metaSampId
                    };
        var data = [{
            type: 'table',
            header: { values: 'Sample Metadata'},
            cells: {
                values: dataDict
            }
        }];
        $boxText = document.getElementById("textmetadata");
        Plotly.plot($boxText, data, layout);
    });

    Plotly.d3.json(otuURL, function(error, response) {
        if (error) { 
            return console.warn(error);
        }  
        var otudesc = response[0].slice(0,10);
    });
}
function buildPlot(){
    var trace = {
        x: [1167, 2859, 482, 2264, 41, 1189, 352, 189, 2318, 1977],
        y: [163, 126, 113, 78, 71, 51, 50, 47, 40, 40],
        mode: "markers",
        marker: {
            size: [163, 126, 113, 78, 71, 51, 50, 47, 40, 40],
            color: [1167, 2859, 482, 2264, 41, 1189, 352, 189, 2318, 1977]
        }
    }
    var data = [trace];
    var layout = { 
        xaxis: { title: "OTU ID" },
        showlegend: false,
        zeroline: true,
        height: 600, 
        width: 980};
    Plotly.plot("divbuble", data, layout);
}
// call initialization to draw the first time
init();
buildPlot();



