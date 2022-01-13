//create needed constants
const rememberDiv = document.querySelector('.remember');
const forgetDiv = document.querySelector('.forget');
const form = document.querySelector('form');
const nameInput = document.querySelector('#entername');
const submitBtn = document.querySelector('#submitname');
const forgetBtn = document.querySelector('#forgetname');

const h1 = document.querySelector('h1');
const personalGreeting = document.querySelector('.personal-greeting');

//stop the form from submitting when a button is pressed
form.addEventListener('submit', function(e) {
    e.preventDefault();
});

//run function when the 'Say hello' button is clicked
submitBtn.addEventListener('click', function() {
    //store name in web storage
    localStorage.setItem('name', nameInput.value);
    //run nameDisplayCheck() to sort out displaying
    //the personalized greetings and updating the form display
    nameDisplayCheck();
});

forgetBtn.addEventListener('click', function() {
    localStorage.removeItem('name');
    nameDisplayCheck();
});

function nameDisplayCheck() {
    //check whether the 'name' data item is stored in web storage
    if (localStorage.getItem('name')) {
        //if so, display personal greeting
        let name = localStorage.getItem('name');
        h1.textContent = 'Welcome, ' + name;
        personalGreeting.textContent = 'Welcome to our website, ' + name + '! Have fun here.';
        //hide the 'remember' part of the form and show the 'forget'
        forgetDiv.style.display = 'block';
        rememberDiv.style.display = 'none';
    } else {
        //if not, display generic greeting
        h1.textContent = 'Welcome to our website ';
        personalGreeting.textContent = "Welcome to our website! Have fun here.";
        //hide the 'forget' part and show the 'remember' form
        forgetDiv.style.display = 'none';
        rememberDiv.style.display = 'block';
    }
}

//every time page loaded, check if personal greeting available
document.body.onload = nameDisplayCheck;