function onLT(){
  setTimeout(openBar, 2000); 
}
var nav = true;
function closeBar() {
    document.querySelector(".sb-sidebar").style.width = "0px";
    document.querySelector(".sb-close").style.right = "0%";
    document.querySelector(".sb-close").innerHTML = "&#9776";
    nav = true;
}
function openBar() {
    document.querySelector(".sb-sidebar").style.width = "250px";
    document.querySelector(".sb-close").style.right = "15%";
    document.querySelector(".sb-close").innerHTML = "X";
    nav = false;
}
function toggleNav() {
    if (nav) {
      openBar();  
    } else {
      closeBar();
    }
}
function openSignin(){
  location.href = "/login"
}

var enrollbtn = document.getElementsByClassName("enroll_stucor")

enrollbtn.addEventListener('click',function()
  {
    var subjectid = this.dataset.s
    console.log(subjectid) 
    console.log(user) 
  })

