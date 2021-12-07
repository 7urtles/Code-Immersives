let button = document.getElementById('listener-button')
let scrollCounter = document.querySelector("#scroll-counter")
let infiniteScroll = document.getElementById('infinite-scroll')
let number = 0


function buttonListener(){
    console.log('left')
}

function scrollListener(){
    scrollCounter.innerText = number++
}

function foreverScroll(){
    pTag = document.createElement('p')
    pTag.id = 'added-text'
    pTag.innerText += `Lorem, ipsum dolor sit amet consectetur adipisicing elit. Natus eaque inventore explicabo sunt! Voluptas labore iusto commodi vitae quos maxime temporibus sunt a, similique consectetur laudantium asperiores porro eius laborum!
    Ad ut quibusdam rerum totam alias fugiat! Neque temporibus ipsam quod animi deserunt voluptatibus, quasi quae explicabo molestiae enim consequuntur fugiat et mollitia perferendis voluptatum autem iure vitae consectetur corrupti? Lorem, ipsum dolor sit amet consectetur adipisicing elit. Assumenda aliquid eos alias voluptate beatae modi, mollitia quisquam amet nihil optio, sapiente dolorem repudiandae blanditiis veniam ex! Repudiandae tempore nostrum cupiditate!`

    infiniteScroll.appendChild(pTag)
}

// Do not use () after a function name, otherwise function runs on page load
button.addEventListener("mouseleave", buttonListener)
window.addEventListener("scroll", scrollListener)
infiniteScroll.addEventListener("scroll", foreverScroll)