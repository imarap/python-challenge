// Get references to the tbody element, input field and button
var $tbody = document.querySelector("tbody");
var $ufoInput = document.querySelector("#ufo_search");
var $searchBtn = document.querySelector("#search");
var $ufoInput2 = document.querySelector("#city_search");
var $ufoInput3 = document.querySelector("#state_search");
var $ufoInput4 = document.querySelector("#country_search");
var $ufoInput5 = document.querySelector("#shape_search");
var $loadMoreBtn = document.querySelector("#load-btn");

// Set a startingIndex and resultsPerPage variable
var startingIndex = 0;
var resultsPerPage = 10;

// Add an event listener to the searchButton, call handleSearchButtonClick when clicked
$searchBtn.addEventListener("click", handleSearchButtonClick1);
$loadMoreBtn.addEventListener("click", handleButtonClick);

// Set filteredUFOSighting to dataSet initially
var filteredUFOSighting = dataSet;

function renderTableSection() {
  // Set the value of endingIndex to startingIndex + resultsPerPage
  var endingIndex = startingIndex + resultsPerPage;
  // Get a section of the dataSet array to render
  var ufoLineSubset = filteredUFOSighting.slice(startingIndex, endingIndex);
  for (var i = 0; i < ufoLineSubset.length; i++) {
    // Get the current dataSet object and its fields
    var ufoLine = ufoLineSubset[i];
    var fields = Object.keys(ufoLine);
    // Create a new row in the tbody, set the index to be i + startingIndex
    var $row = $tbody.insertRow(i + startingIndex);
    for (var j = 0; j < fields.length; j++) {
      // For every field in the setData object, create a new cell and set its inner text to be the current value at the current ufoLine's field
      var field = fields[j];
      var $cell = $row.insertCell(j);
      $cell.innerText = ufoLine[field];
    }
  }
}
function renderTableManySection() {
  var endingIndex = startingIndex + resultsPerPage;
  // Get a section of the dataSet array to render
  var ufoLineSubset = filteredUFOSighting.slice(startingIndex, endingIndex);
  for (var i = 0; i <= ufoLineSubset.length; i++) {
    var myTable = document.getElementById("ufotable").rows[i+1].cells;
    var ufoLine = ufoLineSubset[i];
    var fields = Object.keys(ufoLine);
    for (var j = 0; j < fields.length; j++) {
      var field = fields[j];
      myTable[j].innerHTML = ufoLine[field];
    }
  }
}
//
// Add an event listener to the button, call handleButtonClick when clicked
//$loadMoreBtn.addEventListener("click", handleButtonClick);
//
function handleButtonClick() {
  // Increase startingIndex by resultsPerPage, render the next section of the table
  startingIndex += resultsPerPage;
  renderTableManySection();
  // Check to see if there are any more results to render
  if (startingIndex + resultsPerPage >= filteredUFOSighting.length) {
    $loadMoreBtn.classList.add("disabled");
    $loadMoreBtn.innerText = "All UFOs sighting Loaded";
    $loadMoreBtn.removeEventListener("click", handleButtonClick);
  }
}
//
function handleSearchButtonClick1() {
  // Format the user's search by removing leading and trailing whitespace, lowercase the string
  var filteredUfo = $ufoInput.value.trim().toLowerCase();
  var filteredUfo2 = $ufoInput2.value.trim().toLowerCase();
  var filteredUfo3 = $ufoInput3.value.trim().toLowerCase();
  var filteredUfo4 = $ufoInput4.value.trim().toLowerCase();
  var filteredUfo5 = $ufoInput5.value.trim().toLowerCase();
  // Set filteredUFOSighting to an array of all dataSet whose "datetime" matches the filter
  filteredUFOSighting = dataSet.filter(function(ufoLine) {
    var ufoDateTimeSearch = ufoLine.datetime.substring(0,filteredUfo.length).toLowerCase();
    var ufoCitySearch = ufoLine.city.substring(0,filteredUfo2.length).toLowerCase();
    var ufoStateSearch = ufoLine.state.substring(0,filteredUfo3.length).toLowerCase();
    var ufoCountrySearch = ufoLine.country.substring(0,filteredUfo4.length).toLowerCase();
    var ufoShapeSearch = ufoLine.shape.substring(0,filteredUfo5.length).toLowerCase();
    // If true, add the ufoRow to the filteredUfo, otherwise don't add it to filteredUfo
    var ufoReturnSearch = "";
    if (ufoDateTimeSearch == filteredUfo) {
      ufoReturnSearch = ufoDateTimeSearch;
    } 
    if (ufoCitySearch == filteredUfo2) {
      ufoReturnSearch += ufoCitySearch;
    } 
    if (ufoStateSearch == filteredUfo3) {
      ufoReturnSearch += ufoStateSearch;
    }
    if (ufoCountrySearch == filteredUfo4) {
      ufoReturnSearch += ufoCountrySearch;
    } 
    if (ufoShapeSearch == filteredUfo5) {
      ufoReturnSearch += ufoShapeSearch;
    }
    return ufoReturnSearch;
  });
  startingIndex = 1;
  renderTableManySection();
}

// Render the table for the first time on page load
renderTableSection();