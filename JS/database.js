//**************************************************** Registration ****************************************************/
//*********************************************************************************************************************//

var con = require('./connection') // Importing connection

var express = require('express'); // Importing Express
var app = express()
var bodyParser = require('body-parser'); // Importing Bodyparser


app.use(bodyParser.json())

app.use(bodyParser.urlencoded({ extended: true }));

app.get('/', function (req, res) {
    res.sendFile(__dirname + '/registration.html');
})

app.post('/', function (req, res) {
    // var name = req.body.name;
    // var email = req.body.email;
    // var pass = req.body.pass;
    var jsondata = req.body;
    // console.log(jsondata);

    var values = [];
    // console.log(req.body);
    for (var i = 0; i < jsondata.length; i++)
        values.push([jsondata[i].ID, jsondata[i].name, jsondata[i].email, jsondata[i].pass]);

    var sql = "INSERT INTO Registered_Users(ID, USERNAME, EMAIL, PASSWORD) VALUES ('"+jsondata.ID+"', '" + jsondata.name + "', '" + jsondata.email + "', '" + jsondata.pass + "')";
    con.query(sql, function (error, result) {
        if (error) {
            console.warn(error);
        }
        else {
            res.send('Student Register Successfully' + result.insertId);
            // res.redirect('/index.html');
        }
    })

})
app.listen(3000);





// Old Code


    // con.connect(function (error) {
    //     if (error) {
    //         console.warn(error);
    //     }
    //     else {
    //         console.warn("successfull");
    //     }


        //without Json Format
        // var sql = "INSERT INTO Registered_Users(ID, USERNAME, EMAIL, PASSWORD) VALUES ('110', '"+name+"', '"+email+"', '"+pass+"')";
        // con.query(sql, function(error, result){
        //     if (error) {
        //         console.warn(error);
        //     }
        //     else {
        //         res.send('Student Register Successfully' +result.insertId);
        //     }
        // })