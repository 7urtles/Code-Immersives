// ----- Homework Begins -----
// creating tags
function tagCreator(tagName, className='blank'){
    newTag = document.createElement(tagName)
    newTag.classList.add(className)
    return newTag
}
// main tag element
main = document.getElementById('root')

// create a 'p' tag and set its contents
h1 = tagCreator('h1')
h1.innerHTML = 'Manipulating the DOM'

// create a div, put it on the DOM, and append the
//  'p' tag to it
divH = tagCreator('div','divH')
main.append(divH)
divH.append(h1)

// repeat for the next div but with an h2 as the lower element
h2 = tagCreator('h2')
h2.innerHTML = 'Dynamically!!'
divH = tagCreator('div', 'divH')
main.append(divH)
divH.append(h2)

// now the next 2 divisions
p = tagCreator('p', 'introMsh')
p.innerHTML = 'Welsome to Javascript!'
divP = tagCreator('div', 'divP')
main.append(divP)
divP.append(p)

p = tagCreator('p', 'introMsh')
p.innerHTML = 'It does all the Work.'
divP = tagCreator('div', 'divP')
main.append(divP)
divP.append(p)

// The h1 for the header-picker
h1 = tagCreator('h1')
h1.innerHTML = 'Show a Color Picker'
main.appendChild(h1)

// now the form
form = tagCreator('form')
label = tagCreator('label')
label.htmlFor = 'favcolor'
label.innerHTML = 'Select your favorite color:'

input = tagCreator('input')
input.id = 'favcolor'
input.setAttribute('name', 'favcolor')
input.setAttribute('type', 'color')
input.value = '#ff0000'

// items in the form, then form on the page
form.append(label)
form.append(input)
main.append(form)
// ------ Homework Ends ------




// querySelector using the same values for selection as css.
const queryDiv = document.querySelector('div')
const queryDivAll = document.querySelectorAll('div')
//create HTML elements
const btnDiv = document.createElement('div')
btnDiv.id = 'btnDiv'
// document.querySelector('main').lastElementChild.append(btnDiv)
// document.querySelector('#root').append(btnDiv)
document.querySelector('main').append(btnDiv)
const dynamicBtn = document.querySelector('h2')
dynamicBtn.id="dynamicBtn"

queryDiv.style.backgroundColor = 'red'
const blueBtn = document.createElement('button')
const cyanBtn = document.createElement('button')
blueBtn.innerHTML = "Blue!"
cyanBtn.innerHTML = "Cyan!"
blueBtn.className = "colorBtn"
cyanBtn.className = "colorBtn"
// dynamicBtn.append(blueBtn)

// Functions do work immediately (IIF(E) -> Immediately Invoked Function Expression) or when asked.

// function theFunctionName(parameter) {
//    code goes here
// }

// function changeBackgroundBlue() {
//     console.log("Blue")
//     queryDiv.style.backgroundColor = 'blue'
    
// }
// function changeBackgroundCyan() {
//     console.log("Cyan");
//     queryDiv.style.backgroundColor = 'cyan'
// }
// blueBtn.onclick=changeBackgroundBlue()
// cyanBtn.onclick=changeBackgroundCyan

// function changeBackground(param) {
//     console.log("param: ", param);
//     queryDiv.style.backgroundColor = param
// }



// new way to write functions, function expression, aka fat arrow ( => ) functions
const changeBackground = (param) => {
    console.log("param: ", param);
    queryDiv.style.backgroundColor = param
    // queryDiv.style.backgroundColor = document.querySelector('input').value
}

blueBtn.onclick = function() {changeBackground("blue")}
cyanBtn.onclick = () => changeBackground("cyan")

// create a form using JS
// const colorForm = document.createElement('form')


const colorBtn = document.createElement('button')
colorBtn.innerHTML = "Change Color"
colorBtn.className = "colorBtn"
colorBtn.onclick = () => changeBackground(document.querySelector('input').value)
document.querySelector('label').append(colorBtn)
btnDiv.append(blueBtn, cyanBtn)

const createColorBtn = () => {
     let color = document.querySelector('input').value
     let btn = document.createElement('button')
     btn.innerHTML="Change to: " + color;
     btn.onclick = () => changeBackground(color)
     btn.id = color
     btnDiv.append(btn)
}

const createBtnBtn = document.createElement('button')
createBtnBtn.innerHTML = "Create a Button"
createBtnBtn.onclick = createColorBtn
btnDiv.appendChild(createBtnBtn)