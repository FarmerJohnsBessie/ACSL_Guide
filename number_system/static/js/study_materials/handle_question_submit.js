let submit_button = document.getElementById("submit");
let submit_buttons = document.querySelectorAll('button[name="submit-btn"]')
submit_buttons.forEach(button => {
    button.addEventListener('click', handleSubmit);
})
function handleSubmit(){
    let id = this.id;
    let answer = document.getElementById(`${id}-input`).value;
    console.log(answer);

    fetch(`/check-answer/${filename}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken, // Include the CSRF token in the request headers
        },
        body: JSON.stringify({'user_answer': answer, 'id':id})
    })
    .then(response => response.json())
    .then(responseData => {
        let result = responseData.result;
        console.log(result);
        let result_area = document.getElementById(`${id}-result`);
        result_area.innerHTML = result;
    })
    .catch(error => {
        console.error('Error:', error);
        // Handle any errors

    });
}
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