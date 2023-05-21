//-----2-----
let id;
let pos = 0;

function myMove() {
    let cube = document.getElementById("animate");
    id = setInterval( function() {
        if (pos >= 350) {
            clearInterval(id);
        }
        pos++;
        cube.style.left = pos+"px";
        }, 5)
}
