let zehler = localStorage.getItem("besucherZehler");
const besucherZehler = document.getElementById("besucherZehler");
const Zahl = document.getElementById("zahl");
zehler++;
localStorage.setItem("besucherZehler",zehler);
besucherZehler.innerText = zehler;

const FarbeWechseln = document.getElementById("Farbe");
FarbeWechseln.onclick = function(){
    document.body.classList.toggle("orange");
};