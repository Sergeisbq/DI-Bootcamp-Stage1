class Video {
    constructor(title, uploader, time) {
        this.title = title;
        this.uploader = uploader;
        this.time = time;
    }
    watch() {
        console.log(`${this.uploader} watched all ${this.time} of ${this.title}!`);
    }
}

const newVid_1 = new Video('Bronson', 'Sergei', 5100);
const newVid_2 = new Video('Scherlok', 'Alex', 7200);
newVid_1.watch();
newVid_2.watch();

const vidArr = [
    {title: 'Bronson', uploader: 'Sergei', time: 5100},
    {title: 'Scherlok', uploader: 'Alex', time: 7200},
    {title: 'Top Gun', uploader: 'Shon', time: 5700},
    {title: 'Galaxy Guard', uploader: 'Bob', time: 6200},
    {title: 'Green Book', uploader: 'Jack', time: 6750},
];

for (let item of vidArr) {
    console.log(item.title, item.uploader, item.time);
}

// vidArr.forEach(item) {
//     let film = new Video(...item);

// }