let choices = document.getElementById('typeChoices');
choices.addEventListener('change', function () {
    const selectedChoice = choices.value;
    window.location.replace(`/question_generator/${selectedChoice}`);
});
