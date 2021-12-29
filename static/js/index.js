
function readURL(input) {
  if (input.files && input.files[0]) {

    var reader = new FileReader();

    reader.onload = function(e) {
      $('.image-upload-wrap').hide();

      $('.file-upload-image').attr('src', e.target.result);
      $('.file-upload-content').show();

      $('.image-title').html(input.files[0].name);
    };

    reader.readAsDataURL(input.files[0]);

  } else {
    removeUpload();
  }
}

function removeUpload() {
    $('.file-upload-input').replaceWith($('.file-upload-input').clone());
    $('.file-upload-content').hide();
    $('.image-upload-wrap').show();
  }
  $('.image-upload-wrap').bind('dragover', function () {
      $('.image-upload-wrap').addClass('image-dropping');
    });
    $('.image-upload-wrap').bind('dragleave', function () {
      $('.image-upload-wrap').removeClass('image-dropping');
  });



//function quatizer() {
//    var email = document.getElementById("smail").value;
//    var name = document.getElementById("sname").value;
//    var pass = document.getElementById("spass").value;
//    var confirm = document.getElementById("scpass").value;
//    var entry = {
//      name:  name,
//      email: email,
//      password: pass
//    };
//    if(email == "" || pass == "" || confirm== "" || name == ""){
//      document.getElementById('error2').innerHTML = 'Sorry! Fill out all required Fields!';
//      document.getElementById('error2').style.display = 'block';
//    }else{
//      if(pass !== confirm){
//        document.getElementById('error2').innerHTML = 'Aww! Password does not match, Try Again!';
//       document.getElementById('error2').style.display = 'block';
//      }
//      else{
//        fetch("/api/student/register" , {
//        method: "POST",
//        credentials: "include",
//        body: JSON.stringify(entry),
//        cache: "no-cache",
//        headers: new Headers({
//          "content-type": "application/json"
//          })
//          })
//        .then(function (response) {
//          if (response.status !== 200) {
//            console.log("Looks like there was a problem. Status code: " +response.status );
//            return;
//          }
//          response.json().then(function (data) {
//              sendEmailforVerification(email);
//              $('#myModal').modal('toggle');
//              console.log("Done");
//              document.getElementById('error2').style.display = 'none';
//              document.getElementById("smail").value = "";
//              document.getElementById("sname").value = "";
//              document.getElementById("spass").value = "";
//              document.getElementById("scpass").value = "";
//            return;
//          });
//        })
//        .catch(function (error) {
//          console.log("Fetch error: " + error);
//        });
//      }
//    }
//
//    }


  