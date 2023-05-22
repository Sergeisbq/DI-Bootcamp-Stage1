let client = "John";

const groceries = {
    fruits : ["pear", "apple", "banana"],
    vegetables: ["tomatoes", "cucumber", "salad"],
    totalPrice : "20$",
    other : {
        payed : true,
        meansOfPayment : ["cash", "creditCard"]
    }
}

const displayGroceries = () => {
    groceries.fruits.forEach((item, i, arr) => {
        console.log(item);
    });
}

const cloneGroceries = () => {
    let user = client;
    user = "Betty";
    let shopping = groceries;
    shopping.totalPrice = '35$';
    shopping.other.payed = false;
}

cloneGroceries();
console.log(client);



