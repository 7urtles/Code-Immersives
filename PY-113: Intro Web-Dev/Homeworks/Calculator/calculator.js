// Todo

//create calculator frame ✅
//create buttons ✅
//create display ✅
//take input ✅
//style 🤣
//profit


const calculator = document.getElementById('calculator')
let operation = ''

// Frame holds all calculator components
let createFrame=()=>{
    let frame = document.createElement('div')
    frame.id = 'frame'
    frame.className = 'frame'
    calculator.append(frame)
    return frame
}
createFrame()

// App output feedback display
let createDisplay=()=>{
    let displayContainer = document.createElement('div')
    let display = document.createElement('h1')
    // display container css labels
    displayContainer.id = 'displayContainer'
    displayContainer.className = 'displayContainer'
    // display css attributes
    display.className = 'display'
    display.style.animation='fadeIn 2s linear'
    display.innerText = '0'
    display.id = 'display'
    // pack elements then display to page
    displayContainer.append(display)
    calculator.append(displayContainer)
}
createDisplay()

let createKeypad=()=>{
    const padElements = [
        'AC','DEL','+/-','*',
        '7','8','9','/',
        '4','5','6','+',
        '1','2','3','-',
        '0','.','➡'
    ]
    // making the buttons that can be grouped into a flex box
    padElements.forEach((element, index) => {
        let container = document.createElement('div')
        let number = document.createElement('p')
        // give class-names/ids to elements
        container.className = 'key'
        container.id = element
        number.innerText = element
        // give click event to each button
        container.onclick =()=>{
            logicHandler(container)
        }
        container.style.animation="spin .5s linear"
        number.style.animation='spinReverse .5s linear'
        number.classList.add('noSelect')
        //add both to frame
        container.append(number)
        frame.append(container)
        calculator.append(frame)
    });
}
createKeypad()

let colorKeypad=()=>{
    for(i=0;i<10;i++){
        let key = document.getElementById(i)
        key.classList.add('numberColor')
    }
}
colorKeypad()

let logicHandler=(element)=>{
    let key = element.id
    const display = document.getElementById('display')
    switch (element.id){
        case 'AC': // Clear
            operation = ''
            display.innerText = '0'
            break;
            
        case 'DEL': // Delete
            if(operation!='undefined' & operation!=''){
                operation = String(operation).slice(0,-1)
                display.innerText = operation
            }
            if (operation === ''){
                display.innerText = '0'
            }
            break;

        case '➡': // submit operation
            if(operation === ''){
                break;
            }
            const answer = eval(operation) // Math logic? Never heard of her.
            display.innerText = answer
            operation = answer
            break;  

        case '+/-': // Leading negative symbol
            if(operation[0]==='-'){
                operation = operation.slice(1)
            }
            else if(operation===''){
                break;
            }
            else{
                operation = '-'.concat(operation)
            }
            display.innerText = operation
            break;

        default: // any number pressed
            operation += key
            display.innerText = operation
            break;
    }
}

// key event listeners
$(".key").mousedown(function(){
    this.classList.add('keyClick')
});
$(".key").mouseup(function(){
    this.classList.remove('keyClick')
});
$(".key").mouseleave(function(){
    this.classList.remove('keyClick')
});