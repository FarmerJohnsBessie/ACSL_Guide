document.getElementById('generate-btn').addEventListener('click', function() {
    // This is where you would call your backend API to generate a question and answer
    // For demo purposes, we're just simulating this with placeholder content
    disableGeneration();
    console.log('Generating question...');
    const questionType = document.getElementById('typeChoices').value;
    const json_data = JSON.stringify({'difficulty': document.getElementById('difficulty').value, 'additional-prompt': document.getElementById('additional-prompt').value});
    fetch(`/generate/${questionType}/`,{
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken, // Include the CSRF token in the request headers
        },
        body: json_data,
    })
    .then(response => response.json())
    .then(data => {
        enableGeneration();
        const inputString = data.question;
        const parts = inputString.split(/Problem:|Steps:|Answer:/);

        // Remove empty strings from the result
        const result = parts.filter(part => part.trim() !== "");

        // Output the result
        console.log(result);

        document.getElementById('question-output').value = result[0].trim();
        document.getElementById('steps-output').value = result[1].trim();
        document.getElementById('answer-output').value = result[2].trim();
        displayQuestion();
        displaySteps();
        displayAnswer();
    });
});

document.getElementById('display-question-button').addEventListener('click', displayQuestion);
document.getElementById('display-steps-button').addEventListener('click', displaySteps);
document.getElementById('display-answer-button').addEventListener('click', displayAnswer);

function displayQuestion() {
    const question = document.getElementById('question-output').value;
    let display_area = document.getElementById('question-display');
    display_area.innerHTML = question;
    MathJax.typeset([display_area]);
}

function displaySteps() {
    const steps = document.getElementById('steps-output').value;
    let display_area = document.getElementById('steps-display');
    display_area.innerHTML = steps;
    MathJax.typeset([display_area]);
}

function displayAnswer() {
    const answer = document.getElementById('answer-output').value;
    let display_area = document.getElementById('answer-display');
    display_area.innerHTML = answer;
    MathJax.typeset([display_area]);
}

function clearEverything() {
    document.getElementById('question-output').value = "";
    document.getElementById('steps-output').value = "";
    document.getElementById('answer-output').value = "";
    document.getElementById('question-display').innerHTML = "";
    document.getElementById('steps-display').innerHTML = "";
    document.getElementById('answer-display').innerHTML = "";
    document.getElementById('difficulty-number').value = "";
    document.getElementById('additional-prompt').value = "";
}

function disableGeneration(){
    document.getElementById('generate-btn').disabled = true;
    // make the button not clickable
    document.getElementById('typeChoices').disabled = true;
    document.getElementById('difficulty').disabled = true;
    document.getElementById('additional-prompt').disabled = true;
}

function enableGeneration(){
    document.getElementById('generate-btn').disabled = false;
    document.getElementById('typeChoices').disabled = false;
    document.getElementById('difficulty').disabled = false;
    document.getElementById('additional-prompt').disabled = false;
}


document.getElementById('add-db-btn').addEventListener('click', function() {
    // This is where you would handle adding the generated question and answer to the database
    // You would need to send this data to your backend API that handles database insertion
    const data = {
        question: document.getElementById('question-output').value,
        type: document.getElementById('typeChoices').value,
        is_multiple_choice: false, // Set to true or false as needed
        answer: document.getElementById('answer-output').value,
        steps: document.getElementById('steps-output').value,
        likes: 0,
        difficulty: document.getElementById('difficulty-number').value,
        num_choices: null, // Number of choices
        choices: null, // Array of choices
    };
    fetch('/api/questions/create/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken, // Include the CSRF token in the request headers
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(responseData => {
        console.log('Question created:', responseData);
        // Handle the response as needed
    })
    .catch(error => {
        console.error('Error:', error);
        // Handle any errors
    });
    clearEverything();
});