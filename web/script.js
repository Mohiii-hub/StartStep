let zehler = 0;
const Zahlbutton = document.getElementById("Zahlbutton");
const Zahl = document.getElementById("zahl");
Zahlbutton.onclick = function(){
    zehler++;
    Zahl.innerText = zehler;

};

const FarbeWechseln = document.getElementById("Farbe");
FarbeWechseln.onclick = function(){
    document.body.classList.toggle("orange");
};