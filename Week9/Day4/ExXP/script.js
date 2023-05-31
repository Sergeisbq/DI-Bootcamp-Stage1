let divC = document.getElementById('content');
let divContainer = document.createElement('div');
let divFr = document.createElement('div');
let button = document.createElement('button');

divContainer.classList.add("mainDiv");
divFr.setAttribute('id','toAddCont');
button.classList.add("toFindBtn");
button.textContent = "Find Someone";
button.addEventListener("click", gifAsync);

divC.appendChild(divContainer);
divContainer.appendChild(divFr);
divContainer.appendChild(button);

let pName = document.createElement('p');
pName.classList.add("textContent");
pName.textContent = '';

let pHeight = document.createElement('p');
pHeight.classList.add("textContent");
pHeight.textContent = '';



let pGender = document.createElement('p');
pGender.classList.add("textContent");
pGender.textContent = '';

let pByear = document.createElement('p');
pByear.classList.add("textContent");
pByear.textContent = '';

let pHomew = document.createElement('p');
pHomew.classList.add("textContent");
pHomew.textContent = '';

divFr.appendChild(pName);
divFr.appendChild(pHeight);
divFr.appendChild(pGender);
divFr.appendChild(pByear);
divFr.appendChild(pHomew);


function rndRange(a,b){
    return Math.round(Math.random()*(b-a))+a;
  }

async function gifAsync() {

    try {
        pName.textContent = '';
        pHeight.textContent = '';
        pGender.textContent = '';
        pByear.textContent = '';
        pHomew.textContent = '';

        let pLoading = document.createElement('p');
        pLoading.setAttribute('id','pLoading');
        pLoading.classList.add("textContent");
        pLoading.textContent = '';

        let pLoadingIcon = document.createElement('p');
        pLoadingIcon.setAttribute('id','pLoadingIcon');
        pLoadingIcon.classList.add("textContent");
        pLoadingIcon.textContent = '';
        pLoadingIcon.style.marginLeft = '49%';

        divFr.appendChild(pLoading);
        divFr.appendChild(pLoadingIcon);

        pLoading.textContent = "Loading";
        divFr.classList.add("fa-3x");
        pLoadingIcon.classList.add("fa-solid");
        pLoadingIcon.classList.add("fa-spinner");
        pLoadingIcon.classList.add("fa-spin-pulse");

        let number = rndRange(1, 99);
        let url = `https://www.swapi.tech/api/people/${number}`;
        const res = await fetch(url);
        const data = await res.json();
        planetUrl = data.result.properties.homeworld;
        const res2 = await fetch(planetUrl);
        const data2 = await res2.json();

        pLoading.remove();
        pLoadingIcon.remove();

        pName.textContent = data.result.properties.name;
        pHeight.textContent = `Height: ${data.result.properties.height}`;
        pGender.textContent = `Gender: ${data.result.properties.gender}`;
        pByear.textContent = `Birth Year: ${data.result.properties.birth_year}`;
        pHomew.textContent = `Home World: ${data2.result.properties.name}`;

        console.log(data.result.properties.name);
        console.log(data);

    }

    catch(err) {
        
        let pLoad = document.getElementById("pLoadingf");
        pLoad.remove();
        let pLoadIc = document.getElementById("pLoadingIcon");
        pLoadIc.remove();

        pName.textContent = "Oh No! That person isnt available.";
        pHeight.textContent = '';
        pGender.textContent = '';
        pByear.textContent = '';
        pHomew.textContent = '';
        console.log(err);
    }   
}



