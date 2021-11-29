console.log('running')

// Account form submit button
function button_click(){
    // Gathering user data
    var fname = document.getElementById('fname').value;
    var lname = document.getElementById('lname').value;
    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;

    // printing data to console
    console.log(fname, lname, email)

    // alerting the user
    alert('Thank you ' + fname + '! Your submission has been recorded.')
}


// Search form submit button
function search_it(){
    // Gathering search form data
    var search_data = document.getElementById('search').value
    var engine = document.getElementById('search-provider').value

    // Open new window using search form data
    window.open('https://' + engine + '/search?q=' + search_data);
}