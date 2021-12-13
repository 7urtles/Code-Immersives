// Convert to vanilla Javascript to JQuery, you can ignore createElement and .id 

// querySelector using the same values for selection as css.
const queryDiv = $('div')
const queryDivAll = $('div')

const changeBackground = (param) => {
    console.log("param: ", param);
    $('.divH').css('background-color', param)
}

// Event Listeners
$('div').on('mouseenter', ()=>changeBackground('pink'))
$('div').on('mouseleave', ()=>changeBackground('red'))
$('div').on('click', ()=>alert("Hello From the First Div"))
$('#favcolor').on('change', ()=>changeBackground($('#favcolor').val()))

const scrollDiv = document.createElement('div') 
scrollDiv.id = "scrollDiv"

$('main').append(scrollDiv)
const scrollDisplay = document.createElement("h3")
scrollDisplay.id = "scrollDisplay"
$('#scrollDiv').append(scrollDisplay)
$('#scrollDiv').on('click', ()=>$('#counter').text(Number($('#counter').text())+1))
$('#scrollDiv').css('background-color', 'yellow')
$('#scrollDisplay').html("<span>Scroll Count: </span><span id='counter'>0</span>")

//function for creating a fake comment
const commentFunc = () => {
    const ptag = document.createElement('p')
    $('#scrollDiv').append(ptag)
    $('p').text("In magna migas chillwave, lo-fi banh mi bitters consectetur labore. DIY franzen velit offal vexillologist. Brunch yuccie mixtape, meggings sustainable ea jean shorts af iceland minim. Tousled snackwave vexillologist excepteur semiotics bushwick. XOXO minim seitan tbh adaptogen air plant mustache bicycle rights poke duis readymade yuccie magna iceland.")
}
for (let index = 0; index < 4; index++) {
    commentFunc()
}

$(window).on('scroll', () => $("#counter").text(Number($("#counter").text())+1))

const scrollCheck = () => {
    if ($(window).scrollTop() >= $('body').outerHeight() - $('body').innerHeight()) {
        commentFunc()
    }
}


// Event Listeners
$('div').on('mouseenter', ()=>changeBackground('pink'))
$('div').on('mouseleave', ()=>changeBackground('red'))
$('div').on('click', ()=>alert("Hello From the First Div"))
$('#favcolor').on('change', ()=>changeBackground($('#favcolor').val()))
$(window).on('scroll', scrollCheck)