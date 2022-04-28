function DOM() {

var elems_p = document.getElementsByTagName("p");
console.log(elems_p);
for(var i = 0; i < elems_p.length; i++){
    console.log("elems_p[i] ", elems_p[i])
   }


console.log("document.getElementById('id') ", document.getElementById("id"));
console.log("document.getElementsByClassName('class'') ", document.getElementsByClassName("class"));
console.log("document.getElementsByName('name') ", document.getElementsByName("name"));



console.log("document.querySelectorAll('#id') ", document.querySelectorAll("#id"))
console.log("document.querySelectorAll('div') ", document.querySelectorAll("div"))
console.log("document.querySelectorAll('div p') ", document.querySelectorAll("div p"))
console.log("document.querySelector('p') ", document.querySelector("p"))
console.log("document.querySelectorAll('p') ", document.querySelectorAll("p"))


    
var elems_div = document.getElementsByTagName("div");
console.log("elems_div ", elems_div);
    for(var i = 0; i < elems_div.length; i++){
    console.log("elems_div[i] ", elems_div[i])
    }
for(var i = 0; i < elems_div.length; i++){
    console.log("document.querySelector('div').children ", document.querySelector("div").children);
    }
for (let value of elems_div) {
  console.log(" value.innerHTML", value.innerHTML);}
alert("оповещение для отладки");
  
}