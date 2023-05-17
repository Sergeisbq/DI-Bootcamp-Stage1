// //-----6-----
// //----6.2----
// let div = document.getElementById("navBar");
// div.setAttribute('id', 'socialNetworkNavigation');
// console.log(div);

// //----6.3----
// let ul = document.querySelector("#socialNetworkNavigation ul");
// let li = document.createElement('li');
// let textNode = document.createTextNode("Logout");
// li.appendChild(textNode);
// ul.appendChild(li);

// //----6.4----
// console.log(ul.firstElementChild.textContent);
// console.log(ul.lastElementChild.textContent);


//-----7-----

let book1 = {
    title: "Harry Potter and the Half-Blood Prince",
    author: "J. K. Rowling",
    image: "https://static.wikia.nocookie.net/harrypotter/images/9/95/Half-Blood_Prince_new_cover.jpg/revision/latest/scale-to-width-down/668?cb=20170109054810",
    alreadyRead: false,
}

let book2 = {
    title: "Sapiens: A Brief History of Humankind",
    author: "Yuval Noah Harari",
    image: "https://jamesclear.com/wp-content/uploads/2016/06/sapiens-by-yuval-noah-harari.jpg",
    alreadyRead: true,
}

let allBooks = [book1, book2];

let listOfBooks = document.getElementsByClassName("listBooks")[0];

for (let i = 0; i < allBooks.length; i++) {
    let book = allBooks[i];
    let bookDiv = document.createElement("div");

    let imageElm = document.createElement("img");
    imageElm.setAttribute('src', book.image);
    imageElm.style.width = "100px";

    let detailsElm = document.createElement("p");
    detailsElm.textContent = `${book.title} written by ${book.author}`;

    if (book.alreadyRead) {
        detailsElm.style.color = "red";
      }

    bookDiv.appendChild(imageElm);
    bookDiv.appendChild(detailsElm);

    listOfBooks.appendChild(bookDiv);
}
