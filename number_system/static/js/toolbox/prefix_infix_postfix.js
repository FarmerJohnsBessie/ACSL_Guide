function convertExpression() {
            var expr = document.getElementById("expression").value;
            var inputType = document.getElementById("inputType").value;
            var outputType = document.getElementById("outputType").value;

            let data = {
                'expression':expr,
                'inputType': inputType,
                'outputType': outputType,
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
                document.getElementById("output").innerText = responseData['output'];
                // Handle the response as needed
            })
            .catch(error => {
                console.error('Error:', error);
                // Handle any errors
            });
            // Add more conditions and functions for different conversions


}