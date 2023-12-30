const burgerButton = document.getElementById('burger')
const bodyBlock = document.querySelector('body')
const hiddenNavigation = document.getElementById('navigation')

burgerButton.addEventListener('click', () => {
    if (hiddenNavigation.classList.contains('block')) {
        hiddenNavigation.classList.remove('block')
        bodyBlock.style.overflow = ''
    } else {
        hiddenNavigation.classList.add('block')
        bodyBlock.style.overflow = 'hidden'
    }
})