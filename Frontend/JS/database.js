//*********************************************************************************************************************//
//*************************************************** New Code ******************************************************//

console.log("Registration page loaded");


// var con = require('../../Backend/Database/connection'); // Importing connection

let signUpBtn = document.getElementById("Register_Btn");

signUpBtn.addEventListener('click', () => {

    let UserID = document.getElementById("ID").value;
    let Name = document.getElementById("uname").value;
    let Email = document.getElementById("email").value;
    let Password = document.getElementById("pass").value;

    let data = {
        userid: UserID,
        name: Name,
        email: Email,
        pass: Password
    }

    fetch("http://localhost:5008/registration/register/", {
        method: "POST",
        body: JSON.stringify(data),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then((result) => {
        console.log(result);
    })
        .catch((e) => {
            console.error(e);
        })
});

//*********************************************************************************************************************//





//**************************************************** Registration ****************************************************/
//*********************************************************************************************************************//

// var con = require('./connection') // Importing connection

// var express = require('express'); // Importing Express
// var app = express()
// var bodyParser = require('body-parser'); // Importing Bodyparser


// app.use(bodyParser.json())

// app.use(bodyParser.urlencoded({ extended: true }));

// app.get('/', function (req, res) {
//     res.sendFile(__dirname + '/registration.html');
// })


// app.post('/', function (req, res) {
//     var id = req.body.ID;
//     var name = req.body.name;
//     var email = req.body.email;
//     var pass = req.body.pass;


//     var sql = "INSERT INTO Registered_Users(ID, USERNAME, EMAIL, PASSWORD) VALUES ('"+id+"', '" +name + "', '" +email + "', '" +pass+ "')";
//     con.query(sql, function (error, result) {
//         if (error) {
//             console.warn(error);
//         }
//         else {
//             res.send('Student Register Successfully' + result.insertId);
//         }
//     })

// })
// app.listen(3000);








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