const textField = document.querySelector('.help__text')
const firstQuestion = document.getElementById('input-1')
textField.innerHTML = firstQuestion.value
function openText(key) {
    let clickedButton = document.getElementById(String(key))
    let hiddenField = document.getElementById('input-' + String(key.slice(-1)))

    textField.innerHTML = hiddenField.value
}