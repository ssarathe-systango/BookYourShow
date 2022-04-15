const conn = require("../../Database/connection");
const createPool = require("../../Database/connection");

function putInformation(userid , name , email , pass) {

    let insertQuery = `INSERT INTO Registered_Users(ID, USERNAME, EMAIL, PASSWORD) VALUES ("${userid}", "${name}","${email}" , "${pass}")`;


    conn.query(insertQuery, (err, result) => {
        if (err) {
            console.log(err);
        }
        else {
            console.log("1 row inserted");
        }
    });
}


module.exports = {putInformation } ;