var like_button = document.getElementById("like-button");

like_button.addEventListener("click", function(){
    if(id === -1){
        addQuestion()
    }else{
        likeQuestion(id)
    }
});

function addQuestion(){
    const data = {
        question: question,
        type: type,
        is_multiple_choice: false, // Set to true or false as needed
        answer: answer,
        steps: '', // Set to null if not needed
        likes: 1,
        difficulty: 1,
        num_choices: null, // Number of choices
        choices: null, // Array of choices
    };

    // Send a POST request to the API
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
    window.location.replace(`/question_generator/${type}`);
}

function likeQuestion(id){
    fetch(`/update/like/${id}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken, // Include the CSRF token in the request headers
        },
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
    window.location.replace(`/question_generator/${type}`);
}

