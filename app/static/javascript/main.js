let p = document.getElementById('password');
let btn = document.getElementById('show');

function toggle(){
  p.type = (p.type === "password") ? "text" : "password";
}

btn.addEventListener(onclick, toggle)