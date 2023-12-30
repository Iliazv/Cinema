const accountButton = document.querySelector('.head__user')
const accountBlock = document.querySelector('.head__account')


accountButton.addEventListener('click', () => {
    if (!accountBlock.classList.contains('block')) {
        accountBlock.classList.add('block')
    } else {
        accountBlock.classList.remove('block')
    }
})