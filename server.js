var express = require("express");
var app = express();
var path = require('path');

app.use('/public',express.static(path.join(__dirname,'public')));
app.use('/modules',express.static(path.join(__dirname,'node_modules')));

app.get('/index.html', function (req, res) {
	console.log("Index - GET");
	res.sendFile(path.join(__dirname,"views/index.html"));
});

app.get('/bot1.html', function (req, res) {
	res.sendFile(path.join(__dirname,"views/bot1.html"));
});

 var server = app.listen(3000, "10.250.7.145", function () {
	var host = server.address().address;
	var port = server.address().port;
 
	console.log("Chess bot running at http://%s:%s", host, port);
 });