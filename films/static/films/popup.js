const buttonOpen = document.querySelector('.head__login_btn')
const popup = document.querySelector('.popup')
const background = document.querySelector('.background')
const closeButton1 = document.querySelector('.popup__close_1')
const closeButton2 = document.querySelector('.popup__close_2')
const popupRegister = document.querySelector('.popup-2')
const registerLink = document.getElementById('popup-register')
const loginLink = document.getElementById('popup-login')

buttonOpen.addEventListener('click', () => {
    popup.classList.add('block')
    background.classList.add('block')
})

closeButton1.addEventListener('click', () => {
    popup.classList.remove('block')
    popupRegister.classList.remove('block')
    background.classList.remove('block')
})

closeButton2.addEventListener('click', () => {
    popup.classList.remove('block')
    popupRegister.classList.remove('block')
    background.classList.remove('block')
})

background.addEventListener('click', () => {
    popup.classList.remove('block')
    popupRegister.classList.remove('block')
    background.classList.remove('block')
})

registerLink.addEventListener('click', () => {
    popup.classList.remove('block')
    popupRegister.classList.add('block')
})

loginLink.addEventListener('click', () => {
    popup.classList.add('block')
    popupRegister.classList.remove('block')
})

function showPassword(id) {
    let passwordField = document.getElementById('password-' + String(id))
    let band = document.getElementById('eye-' + String(id))
    if (passwordField.type == 'password') {
        passwordField.type = 'text'
        band.style.display = 'block'
    } else {
        passwordField.type = 'password'
        band.style.display = 'none'
    }
}