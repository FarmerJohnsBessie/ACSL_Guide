function solveExpression() {
    var expression = document.getElementById("expression").value;
    let data = {
        'expression':expression,
    }
    fetch('/solve/prefix_infix_postfix/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken, // Include the CSRF token in the request headers
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(responseData => {
        document.getElementById("output").innerText = 'Result:'+responseData['output'];
        // Handle the response as needed
    })
    .catch(error => {
        console.error('Error:', error);
        // Handle any errors
    });

}

function solveEquation() {
    var bit_string_length = document.getElementById('bit-string-length').value;
    var equation = document.getElementById("equation").value;
    let data = {
        'equation':equation,
        'bit_string_length': bit_string_length,
    }
    fetch('/solve/prefix_infix_postfix/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken, // Include the CSRF token in the request headers
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(responseData => {
        document.getElementById("output").innerText = 'Result:'+responseData['output'];
        // Handle the response as needed
    })
    .catch(error => {
        console.error('Error:', error);
        // Handle any errors
    });

}