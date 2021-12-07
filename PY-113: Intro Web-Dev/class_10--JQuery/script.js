

// JQuery is a popular library for JavaScript meant to help speed up development
//   by making some tasks quicker to accomplish by needing less code from the developer
//   as compared to vanilla Javascript

// Different methods of traversing the DOM

//  Example of changing the innerHTML of an h1 element by using its class name:
$('h1.jquery-test').html("Learning JQuery")


// Event listener on a button that changes background color:

// -----[ Event Listener ]-----
$('button#jq-listener').on('click',function(event){
    // log the listener to console
    console.log('jq-listener clicked!')

    // creating random rgb values
    r = String(Math.floor(Math.random() * 255))
    g = String(Math.floor(Math.random() * 255))
    b = String(Math.floor(Math.random() * 255))

    // -----[ Changing CSS ]-----
    $('div.color-box').css('background-color', `rgb(${r},${g},${b})`)
});