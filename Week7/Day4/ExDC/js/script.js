let planets = [

    {name: "Mercury", moons: 0},
    {name: "Venus", moons: 0},
    {name: "Earth", moons: 1},
    {name: "Mars", moons: 0},
    {name: "Jupiter", moons: 2},
    {name: "Saturn", moons: 3},
    {name: "Uranus", moons: 4},
    {name: "Neptune", moons: 0},

];

for (let planet of planets) {
    let div = document.createElement('div');
    div.classList.add("planet");
    div.classList.add(planet.name.toLowerCase());
    console.log("div", div);

    let section = document.getElementsByClassName("listPlanets")[0];
    section.appendChild(div);

    for (let i = 0; i < planet.moons; i++) {
        let moonDiv = document.createElement('div');
        moonDiv.classList.add("moon");
        moonDiv.style.top = i * 12 + "px";
        moonDiv.style.left = i * 12 + "px";
        div.appendChild(moonDiv);
        
    }

}


