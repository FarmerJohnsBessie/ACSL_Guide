let submit_button = document.getElementById("submit");
submit_button.addEventListener("click", function () {
    let answer = document.getElementById("text").value;
    console.log(answer);

    fetch('/check-answer/demo/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken, // Include the CSRF token in the request headers
        },
        body: JSON.stringify({'user_answer': answer})
    })
    .then(response => response.json())
    .then(responseData => {
        let result = responseData.answer;
        console.log(result);
    })
    .catch(error => {
        console.error('Error:', error);
        // Handle any errors

    });
});