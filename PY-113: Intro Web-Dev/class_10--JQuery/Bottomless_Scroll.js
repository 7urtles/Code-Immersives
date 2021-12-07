

// keeping track of how many posts there are
let counter = 1

makePost = () =>{
    // create new p-tag element
    let recurringText = document.createElement('p')
    // set its text to the counter number
    recurringText.innerText = `Post #`+counter
    // increase counter
    counter++
    // return the resulting p-tag
    return recurringText
}

// Listener for the scrollbox
$('.bottomless-scrollbox').on('scroll', ()=>{
    // call the post maker function and add its result to the DOM
    $('.bottomless-scrollbox').append(makePost())
})