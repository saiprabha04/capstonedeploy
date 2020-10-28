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
function resp(){
  var r= document.getElementById("res");
  alert(r)
}

var enrollbtn = document.getElementsByClassName("enroll_stucor")

for (var i = 0 ; i < enrollbtn.length; i++) {
  enrollbtn[i].addEventListener('click',function(){
    var subjectid = this.dataset.s
    if(user)
    {
      addEnroll(user,subjectid)
      alert("Enrolled successfully")
    }
  })
}

function addEnroll(user,subjectid){
  console.log('Sending data...')

  var url = '/enroll_course/'
  fetch(url, {
    method:'POST',
    headers:{
      'Content-Type':'application/json',
      'X-CSRFToken':csrftoken,
    },
    body:JSON.stringify({'subjectid':subjectid})
  })

  .then((response) => {
    return response.json()
  })
}
