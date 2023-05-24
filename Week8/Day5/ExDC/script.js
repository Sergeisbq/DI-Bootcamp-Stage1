const isAnagram = (param1, param2) => {
    let a = param1.toLowerCase().split('').sort().join('').trim();
    let b = param2.toLowerCase().split('').sort().join('').trim();
    for (i in a) {
        if (a[i] == b[i]) {
            console.log('This is an anagram');
        }
        else {
            console.log('This is not an anagram');
        }
    }
    console.log(a);
    console.log(b);
}

isAnagram("Astronomer", "Moon starer");
isAnagram("School master", "The classroom");
isAnagram("The Morse Code", "Here come dots");
isAnagram("Astronomer", "Here come dots");