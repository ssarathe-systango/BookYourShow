/*-----------------------------------------------------------------------------------------------------------------------
* Firebase Information:-
Theater --->
            ShowTime
            Theater Name
            Seat Booked
            Total Price
-------------------------------------------------------------------------------------------------------------------------*/


import { initializeApp } from "https://www.gstatic.com/firebasejs/9.6.7/firebase-app.js";
// import { getDatabase, set, ref, child, get, onValue, update } from "https://www.gstatic.com/firebasejs/9.6.7/firebase-detabase.js";

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
const db = getDatabase();

function BookingInfo() {

    let show = localStorage.getItem("ShowTime");
    let theater = localStorage.getItem("TheaterName");
    let totalprice = localStorage.getItem("totalPrice");
    let seatselected = localStorage.getItem("seatSelected");
    let username = localStorage.getItem("user_name");
    // console.log(show);
    // console.log(theater);
    // console.log(totalprice);
    // console.log(seatselected);
    console.log(username);
    let UniqueId = show;
    set(ref(db, "Booking Info/" + UniqueId + " " + username), {
        Time: show,
        Theater: theater,
        Price: totalprice,
        Seat: seatselected
    })
        .then(() => { alert('Done'); })
        .catch(() => { alert('errro'); });
}
var register = document.getElementById('paynow');
register.addEventListener('click', BookingInfo);
//-------------------------------------------------------------------------------------------------------------------------//

let count = 0;
//changing seat color
window.ChangeColor = function (id) {
    let element = document.getElementById(id);

    if (element.style.backgroundColor === 'mediumvioletred') {
        element.style.backgroundColor = '#5c5c5c';

    }
    else {
        element.style.backgroundColor = 'mediumvioletred';

    }

    if (element.style.backgroundColor === 'mediumvioletred') {
        count++;
    }
    else {
        count--;
    }

    let price = document.getElementById("seat1").dataset.price;
    total = count * parseInt(price);
    // console.log(total);

    let seatvalue = document.getElementById(id).innerText;
    // console.log(seatvalue);
    // console.log(display);


    let totalPrice = localStorage.setItem("totalPrice", total);
    let seatSelected = localStorage.setItem("seatSelected", seatvalue);

    // console.log(totalPrice);
    // console.log(seatSelected);
}
let show = localStorage.getItem("ShowTime");
let theater = localStorage.getItem("TheaterName");
let rec_movie_1 = localStorage.getItem("MovieName");

// console.log(show);
// console.log(theater);
// console.log(moviename);

document.getElementById("display").innerText += " for " + show + " " + theater + "\n" + "Movie: " + rec_movie_1;


