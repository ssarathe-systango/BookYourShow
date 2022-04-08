import { initializeApp } from "https://www.gstatic.com/firebasejs/9.6.7/firebase-app.js";

import { getDatabase, set, ref, child, get, onValue, update }
    from "https://www.gstatic.com/firebasejs/9.6.7/firebase-database.js";

const firebaseConfig = {
    apiKey: "AIzaSyCixKBXmM2r8M4k2peUH7roMm40Ohx5A8Y",
    authDomain: "bookyourshow-9c1f5.firebaseapp.com",
    databaseURL: "https://bookyourshow-9c1f5-default-rtdb.firebaseio.com",
    projectId: "bookyourshow-9c1f5",
    storageBucket: "bookyourshow-9c1f5.appspot.com",
    messagingSenderId: "430499662430",
    appId: "1:430499662430:web:d1b813748385cf013a42cf",
    measurementId: "G-V0WMX170VY"
};

// ----------------------------------------------------- Initialize Firebase ---------------------------------------------//
const app = initializeApp(firebaseConfig);
const arr = ["@", "#", "$", "%", "&", "/", "*", "-", "~", "[", "]", "{", "}", "?", ";", ":"];
const db = getDatabase();

function writeUserData() {

    let isValid = true;
    let Username = document.getElementById('uname').value.trim();
    let Password = document.getElementById('pass').value;
    let Email = document.getElementById('email').value;

    localStorage.setItem("user_name", Username);
    localStorage.setItem("Email", Email);

    // validation for special characters 
    arr.forEach(check => {
        if (Username.includes(check)) {
            isValid = false;
            alert('Invalid Characters!');
            location.reload();
        }
    });
    if (Username != "" && Password != "" && Email != "") {
        let UniqueId = Username;
        set(ref(db, "Registered Users/" + UniqueId), {
            email: Email,
            uname: Username,
            pass: Password,
        }).then(() => { alert('User Registered'); })
    }
    else {
        alert("Please Enter Something !");
    }
}

// User Registration


var register = document.getElementById('RegisterBtn');
register.addEventListener('click', writeUserData);