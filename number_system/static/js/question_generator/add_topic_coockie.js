function saveChoice() {
    const selectedChoice = document.getElementById('typeChoices').value;

    // Set the choice as a cookie with an expiration time (e.g., 7 days)
    const expirationDate = new Date();
    expirationDate.setDate(expirationDate.getDate() + 7);

    document.cookie = `userChoice=${selectedChoice}; expires=${expirationDate.toUTCString()}; path=/`;
    console.log('Cookie saved:',document.cookie);
    let json_data = {'choice': selectedChoice};

    fetch('/question_generator/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken, // Include the CSRF token in the request headers
        },
        body: json_data,
    })
    .then(response => response.json())
    .then(responseData => {
        console.log(responseData.result);
        // Handle the response as needed
    })
    .catch(error => {
        console.error('Error:', error);
        // Handle any errors
    });
}

const choices = document.getElementById('typeChoices');
choices.addEventListener('change', saveChoice);

// Function to retrieve the user's choice from the cookie on page load
window.onload = function() {
    const cookieValue = document.cookie
        .split('; ')
        .find(row => row.startsWith('userChoice='))
        ?.split('=')[1];

    if (cookieValue) {
        // If a choice is found in the cookie, set the select element value
        document.getElementById('typeChoices').value = cookieValue;
    }
};
