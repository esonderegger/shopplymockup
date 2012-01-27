function synchronousGetFile(url) {
  if (window.XMLHttpRequest) {              
    AJAX=new XMLHttpRequest();              
  } else {                                  
    AJAX=new ActiveXObject("Microsoft.XMLHTTP");
  }
  if (AJAX) {
     AJAX.open("GET", url, false);                             
     AJAX.send(null);
     return AJAX.responseText;                                         
  } else {
     return false;
  }                                             
}
function initMainPage() {
  var browseData = synchronousGetFile("/browse");
  document.getElementById("dealsContent").innerHTML = browseData;
  moveCenter(3);
}
function moveCenter(num){
  var llBlock = getBlockByNum(num - 2);
  llBlock.style.webkitTransform = "rotateY(80deg) scale(0.5)";
  llBlock.style.left = "0px";
  llBlock.style.opacity = 0.3;
  llBlock.style.zIndex = 1;
  var lBlock = getBlockByNum(num - 1);
  lBlock.style.webkitTransform = "rotateY(40deg) scale(0.8)";
  lBlock.style.left = "150px";
  lBlock.style.opacity = 0.9;
  lBlock.style.zIndex = 2;
  var centerBlock = getBlockByNum(num);
  centerBlock.style.webkitTransform = "rotateY(0deg) scale(1)";
  centerBlock.style.left = "300px";
  centerBlock.style.opacity = 1;
  centerBlock.style.zIndex = 3;
  var rBlock = getBlockByNum(num + 1);
  rBlock.style.webkitTransform = "rotateY(-40deg) scale(0.8)";
  rBlock.style.left = "475px";
  rBlock.style.opacity = 0.9;
  rBlock.style.zIndex = 2;
  var rrBlock = getBlockByNum(num + 2);
  rrBlock.style.webkitTransform = "rotateY(-80deg) scale(0.5)";
  rrBlock.style.left = "650px";
  rrBlock.style.opacity = 0.3;
  rrBlock.style.zIndex = 1;
}
function getBlockByNum(num){
 if (num >= 0) {
    return document.getElementById("object" + num);
 } else {
    var flowcount = document.getElementsByClassName("coverflow").length;
    var newNum = num + flowcount;
    document.getElementById("label").innerHTML = newNum;
    return document.getElementById("object" + newNum);
 }
}