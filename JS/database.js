const createPool = require('mysql');
// import createPool from 'mysql'
const pool = createPool.createConnection({
    host: "localhost",
    port: "3307",
    user: "root",
    password: "",
    database: "BookYourShow"
})

pool.connect((err, result) => {
    if (err) {
        console.warn(err);
    }
    else {
        console.warn(result);
    }
});

pool.query("SELECT ID, USERNAME, EMAIL, PASSWORD FROM Registered_Users",(err, result) => {
    if (err) {
        console.warn(err);
    }
    else {
        console.log(result);
    }
})



    // pool.query(`"INSERT INTO Registered_Users VALUES ('101', ${Username}, ${Email}, ${Password})"`, (err, result) => {
    //     if (err) {
    //         console.warn(err);
    //     }
    //     else {
    //         console.log(result);
    //     }
    // })



//     function writeUserData() {

//         let Username = document.getElementById('uname').value.trim();
//         let Password = document.getElementById('pass').value;
//         let Email = document.getElementById('email').value;
    
//         // localStorage.setItem("user_name", Username);
//         // localStorage.setItem("Email", Email);
//         // localStorage.setItem("Password", Password);
    
    
//         // for fetching data 
// }
//     // User Registration
//     var register = document.getElementById('RegisterBtn');
//     register.addEventListener('click', writeUserData);
