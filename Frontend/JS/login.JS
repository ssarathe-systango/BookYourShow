function Authentication() {
    let Username = document.getElementById('uname').value.trim();
    let Password = document.getElementById('pass').value;

    db.ref('Registered Users').once('value')
        .then(function (snapshot) {

            var flag = false;

            snapshot.forEach((item) => {

                uname = item.val().uname;
                pass = item.val().pass;

                if (uname === Username && pass === Password) {
                    flag = true;
                    localStorage.setItem("user_name", uname);

                    window.location = "index.html";
                }

            });

            if (flag === false) {
                alert("Invalid Username Or Password!");
            }
        })
        .catch((error) => {
            console.log(error);
            return false;
        });

}
function login(user) {
    window.location = "index.html";
}