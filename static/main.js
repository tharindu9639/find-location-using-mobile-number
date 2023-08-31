function validateForm() {
    var x = document.forms["passdata"]["number"].value;
    //-----------------check empty number----------------------
    if (x == "") {
      alert("Number must be filled out");
      return false;
    }
    //-----------------check number less than 10----------------------
    if(x.length < 10) {
        alert("Number must be greater than 10");
      return false;
    } 
  }

//-----------------only input number----------------------

// function numberonly(input){
//     var num = /[^0-9]/gi;
//     input.value = input.value.replace(num,"")
//   }

