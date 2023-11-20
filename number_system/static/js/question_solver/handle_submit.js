var uploadedFile = null; // Store the uploaded file object

function normalizeNewlines(str) {
    return str.replace(/\n+/g, '\n');
}

document.getElementById('send-btn').addEventListener('click', function() {
    document.getElementById('user-input').style.height = 'auto'; // Reset the height
    var userInput = document.getElementById('user-input');
    var messageToSend = normalizeNewlines(userInput.value.trim());
    if (messageToSend !== '' || uploadedFile) {
        addMessage(messageToSend, 'user-message');
        if (uploadedFile) {
            addFileToMessage(uploadedFile.name);
            // Replace with the code to send the message and the file to the backend
            sendFileToServer(uploadedFile); // Dummy function to simulate file send
            uploadedFile = null; // Clear the stored file after sending

            // Clear the uploaded files display area
            var uploadedFilesDiv = document.getElementById('uploaded-files');
            uploadedFilesDiv.innerHTML = '';
        }
        // Replace this with the code to send the message to the AI and get the response
        getAIResponse(messageToSend); // Dummy function for actual AI call
        userInput.value = ''; // Clear the input after sending
    }
});

document.getElementById('upload-btn').addEventListener('click', function() {
    document.getElementById('file-input').click(); // Trigger file input click
});

document.getElementById('file-input').addEventListener('change', function(event) {
    var files = event.target.files;
    if (files.length > 0) {
        uploadedFile = files[0]; // Store the file object
        displayUploadedFile(uploadedFile);
    }
});

function addMessage(message, className) {
    var chatHistory = document.getElementById('chat-history');
    var messageDiv = document.createElement('div');
    messageDiv.textContent = message;
    messageDiv.className = 'message ' + className;
    chatHistory.appendChild(messageDiv);
    chatHistory.scrollTop = chatHistory.scrollHeight; // Scroll to latest message
}

function addFileToMessage(filename) {
    var chatHistory = document.getElementById('chat-history');
    var fileDiv = document.createElement('div');
    fileDiv.textContent = "File sent: " + filename;
    fileDiv.className = 'message file-message';
    chatHistory.appendChild(fileDiv);
}

function displayUploadedFile(file) {
    var uploadedFilesDiv = document.getElementById('uploaded-files');
    uploadedFilesDiv.innerHTML = ''; // Clear previous files (if any)
    var fileItem = document.createElement('div');
    fileItem.className = 'file-item';
    fileItem.textContent = "Ready to send: " + file.name;
    uploadedFilesDiv.appendChild(fileItem);
}

function getAIResponse(message) {
    // Dummy response for the sake of this example
    var response = "This is a simulated response to: " + message;
    setTimeout(function() { // Simulate asynchronous network call
        addMessage(response, 'ai-response');
    }, 1000);
}

function sendFileToServer(file) {
    // Dummy function to simulate file send to server
    console.log("File sent to server: ", file.name);
    // Actual implementation would involve using FormData and an AJAX request or fetch API
}

var userInput = document.getElementById('user-input');

// Automatically adjust textarea height
userInput.addEventListener('input', function() {
    this.style.height = 'auto'; // Reset the height
    var maxHeight = 200; // Set the maximum expandable height
    this.style.height = (this.scrollHeight > maxHeight ? maxHeight : this.scrollHeight) + 'px';
});