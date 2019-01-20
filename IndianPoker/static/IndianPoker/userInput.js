function buttonUpdate() {

    var inputText = document.getElementById('raiseValue').value;
    var inputTextNumber = parseInt(inputText, 10);
    if (inputText == '')
    {
        document.getElementById("callOrRaise").innerHTML = "Call";
        inputTextNumber = 0;
    }
    else
    {
        if (inputTextNumber < 0) {
            document.getElementById("callOrRaise").innerHTML = "Call";
            inputTextNumber = 0;
        }
        if (inputTextNumber > 0) {
            document.getElementById("callOrRaise").innerHTML = "Raise";
        }
        else {
            document.getElementById("callOrRaise").innerHTML = "Call";
            inputTextNumber = 0;
        }
        document.getElementById("raiseValue").value = inputTextNumber;
    }
    document.getElementById("callOrRaise").value = inputTextNumber;
    

}
function fold() {
    // SEND SERVER FOLD COMMAND
}
function callOrRaise() {
    inputTextNumber = readInputText();
    // SEND SERVER CALL OR RAISE INFORMATION
}
function readInputText() {
    var inputText = document.getElementById('raiseValue').value;
    var inputTextNumber = parseInt(inputText, 10);
    return inputTextNumber;
}