document.getElementById("navbar").innerHTML = `
    <div class="topnav">
        <div>
             <button id="Farbe">orange Modo</button>
        </div>
        <a href="index.html" class="active">Persian Kitchen</a>
            <div id="myLinks">
                <a href="index.html">Home</a>
                <a href="uberMich.html">uberMich</a>
                <a href="contact.html">Contact</a>
            </div>
        <a href="javascript:void(0);" class="icon" onclick="myFunction()">
            <i class="fa fa-bars"></i>
        
        </a>
    </div>
`;

function myFunction() {
    const x = document.getElementById("myLinks");
    if (x.style.display === "block") {
        x.style.display = "none";
    } else {
        x.style.display = "block";
    }
}