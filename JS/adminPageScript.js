
document.getElementById('addMovie').onclick= ()=>showModal('Add Movie','',
'Cancel','Save Changes',()=>
{
    console.log('Changes saved');
});

document.getElementById('removeMovie').onclick= ()=>showModal('Remove Movie',
'Hello','Cancel','Save Changes',()=>
{
    console.log('Changes saved');
});
document.getElementById('addTheater').onclick= ()=>addTheaterShowModal('Add Theater',
'Hello','Cancel','Save Changes',()=>
{
    console.log('Changes saved');
});


// document.getElementById("imageInputModal").addEventListener("change",preview);
function preview(){
  
  const imageInputModal = document.getElementById("imageInputModal");
  const imagePreview= document.getElementById("imagePreview");
  const reader = new FileReader();

  reader.onload = function(){
    console.log(reader.result);
    imagePreview.src = `${reader.result}`;
  }

  reader.readAsDataURL(imageInputModal.files[0]);
// 
}
function saveChanges(){

    const imagePreview = document.getElementById("imagePreview").value;
    const movieName = document.getElementById("movieName").value;
    const animation = document.getElementById("animation");
    const movieLanguage = document.getElementById("movieLanguage");
    const movieDuration = document.getElementById("movieDuration");
    const movieCertification = document.getElementById("movieCertification");
    const releasedate = document.getElementById("releasedate");
    const aboutMovie = document.getElementById("aboutMovie");
    const movieCast = document.getElementById("movieCast");
    const movieCrew = document.getElementById("movieCrew");
    const saveData = document.getElementById("saveData");
    console.log(imagePreview);
    console.log(movieName);


}

function saveAddTheater(){
  const theaterName = document.getElementById("theaterName").value;
  const theaterId = document.getElementById("theaterId").value;
  const location = document.getElementById("location").value;
  const cityName = document.getElementById("cityName").value;
  const showTime = document.getElementById("showTime").value;
  const saveTheaterData = document.getElementById("saveTheaterData").value;
  
  console.log(theaterName);
  console.log(theaterId);
  console.log(location);
  console.log(cityName);
  console.log(showTime);
  

}

