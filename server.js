var express = require("express");
var app = express();
var path = require('path');
var bodyParser = require("body-parser");
var spawn = require("child_process").spawn;

app.use(bodyParser.urlencoded({extended: false}))
app.use(bodyParser.json())

app.use('/public',express.static(path.join(__dirname,'public')));
app.use('/modules',express.static(path.join(__dirname,'node_modules')));

app.get('/index.html', function (req, res) {
	console.log("Index - GET");
	res.sendFile(path.join(__dirname,"views/index.html"));
});

app.get('/bot1.html', function (req, res) {
	console.log("Bot1 - GET")
	res.sendFile(path.join(__dirname,"views/bot1.html"));
});

app.post('/curpos',function (req, res){
	var boardFEN = req.body['game'];
	//console.log(boardFEN);
	var pythonProcess = spawn('C:/Users/Aravind Ravikumar/AppData/Local/Programs/Python/Python37/python.exe',["public/chess_engine/minmax.py",boardFEN]);		//Because path not detected in python script, use this if Windows

	pythonProcess.stdout.on('data', function(data){
		console.log(data.toString());
	 });

	 pythonProcess.stderr.on('data', function(data){
		console.log("Error in script");
		console.log(data.toString());
	 });

});

 var server = app.listen(8080, "127.0.0.1", function () {
	var host = server.address().address;
	var port = server.address().port;
 
	console.log("Chess bot running at http://%s:%s", host, port);
 });