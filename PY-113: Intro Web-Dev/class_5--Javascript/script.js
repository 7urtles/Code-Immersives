
// -----------------[ USING COOKIES ]-----------------
// In JS you should declare your variable types
// 'let' for non-changing variables, 'var' for variables needing re-assignment
let cookie_data = document.cookie;

// splitting the cookie and grabbing the second index, which is the current username
let user = {username : cookie_data.split('=')[1]};

// show the current user dictionary in the console
console.log(user)



//if the username has not been set
if (user['username'] === undefined){

    // Get a username from an alert popup
    user['username'] = window.prompt("Username:","chparmley");

    // Save the data to a cooke  cookie formatting-->  "variable_name=data;"
    document.cookie = `username=${user["username"]};`
}



// -----------------[ Changing the DOM ]-----------------
// Concept is the same for getting elements by class, tag, etc...
document.getElementById('username').innerHTML = user['username'];

// Style may also be changed via JS
document.getElementById('username').style.textShadow = '.5px .5px grey';



// -----------------[ Creating DOM Elements ]-----------------

// make an a tag
let git_link = document.createElement('a');
// setting it's link
git_link.href = 'https://github.com/chparmley/Code-Immersives/tree/main/PY-113:%20Intro%20Web-Dev/class_5--Javascript';
// assign an ID
git_link.id = 'github-link';
// Set visible link text
git_link.innerHTML = 'GitHub';
// Remove underline
git_link.style.textDecoration = 'none';
// Append the created 'a tag' to the footer-info division
document.getElementById('footer-info').appendChild(git_link);
// set text within the div to center align
document.getElementById('footer-info').style.textAlign = 'center';

// making a p tag for my author data
let author_data = document.createElement('p');
// Put my name and school in the created p tag
author_data.innerHTML = 'Charles Parmley, Code Immersives 2021'
// Append the tag to the DOM, inside of the footer-info division
document.getElementById('footer-info').appendChild(author_data);

// positioning the footer
document.getElementsByTagName('footer').style.position = 'absolute';
document.getElementsByTagName('footer').style.bottom = 0;