
   
// function BookingInfo() {

// }


// var register = document.getElementById('paynow');
// register.addEventListener('click', BookingInfo);

// console.log(show);
// console.log(theater);
// document.getElementById("display").innerText += " for " + show + " " + theater + "\n" + "Movie: " + rec_movie_1;


 // Import the functions you need from the SDKs you need
 import { initializeApp } from "https://www.gstatic.com/firebasejs/9.6.11/firebase-app.js";
 import { getAnalytics } from "https://www.gstatic.com/firebasejs/9.6.11/firebase-analytics.js";
 // TODO: Add SDKs for Firebase products that you want to use
 // https://firebase.google.com/docs/web/setup#available-libraries

 // Your web app's Firebase configuration
 // For Firebase JS SDK v7.20.0 and later, measurementId is optional
 const firebaseConfig = {
     apiKey: "AIzaSyAPaUXSG4jDBh37oBebeSLOS_H6x1U02RU",
     authDomain: "book-your-show-b79e2.firebaseapp.com",
     databaseURL: "https://book-your-show-b79e2-default-rtdb.firebaseio.com",
     projectId: "book-your-show-b79e2",
     storageBucket: "book-your-show-b79e2.appspot.com",
     messagingSenderId: "278309549811",
     appId: "1:278309549811:web:f6ce73d73b77d3d2712986",
     measurementId: "G-B1M7Z352H2"
 };

 // Initialize Firebase
 const app = initializeApp(firebaseConfig);
 const analytics = getAnalytics(app);




 import { getDatabase, set, ref, child, get, onValue }
     from "https://www.gstatic.com/firebasejs/9.6.11/firebase-database.js";

 const db = getDatabase();
 let show = localStorage.getItem("ShowTime");
let theater = localStorage.getItem("TheaterName");
let rec_movie_1 = localStorage.getItem("MovieName");
let totalprice = localStorage.getItem("totalPrice");
let seatselected = localStorage.getItem("seatSelected");
let username = localStorage.getItem("user_name");

let seatInfo = [];
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
    let total = count * parseInt(price);
    // console.log(total);

    let seatvalue = document.getElementById(id).innerText;
    // console.log(seatvalue);
    // console.log(display);

    seatInfo.push(seatvalue);

    console.log(seatInfo);
    

    let totalPrice = localStorage.setItem("totalPrice", total);
    // let seatSelected = localStorage.setItem("seatSelected", seatselected);
    let seatinfo = localStorage.setItem("SeatArray", seatInfo);
  
    // console.log(totalPrice);
    // console.log(seatSelected);
}


//  const payBtn = document.getElementById('payBtn');

//  function selectedSeats() {
//    let seatVal = localStorage.getItem('SeatArray')
//    let username = localStorage.getItem("username");
//    console.log(seatVal);
//    console.log(username);


//      set(ref(db, 'SelectedSeats/'+ username ), {
      
//         seat: seatVal
        
//      })
//          .then(() => {
           
//              alert("The user added successfully");
//          })
//          .catch(() => {
//              alert("something went wrong" + error);
//          })
         
//  }


//         payBtn.addEventListener('click',selectedSeats );
