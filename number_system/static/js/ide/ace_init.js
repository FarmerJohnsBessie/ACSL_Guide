const parser = require('../parsers/aal_parser');

var editor;

window.onload = function() {
    editor = ace.edit("editor");
    editor.setTheme("ace/theme/monokai");
};

var language_dropdown_menu = document.getElementById("language");

language_dropdown_menu.addEventListener("change", function (){
    const selected_choice = language_dropdown_menu.value;
    if (selected_choice === 'LISP'){
        editor.session.setMode('ace/mode/lisp');
    }else{
        editor.session.setMode('ace/mode/plain_text');
    }
});

const runCodeButton = document.getElementById("run-code");
runCodeButton.addEventListener("click", function() {
    var code = editor.getSession().getValue();
    console.log(code);
    var url = '/ide/run/'
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({'code': code, 'language': document.getElementById('language').value, 'inputs': document.getElementById('input-area').value})
    })
    .then(response => response.json())
    .then((data) => {
        console.log('Data: ', data.output);

        document.getElementById('output').innerHTML = data.output;
        // $(".output").text(data.output);
    })
});