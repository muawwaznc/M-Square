// BecomeSeller.html
function checkPassword() {
  var pass = document.getElementById("password");
  var cPass = document.getElementById("c-password");
  var btn = document.getElementById("submit-btn");
  if (!(pass.value === cPass.value) || pass.value === "") {
    pass.style.backgroundColor = "rgb(255, 0, 0, .5)";
    cPass.style.backgroundColor = "rgb(255, 0, 0, .5)";
    btn.disabled = true;
  } else {
    pass.style.backgroundColor = "rgb(255, 255, 255)";
    cPass.style.backgroundColor = "rgb(255, 255, 255)";
    btn.disabled = false;
  }
}
