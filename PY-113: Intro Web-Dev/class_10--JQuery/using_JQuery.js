

// JQuery is a popular library for JavaScript meant to help speed up development
//   by making some tasks quicker to accomplish by needing less code from the developer
//   as compared to vanilla Javascript

// Script tag with link to jquery must be placed/linked in html page
//  <script src="http://code.jquery.com/jquery-latest.min.js"></script>



// -----[ Traversing the DOM ]-----

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
    $('div.color-box').css('background-color', `rgb(${r},${g},${b})`);
});


// Classes:
    // Adding:    .addClass('newClass')
    // Removing:  .removeClass('newClass')

// Accessing element text:
    // ex: $('.box-toggler').text()
// Showing or hiding content:
    // Hide: .hide()   ex:  $('div.color-box').hide()
    // Show: .show()   ex:  $('div.color-box').show()




// Toggling visibility of an element
$('.box-toggler').on('click', function(event){

    if ($('.box-toggler').text() === 'Hide box'){
        //hide color box
        $('.color-box').hide();
        //hide color changer button
        $('#jq-listener').hide();
        //flip toggleStatus boolean
        //change text in show/hide button
        $('.box-toggler').text('Show box')
        return
    }
    // code is reached only if toggleStatus is set to false
    $('.color-box').show();
    $('#jq-listener').show();
    $('.box-toggler').text('Hide box')
})