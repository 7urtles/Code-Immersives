const header = document.querySelector('header')
const body = document.querySelector('body')

const main = document.querySelector('main')
const footer = document.querySelector('footer')

header.style.backgroundColor = 'aliceblue'
body.style.backgroundColor = 'rgb(246, 155, 155)'
main.style.backgroundColor = 'aliceblue'
main.style.borderRadius = '.5rem'
main.style.padding = '1rem'
footer.style.backgroundColor = 'aliceblue'



// -------[ Dynamic list creation ]-------

// define parent to add elements to
let ul = document.querySelector('ul')

let counter = 0
// changing background color0
function changeColor(){
    r = Math.floor(Math.random()*255);
    g = Math.floor(Math.random()*255);
    b = Math.floor(Math.random()*255);
    a = Math.floor(Math.random()*100)/100;
    console.log(a)

    let color = `rgba(${r}, ${g}, ${b}, ${a})`
    document.getElementById('body').style.backgroundColor = color
}
// function to display alert
function addItem(){
    if (counter<10){
        counter++
        // When creating elements withing a loop, you must re-declare the 
        //   variable that is count to be added multiplt times
        let li = document.createElement('li')
        // adjust the lists inner contents to inclue the incremented counter
        li.innerHTML = document.getElementById('list-input').value

        // append the dynamic list element to to the unorded-list
        ul.appendChild(li);
    }
    else{
        alert("Sorry, no more than 10 items allowed")
    }
}

// remove last item of list
function removeItem(){
    if (counter>0){
        lastItem = document.getElementById('dynamic-list').lastElementChild
        console.log(lastItem)
        ul.removeChild(lastItem)
        counter--
    }
}

// Creating an add item button and giving it a function for the click event
let colorButton = document.createElement('button')
let addButton = document.createElement('button')
let removeButton = document.createElement('button')

// inner text of buttons
colorButton.innerHTML = 'Change Color'
addButton.innerHTML = 'Add Item'
removeButton.innerText = 'Remove Item'

// assign the button the entire function by not using the ()
colorButton.onclick = changeColor
addButton.onclick = addItem
removeButton.onclick = removeItem

// adding all the buttons to the page
document.getElementById('bg-button').appendChild(colorButton)
document.getElementById('add-button').appendChild(addButton)
document.getElementById('remove-button').appendChild(removeButton)
