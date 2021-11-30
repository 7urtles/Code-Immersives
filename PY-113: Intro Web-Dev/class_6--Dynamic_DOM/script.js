const header = document.querySelector('header')
const body = document.querySelector('body')

const main = document.querySelector('main')
const footer = document.querySelector('footer')

header.style.backgroundColor = 'aliceblue'
body.style.backgroundColor = 'black'
main.style.backgroundColor = 'aliceblue'
footer.style.backgroundColor = 'aliceblue'



// Dynamic list creation

// define parent to add elements to
let ul = document.querySelector('ul')

for (let counter = 0; counter < 5; counter++){
    // When creating elements withing a loop, you must re-declare the 
    //   variable that is count to be added multiplt times
    let li = document.createElement('li')

    // adjust the lists inner contents to inclue the incremented counter
    li.innerHTML = 'Item ' + String(counter);

    // append the dynamic list element to to the unorded-list
    ul.appendChild(li);
}

// function to print to console
function buttonClick(){
    console.log('Button Clicked!')
}

// Creating a button and giving it a function for the click event
let button = document.createElement('button')
button.innerHTML = 'Hello'

// assign the button the entire function by not using the ()
main.appendChild(button)