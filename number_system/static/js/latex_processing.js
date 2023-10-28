var latexInput = document.getElementById('latex-input');
var latexOutput = document.getElementById('latex-output');

latexInput.addEventListener('input', function() {
    var latexExpression = latexInput.value;
    if(latexExpression === ""){
        latexOutput.innerHTML = ""
    }else{
        latexOutput.innerHTML = "Your Expression: \\("+ latexExpression + "\\)"
        MathJax.typeset([latexOutput]);
    }

});
