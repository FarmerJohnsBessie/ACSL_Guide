var latexInput = document.getElementById('latex-input');
var latexOutput = document.getElementById('latex-output');

latexInput.addEventListener('input', updateLatexOutput);

function updateLatexOutput(){
    console.log(123)
    var latexExpression = latexInput.value;
    if(latexExpression === ""){
        latexOutput.innerHTML = ""
    }else{
        latexOutput.innerHTML = "Your Expression: \\("+ latexExpression + "\\)"
        MathJax.typeset([latexOutput]);
    }
}
window.onload(updateLatexOutput);