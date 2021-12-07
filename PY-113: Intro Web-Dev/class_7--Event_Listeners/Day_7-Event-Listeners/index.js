// querySelector using the same values for selection as css.
const queryDiv = document.querySelector('div')
const queryDivAll = document.querySelectorAll('div')

const changeBackground = (param) => {
    console.log("param: ", param);
    queryDiv.style.backgroundColor = param
    // queryDiv.style.backgroundColor = document.querySelector('input').value
}

// Event Listeners

// dynamicBtn.addEventListener("mouseenter", function(){alert("Hello World")})
queryDiv.addEventListener("mouseenter", () => changeBackground("pink"))
queryDiv.addEventListener("mouseleave", () => changeBackground("red"))
queryDiv.addEventListener("click", ()=> alert("Hello From the First Div"))

document.querySelector('#favcolor').addEventListener('change', ()=>changeBackground(document.querySelector('#favcolor').value))

const scrollDiv = document.createElement('div')
scrollDiv.id = "scrollDiv"
scrollDiv.style.backgroundColor="yellow"
document.querySelector('main').append(scrollDiv)
const scrollDisplay = document.createElement("h3")
scrollDisplay.id = "scrollDisplay"
scrollDisplay.innerHTML = "<span>Scroll Count: </span><span id='counter'>0</span>"
scrollDiv.append(scrollDisplay)
// document.querySelector('#counter').innerText=2

//function to increment the scroll counter
// const scrollInc = () => {
//     // let currentVal = document.querySelector("#counter").innerText
//     // currentVal = parseInt(currentVal)
//     // currentVal = currentVal + 1
//     // or
//     // currentVal += 1
//     // document.querySelector("#counter").innerText = currentVal
//     document.querySelector("#counter").innerText++
// }
// const scrollInc = () => {
//     // let currentVal = document.querySelector("#counter").innerText
//     // currentVal++ //does not need parseInt
//     // document.querySelector("#counter").innerText = currentVal
// }
// const scrollInc = () => {
//     // document.querySelector("#counter").innerText++
// }

// scrollDiv.addEventListener('click', scrollInc)
scrollDiv.addEventListener('click', () => document.querySelector("#counter").innerText++)

//function for creating a fake comment
const commentFunc = () => {
    const ptag = document.createElement('p')
    ptag.innerText = "In magna migas chillwave, lo-fi banh mi bitters consectetur labore. DIY franzen velit offal vexillologist. Brunch yuccie mixtape, meggings sustainable ea jean shorts af iceland minim. Tousled snackwave vexillologist excepteur semiotics bushwick. XOXO minim seitan tbh adaptogen air plant mustache bicycle rights poke duis readymade yuccie magna iceland."
    scrollDiv.append(ptag)
}
for (let index = 0; index < 4; index++) {
    commentFunc()
}

window.addEventListener('scroll', () => document.querySelector("#counter").innerText++)

// using the following properties:
// window.pageYOffset / window.innerHeight / document.body.offsetHeight
// use the scroll event listener to add more ptags of hipster ipsum to the page
// every time the user gets close to the bottom of the page more should be added
// so they never reach the bottom.  They should be able to scroll infinitely.