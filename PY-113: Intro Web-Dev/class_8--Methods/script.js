document.title = 'JS Methods'
let mainDiv = document.getElementById('root')
const lineBreak = document.createElement('br')

// -----[ String Methods ]-----
// Section Title
const titleS = document.createElement('h1')
titleS.id = 'titleS'
titleS.innerText = 'JavaScript String Methods'

// Section Div
let stringDiv = document.createElement('div')
stringDiv.id = stringDiv

// String Section Content





// -----[ Array Methods ]-----
// Section Title
const titleA = document.createElement('h1')
titleA.id = ('titleA')
titleA.innerText = 'JavaScript Array Methods'

// Section Div
let arrayDiv = document.createElement('div')
arrayDiv.id = arrayDiv

// Array Section Content

// creating a test array with a length of 20
function arrayMaker(number){
    let newArray = []
    for (let i=1; i<number+1; i++){
        // .push() works similar to .append() in python
        newArray.push(i)
    }
    return newArray
}
let testArray = arrayMaker(20)

// Display numbers in array that are divisible by 3 or 5

function div3or5(localArray){
    localArray.forEach(element => {
        if (element % 3 === 0 || element % 5 === 0){
        console.log(element)
        }
    });
}
// div3or5(testArray)


// adding descriptors to the DOM
let filterTitle = document.createElement('h3')
filterTitle.innerText = '.filter():'
let filterDescriptor = document.createElement('p')
filterDescriptor.innerText = 'Iterates a list, and returns non "undefined" or "non-zero" results.'
arrayDiv.append(filterTitle, filterDescriptor)

// -----[ Filter ]-----
// same as above but using .filter(), returning, and adding to the DOM instead of console.logging
arrayDiv.append(testArray.filter(element=>{
    if (element % 3 === 0 || element % 5 === 0){
        return element
    }
}))

// .push()
methodPush = document.createElement('p')
methodPush.innerText = '.push() adds an item to the end of an array'
arrayDiv.append(methodPush)


// .splice()
methodSplice = document.createElement('p')
methodSplice.innerText = '.splice() changes contents of an array by removing or replacing existing elements and/or adding new elements in their place.'
arrayDiv.append(methodSplice)

// .filter()
// .map()


// Insert elements to page
mainDiv.append(titleS, stringDiv, titleA, arrayDiv)