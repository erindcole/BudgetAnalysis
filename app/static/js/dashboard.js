queue()
    .defer(d3.json, "/explore")
    .await(makeCharts);

function makeCharts(error, data) {
	

};
