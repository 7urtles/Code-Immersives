// Convert to vanilla Javascript to JQuery, you can ignore createElement and .id 

// querySelector using the same values for selection as css.
const queryDiv = document.querySelector('div')
const queryDivAll = document.querySelectorAll('div')

const changeBackground = (param) => {
    console.log("param: ", param);
    queryDiv.style.backgroundColor = param
}

// Event Listeners

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

const scrollCheck = () => {
    if (window.pageYOffset >= document.body.offsetHeight - window.innerHeight) {
        commentFunc()
    }
}

window.addEventListener('scroll', scrollCheck)