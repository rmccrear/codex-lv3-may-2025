// run this command to run the program
// node invert-images.js
/**
 * 
 * @param {Array} imageList A list with the pixels to display
 * @param {Number} width Width of the image
 * @param {Number} height Height of the image
 */
function printImage(imageList, width, height) {
    let rows = []
    for(let i=0; i<height; i++) {
        rows.push(imageList.slice(i*width, (i+1)*width));
    } 
    for(let i=0; i<rows.length; i++) {
        console.log(rows[i].join(" "));
    }
    console.log("\n");
    console.log(imageList.join("") + "\n\n");
}

// This string of a dog is from: https://studio.code.org/courses/csd-2025/units/6/lessons/4/levels/3
const dogString = "111111111111101111111111101111100111101111100001101111100001110000000111110000000111110000000111110111110111110111110111110111110111111111111111";
const dogList = dogString.split("");
console.log("dog image...");
printImage(dogList, 12, 12);

const invertedDogList = [];
for(let i=0; i<dogList.length; i++) {
    if(dogList[i]== "0") {
        invertedDogList[i] = "1"
    } else if(dogList[i] == "1") {
        invertedDogList[i] = "0"
    }   
}
console.log("inverted...");
printImage(invertedDogList, 12, 12);
