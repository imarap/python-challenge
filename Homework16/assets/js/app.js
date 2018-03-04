// D3 Scatterplot Assignment
// Students:
// =========
// Follow your written instructions and create a scatter plot with D3.js.

// Whenever the window resizes, call the handleResize function
d3.select(window).on("resize", handleResize);
// When the browser loads, loadChart() is called
loadChart();
function handleResize() {
    var svgArea = d3.select("svg");
    // If there is already an svg container on the page, remove it and reload the chart
    if (!svgArea.empty()) {
        svgArea.remove();
        loadChart();
    }
}

function loadChart() {
    // Define SVG area dimensions
    var svgWidth = window.innerWidth;
    var svgHeight = window.innerHeight;
    // Define the chart's margins as an object
    var chartMargin = {
        top: 30,
        right: 30,
        bottom: 30,
        left: 30
    };
    // Define dimensions of the chart area
    var chartWidth = svgWidth - chartMargin.left - chartMargin.right;
    var chartHeight = svgHeight - chartMargin.top - chartMargin.bottom;
    // Select body, append SVG area to it, and set the dimensions
    // Inside the SVG area, append an SVG group, move it down and to the right
    var svg = d3
        .select(".chart")
        .append("svg")
        .attr("height", svgHeight)
        .attr("width", svgWidth)
        .append("g")
        .attr("transform", "translate(" + chartMargin.left + ", " + chartMargin.top + ")");
    // Configure a band scale, with a range between 0 and the chartWidth and a padding of 0.1 (10%)
    var xBandScale = d3.scaleBand().range([0, chartWidth]).padding(0.1);
    // Create a linear scale, with a range between the chartHeight and 0.
    var yLinearScale = d3.scaleLinear().range([chartHeight, 0]);


/*
var svgWidth = 960;
var svgHeight = 500;
var margin = { top: 20, right: 40, bottom: 60, left: 100 };
var width = svgWidth - margin.left - margin.right;
var height = svgHeight - margin.top - margin.bottom;
// Create an SVG wrapper, append an SVG group that will hold our chart, and shift the latter by left and top margins.
var svg = d3.select(".chart")
    .append("svg")
    .attr("width", svgWidth)
    .attr("height", svgHeight)
    .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")")
*/
    var chart = svg.append("g");

    d3.csv("../../data/Data.csv", function(err, povData) {
        if (err) {
            throw err;
        }
        console.log(povData);
        povData.forEach(function(data) {
            data.poverty = +data.poverty;
            data.healthcare = +data.healthcare;
        });

        // Create scale functions
        var yLinearScale = d3.scaleLinear()
            .range([chartHeight, 0]);
        var xLinearScale = d3.scaleLinear()
            .range([10, chartWidth]);
        // Create axis functions
        var bottomAxis = d3.axisBottom(xLinearScale);
        var leftAxis = d3.axisLeft(yLinearScale);
        // Scale the domain
        xLinearScale.domain([8, d3.max(povData, function(data) {
            return +data.poverty;
        })]);
        yLinearScale.domain([0, d3.max(povData, function(data) {
            return +data.healthcare;
        })]);

        var toolTip = d3.tip()
        .attr("class", "tooltip")
        .offset([50, 50])
        .html(function(data) {
            var stateName = data.state;
            var statePoverty = +data.poverty;
            var stateHealth = +data.healthcare;
            return (stateName + "<hr/> Poverty: " + statePoverty + "%<br> Healthcare: " + stateHealth +"%");
        });
        chart.call(toolTip);

        chart.selectAll("circle")
        .data(povData)
        .enter()
        .append("circle")
        .attr("cx", function(data, index) {
            return xLinearScale(data.poverty);
        })
        .attr("cy", function(data, index) {
            return yLinearScale(data.healthcare);
        })
        .attr("r", "10")
        .attr("fill", "skyblue")
        .on("mouseover", toolTip.show)
        .on("mouseout", toolTip.hide);

        chart.selectAll("text")
        .data(povData)
        .enter()
        .append("text")
        .text(function(data) { return data.abbr; })
        .attr("x", function(data) { return xLinearScale(data.poverty) })
        .attr("y", function(data) { return yLinearScale(data.healthcare) })
        .attr("font-family", "sans-serif")
        .attr("font-size", "8px")
        .attr("fill", "white");

        chart.append("g")
        .attr("transform", `translate(0, ${chartHeight})`)
        .call(bottomAxis);
        chart.append("g")
        .call(leftAxis);

        chart.append("text")
        .attr("transform", "rotate(-90)")
        .attr("y", 0 - chartMargin.left-6) // + 40)
        .attr("x", 0 - (chartHeight / 2))
        .attr("dy", "1em")
        .attr("class", "axisText")
        .text("Lacks Healthcare (%)");

        // Append x-axis labels
        chart.append("text")
        .attr("transform", "translate(" + (chartWidth - 400 ) + " ," + (chartHeight + chartMargin.top - 5 ) + ")")
        //.attr("transform", "translate(" + (chartWidth / 2) + " ," + (chartHeight + chartMargin.top + 30) + ")")
        .attr("class", "axisText")
        .text("Poverty (%)");

    });
}