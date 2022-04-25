// function BookingInfo() {

// }


// var register = document.getElementById('paynow');
// register.addEventListener('click', BookingInfo);
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


// console.log(show);
// console.log(theater);
// document.getElementById("display").innerText += " for " + show + " " + theater + "\n" + "Movie: " + rec_movie_1;
