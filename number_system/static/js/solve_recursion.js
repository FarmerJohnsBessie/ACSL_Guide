const equationInputs = document.querySelectorAll('input[name="equation"]');
const conditionInputs = document.querySelectorAll('input[name="condition"]');
// handleInputChange(); // Call the function once to initialize the LaTeX string
// Add event listeners to detect changes in equation and condition inputs
equationInputs.forEach(input => {
    input.addEventListener('input', handleInputChange);
});

conditionInputs.forEach(input => {
    input.addEventListener('input', handleInputChange);
});

let numEquations = 1;
document.getElementById("addEquation").addEventListener("click", function () {
    const equationsDiv = document.getElementById("equations");
    const newEquation = document.querySelector(".equation").cloneNode(true);
    const equations = newEquation.querySelectorAll('input');
    equations.forEach(input => {
        input.value = "";
    });
    equationsDiv.appendChild(newEquation);
    const equationInputs = document.querySelectorAll('input[name="equation"]');
    const conditionInputs = document.querySelectorAll('input[name="condition"]');

    // Add event listeners to detect changes in equation and condition inputs
    equationInputs.forEach(input => {
        input.addEventListener('input', handleInputChange);
    });

    conditionInputs.forEach(input => {
        input.addEventListener('input', handleInputChange);
    });
    numEquations++;
});
document.getElementById("removeEquation").addEventListener("click", function () {
    if(numEquations>1) {
        const equationsDiv = document.getElementById("equations");
        equationsDiv.removeChild(equationsDiv.lastChild);
        numEquations--;
    }
});

let numVariables = 1;
document.getElementById("addVariable").addEventListener("click", function () {
    if(numVariables<2) {
        const variablesDiv = document.getElementById("variables");
        const newVariable = document.querySelector(".variable").cloneNode(true);
        // change the variable name to y
        newVariable.querySelector("label").innerHTML = "y = ";
        variablesDiv.appendChild(newVariable);

        //change the function label to f(x,y)
        const functionLabel = document.getElementById("function-label");
        functionLabel.innerHTML = "Calculate f(x,y)";

        numVariables++;
    }
});

document.getElementById("removeVariable").addEventListener("click", function () {
    if(numVariables>1) {
        const variablesDiv = document.getElementById("variables");
        variablesDiv.removeChild(variablesDiv.lastChild);

        //change the function label to f(x)
        const functionLabel = document.getElementById("function-label");
        functionLabel.innerHTML = "Calculate f(x)";

        numVariables--;
    }
});

document.getElementById("recursiveForm").addEventListener("submit", function (e) {
    e.preventDefault();

    const formData = new FormData(this);
    const equations = formData.getAll("equation");
    const conditions = formData.getAll("condition");
    const value = formData.getAll("value");

    const resultDiv = document.getElementById("result");
    resultDiv.innerHTML = "Result: ";
    // Convert equations and conditions into JSON
    let json_data = {
        equations: [],
        conditions: [],
        value: [],
    };
    for (let i = 0; i < equations.length; i++) {
        json_data.equations.push(equations[i]);
        json_data.conditions.push(conditions[i]);
    }
    for (let i = 0; i < value.length; i++) {
        json_data.value.push(value[i]);
    }
    json_data = JSON.stringify(json_data);
    fetch('/solve/recursion/', {
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
        resultDiv.innerHTML += responseData.result;
        // Handle the response as needed
    })
    .catch(error => {
        console.error('Error:', error);
        // Handle any errors
    });
});

// Define the change detection function
function handleInputChange() {
    const form = document.getElementById("recursiveForm");

    // Create a new FormData object and pass the form element as an argument
    const formData = new FormData(form);

    const equations = formData.getAll("equation");
    const conditions = formData.getAll("condition");

    // Initialize the LaTeX string with the opening part
    let piecewiseContent = "\\[f(x) = \\begin{cases}";

    for (let i = 0; i < equations.length; i++) {
        // if(equations[i] === "" || conditions[i] === ""){
        //     continue;
        // }
        // Add the LaTeX for each equation and condition
        piecewiseContent += equations[i] + " & \\text{if } " + conditions[i];

        // Add a newline character after each condition except the last one
        if (i < equations.length - 1) {
            piecewiseContent += "\\\\";
        }
    }

    // Add the closing part
    const finalLatex = piecewiseContent + "\\end{cases}\\]";
    const latex_area = document.getElementById("latex-area");
    latex_area.innerHTML = finalLatex;
    MathJax.typeset([latex_area]);
}