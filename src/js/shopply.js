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
  var myDealsText = synchronousGetFile("/myDealsCount");
  document.getElementById("myDealsLink").innerHTML = myDealsText;
}
function moveCenter(num){
  var flowcount = document.getElementsByClassName("coverflow").length;
  for (var i=0; i < flowcount; i++) {
    //if (num != i) && (num - 1 != i) && (num + flowcount -1 != i) && (num - 2 != i) && (num + flowcount - 2 != i) && (num + 1 != i) && (num - flowcount +1 != i) && (num + 2 != i) && (num - flowcount + 2 != i) {
      var invisibleBlock = getBlockByNum(i);
      invisibleBlock.style.opacity = 0;
      invisibleBlock.style.left = "-500px";
    //}
  }
  var llBlock = getBlockByNum(num - 2);
  llBlock.style.webkitTransform = "rotateY(80deg) scale(0.6)";
  llBlock.style.left = "-50px";
  llBlock.style.opacity = 0.3;
  llBlock.style.zIndex = 1;
  var lBlock = getBlockByNum(num - 1);
  lBlock.style.webkitTransform = "rotateY(40deg) scale(0.8)";
  lBlock.style.left = "120px";
  lBlock.style.opacity = 0.9;
  lBlock.style.zIndex = 2;
  var centerBlock = getBlockByNum(num);
  centerBlock.style.webkitTransform = "rotateY(0deg) scale(1)";
  centerBlock.style.left = "300px";
  centerBlock.style.opacity = 1;
  centerBlock.style.zIndex = 3;
  var rBlock = getBlockByNum(num + 1);
  rBlock.style.webkitTransform = "rotateY(-40deg) scale(0.8)";
  rBlock.style.left = "480px";
  rBlock.style.opacity = 0.9;
  rBlock.style.zIndex = 2;
  var rrBlock = getBlockByNum(num + 2);
  rrBlock.style.webkitTransform = "rotateY(-80deg) scale(0.6)";
  rrBlock.style.left = "650px";
  rrBlock.style.opacity = 0.3;
  rrBlock.style.zIndex = 1;
}
function getBlockByNum(num){
  var flowcount = document.getElementsByClassName("coverflow").length;
 if (num >= 0 && num < flowcount) {
    return document.getElementById("object" + num);
 } else if (num < flowcount){
    var newNum = num + flowcount;
    return document.getElementById("object" + newNum);
 } else {
    var newNum = num - flowcount;
    return document.getElementById("object" + newNum);
 }
}
function getCenterNum(){
  var flowcount = document.getElementsByClassName("coverflow").length;
  for (var i=0; i < flowcount; i++) {
    var testObject = getBlockByNum(i);
    if (testObject.style.opacity == 1){
      return i;
    }
  }
}
function moveLeft(){
  var centerNum = getCenterNum();
  moveCenter(centerNum + 1);
}
function moveRight(){
  var centerNum = getCenterNum();
  moveCenter(centerNum - 1);
}
function addToDeals() {
  var centerNum = getCenterNum();
  var centerBlock = getBlockByNum(centerNum);
  var centerTitle = centerBlock.title;
  var myDealsText = synchronousGetFile("/myDealsCount?addkey=" + centerTitle);
  document.getElementById("myDealsLink").innerHTML = myDealsText;
}
function showMyDeals() {
  document.searchLink.searchstring.value = "Search...";
  document.getElementById("homeLink").title = "myDeals";
  var listData = synchronousGetFile("/list?myDeals=yes");
  document.getElementById("dealsContent").innerHTML = listData;
}
function addDealFromList(key) {
  var myDealsText = synchronousGetFile("/myDealsCount?addkey=" + key);
  document.getElementById("myDealsLink").innerHTML = myDealsText;
  shopplySearch();
}
function removeDealFromList(key) {
  var myDealsText = synchronousGetFile("/myDealsCount?removekey=" + key);
  document.getElementById("myDealsLink").innerHTML = myDealsText;
  shopplySearch();
}
function shopplySearch() {
  if (document.getElementById("homeLink").title == "myDeals"){
    var myDealString = "myDeals=yes&"
  } else {
    var myDealString = "myDeals=no&"
  }
  var search = document.searchLink.searchstring.value;
	if (search.length==0) { 
	  if (document.getElementById("homeLink").title == "allDeals"){
		  initMainPage();
		}
		return;
	}
	if (search == "Search..."){
	  search = "";
	} 
	if (window.XMLHttpRequest) {
		Xmlhttp=new XMLHttpRequest();
	} else {
		Xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
	}
	Xmlhttp.onreadystatechange=function() {
		if (Xmlhttp.readyState==4 && Xmlhttp.status==200) {
			document.getElementById("dealsContent").innerHTML=Xmlhttp.responseText;
		}
	}
	Xmlhttp.open("GET","/list?" + myDealString + "search=" + search,true);
	Xmlhttp.send();
}
function disableEnterKey(e) //don't remember where I found this function, but I always copy/paste it from other projects
{
     var key;      
     if(window.event)
          key = window.event.keyCode; //IE
     else
          key = e.which; //firefox      

     return (key != 13);
}