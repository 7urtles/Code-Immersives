


let counter = 1
function makePost(){
    let recurringText = document.createElement('p')

    recurringText.innerText = `Post #`+counter
    counter++
    return recurringText
}

// Listener for the scrollbox

$('.bottomless-scrollbox').on('scroll', function(){
    console.log('scrolling')
    $('.bottomless-scrollbox').append(makePost())
})