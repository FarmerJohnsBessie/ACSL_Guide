const parser = require('./parsers/aal_parser');

var editor;

window.onload = function() {
    editor = ace.edit("editor");
    editor.setTheme("ace/theme/monokai");
};

const runCodeButton = document.getElementById("run-code");
runCodeButton.addEventListener("click", function() {
    let code = editor.getValue();
    console.log(code);
    const result = parser.parse(code);

    console.log(result);
});