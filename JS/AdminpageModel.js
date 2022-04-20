var modalWrap = null;
const showModal = (title, description,
  cancelbtn = 'Close',
  saveChangesbtn = 'Save Changes',
  callback
) => {
  if (modalWrap !== null) {
    modalWrap.remove();

  }

  modalWrap = document.createElement('div');
  modalWrap.innerHTML = `
  
    <div class="modal fade" id="movieModal" tabindex="-1" aria-labelledby="movieModalLabel" aria-hidden="true">
    <div class="modal-dialog modal-lg">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="movoieModalLabel">${title}</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          
          </div>
        <form action = "" method=="POST">
        <div class="modal-body" id="imageModal">
        <input type="file" id="imageInputModal" name="image" onchange="preview()">
        <div class="container">
          <!-- Uploaded Image -->
          <img id="imagePreview" src="" alt="Picture">
        </div>
        
        <div>
        <input class="form_field mb-3" type="text" name="movie" id="movieName" placeholder="Name of the Movie" autofocus="true"/>
        <input class="form_field mb-3" type="text" name="animation" id="animation" placeholder="Animation" autofocus="true"/>
        <input class="form_field mb-3" type="text" name="language" id="movieLanguage" placeholder="Language" autofocus="true"/>
        <input class="form_field mb-3" type="text" name="duration" id="movieDuration" placeholder="Movie Duration" autofocus="true"/>
        <input class="form_field mb-3" type="text" name="certification" id="movieCertification" placeholder="Certification" autofocus="true"/>
        <input class="form_field mb-3" type="text" name="date" id="releasedate" placeholder="Release Date" autofocus="true"/>
        <input class="form_field mb-3" type="text" name="about" id="aboutMovie" placeholder="About Movie" autofocus="true"/>
        <input class="form_field mb-3" type="text" name="cast" id="movieCast" placeholder="Cast" autofocus="true"/>
        <input class="form_field mb-3" type="text" name="crew" id="movieCrew" placeholder="Crew" autofocus="true"/>
       
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary modal-cancel-btn" data-bs-dismiss="modal">${cancelbtn}</button>
          <button type="button" id="saveData" onclick="saveChanges()" class="btn btn-primary modal-saveChanges-btn">${saveChangesbtn}</button>
        </div>
        </from>
      </div>
    </div>
  </div>`;

  // modalWrap.querySelector('.modal-saveChanges-btn').onclick = callback;
  document.body.append(modalWrap);

  var modal = new bootstrap.Modal(modalWrap.querySelector('.modal'));
  modal.show();
}




