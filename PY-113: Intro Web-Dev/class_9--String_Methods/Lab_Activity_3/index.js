document.title = "JS Methods"
const titleS = document.createElement('h1')
titleS.id = "titleS"
titleS.innerText="Javacript String Methods"
const titleA = document.createElement('h1')
titleA.id = "titleA"
titleA.innerText="Javacript Array Methods"
document.querySelector('#root').append(titleS, titleA)
const divS = document.createElement('div')
const divA = document.createElement('div')
divS.id = 'divS'
divA.id = 'divA'
document.querySelector('#titleS').append(divS)
document.querySelector('#titleA').append(divA)

const testArr = [1,2,3,4,5] 

// ------------Map,Filter,Reduce---------------

// map is just a standard for loop that has to return a value every loop
//
let mapArr = testArr.map(element => element+1)  //single function implies return
let mapFuncArr = testArr.map(element => {       // if you want to use a return
    let newVal = element + 2                    // you to write a function with {}
    newVal = newVal + element
    return newVal
})

// filter is the same as map but only returns the original value/element and only if the logic passes
//
let filterArr = testArr.filter((element,index) => index % 2 == 0)
let filterFuncArr = testArr.filter((element,index) => {
    if(index > 0) {
        if(element % 2 === 0) {
            return element
        }
    } 
})

// reduce as up all the value in an array, can also add a starting value (the 10 below)
let reduceArr = testArr.reduce((total, element) => total + element,10)

const numArr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
 
// -----------JS operators-----------
//  >,>=
//  <,<=
//  ==, ===  //triple equals has match both value and the type
//  !=, !== //same as above, but "not equals"
//  && and
//  || or
//  % mod (remainder)

//display an array of the numbers from numArr that are evenly divisible by 3 or 5 in the array div
//
// ><---- no built in functions ----><
//
//  ----as-a-function----
// const divArr = (array) => {
//     let divArr = []
//     for (let index = 0; index < array.length; index++) {
//         let element = numArr[index];
//         if (element % 3 === 0 || element % 5 === 0) {
//             divArr.push(element)
//         }
//     }
//     return divArr
// }
// divA.append(divArr(numArr))
//// // -----map is the same as the function above
// it uses a default for loop and returns a value every loop
// pushes into a new array and then returns that new array  
//  //   -----
// // numArr.map(element => {                          
//     if (element % 3 === 0 || element % 5 === 0) {
//            divArr.push(element)
//         }
// })
// //  -------------------------------------------------


//   ----no-functions----
// const divArr = []
//
//
// for (let index = 0; index < numArr.length; index++) {
//     const element = numArr[index];
//     if (element % 3 === 0 || element % 5 === 0) {
//         divArr.push(element)
//     }
// }
// divA.append(divArr)
//

//   ><----built in functions----><
//
// ----verbose----
// const divArr = numArr.filter(element => {
//     if (element % 3 === 0 || element % 5 === 0) {
//         return element
//     }
// })
// divA.append(divArr)
//
// ----middle_ground----
// by default a single line filter will return the element if it passes the logic check
// const divArr = numArr.filter(element => (element % 3 === 0 || element % 5 === 0))  
// divA.append(divArr)
//
// ----concise----
// divA.append(numArr.filter(element => (element % 3 === 0 || element % 5 === 0)))
//
//
// -----------------JS Parameters-------------------
// in javascript parameters are handled not by name but by order of input.
// i.e. 
// numArr.map(element => element) 
// is the same as  
// numArr.map(unicorn => unicorn) 
// or
// numArr.map((element, index, array) => element + array[index])
// is the same as  
// numArr.map((cat, dog, bird) => cat + bird[dog])
//
// let animalArr = numArr.map((cat, dog, bird) => cat + bird[dog])
// let normalArr = numArr.map(e => e*2)
// let fauxIndexArr = numArr.map(index => index*2)
// let indexArr = numArr.map((element, index) => index*2)
//
// js parameters can also have a default value
// const colorDivs = (red=255, green=255, blue=255) => {
//     // document.querySelector('#titleA').style.backgroundColor = 'rgb(' + red + ',' + green + ',' + blue + ')'
//     document.querySelector('#titleA').style.backgroundColor = `rgb(${red},${green},${blue})`
// }
// if you do not want to define a parameter use undefined
// colorsDiv(undefined,128,0)

// JS String Methods
// let newString = "Hello"
// newString = newString + " " + "World"
// document.querySelector("#divS").append(newString)
// const brk = document.createElement('br')
// document.querySelector("#divS").append(brk)
// let hello = "hello"
// let world = "World"
// let helloworld = hello.concat(world)
// document.querySelector("#divS").append(helloworld)
// for (let index = 0; index < newString.length; index++) {
//     const element = newString[index];
//         if (newString.charAt(index) === helloworld.charAt(index) ){
//             console.log(newString.charAt(index));
//             console.log(helloworld.charAt(index))
//             console.log("True")
//          } else {
//             console.log(newString.charAt(index));
//             console.log(helloworld.charAt(index))
//             console.log("False")
//          }
// }

//  Split and Join

const capitolize = (param, type) => {
    let capitol = param.charAt(0).toUpperCase()
    console.log(param, type);
    if (type === 'letter') {
        return capitol
    } 
    let splitparam = param.split(param.charAt(0))
    console.log('!@-------capitol-------@!')
    console.log(splitparam.join(capitol))
    return splitparam.join(capitol)
}
const propername = (param) => {
    //"new york city"
    // console.log('!@-------split--" "-----@!')
    // console.log(param.split(" "))
    // ['new', 'york', 'city']
    // console.log('!@-------split--""-----@!')
    // console.log(param.split(""))
    // ['n', 'e', 'w', ' ', 'y', 'o', 'r', 'k', ' ', 'c', 'i', 't', 'y']
    
    splitParam = param.split(" ")
    const capitolArray = splitParam.map(element => capitolize(element)) //callback
    // ['New', 'York', 'City']
    const finalOutput = capitolArray.join(" ")
    // "New York City"
    // document.querySelector('#divS').append(finalOutput)
    return finalOutput
}
const acronymFunc = (param) => {
    splitParam = param.split(" ")    
    


    // -----[ Charles Code Begins ]-----
    // -- Covers capitalization cases --
    // array of words to ignore
    const ignoreArray = ['A', 'THE', 'OF', 'FOR', 'AND']
    // loop over words to be used in acronym
    for (i=0;i<splitParam.length;i++){
        // if its lowercase version is in the array
        if(ignoreArray.indexOf(splitParam[i].toUpperCase()) > -1){
            // remove it
            splitParam.splice(i,1)
            // and do not allow the counter to increase, since the array size decreased
            i--
        }
    }
    // -----[ Charles Code Ends ]-----



    const capitolArray = splitParam.map(element => capitolize(element, 'letter'))
    let finalOutput = capitolArray.join(".")
    finalOutput += "."
    return finalOutput
}

// propername("new york city")
// console.log(capitolize("hello"))

const btnHelper = (funcName, inputValue) => {
    console.log(funcName, inputValue);
    let output;
    if (funcName === 'propername') {
        output = propername(inputValue)
    }
    if (funcName === 'capitolize') {
        output = capitolize(inputValue)
    }
    if (funcName === 'acronym') {
        output = acronymFunc(inputValue)
    }
    document.querySelector('#divOutput').append(output)
} 

let stringInput = document.createElement('input')
stringInput.id = 'stringInput'
document.querySelector('#divS').append(stringInput)
let properBtn = document.createElement('button')
let capitolBtn = document.createElement('button')
let acronymBtn = document.createElement('button')
properBtn.innerText = 'Proper Name IT!'
properBtn.onclick = () => btnHelper('propername', stringInput.value)
capitolBtn.innerText = 'Capitolize IT!'
capitolBtn.onclick = () => btnHelper('capitolize', stringInput.value)
acronymBtn.innerText = 'Acronym IT!'
acronymBtn.onclick = () => btnHelper('acronym', stringInput.value)

document.querySelector('#divS').append(properBtn,capitolBtn,acronymBtn)

const divOutput = document.createElement('div')
divOutput.id = "divOutput"
document.querySelector('#divS').append(divOutput)
