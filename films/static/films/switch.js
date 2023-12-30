const pictureCollection = [...document.querySelector('.main__video').children]
const selectorCollection = [...document.querySelector('.main__switch').children]
const moduleCollection = [...document.querySelector('.main__description').children]

let overlay = document.querySelector('.overlay')

const filmButton = document.getElementById('film-button')
const libraryButton = document.getElementById('library-button')
const filmSection = document.querySelector('.main__films')
const librarySection = document.querySelector('.main__library')

selectorCollection.forEach(element => {
    element.addEventListener('click', () => {
        selectorCollection.forEach(stripe => {
            stripe.classList.remove('visited')
        });
        let index = Number(String(element.id).slice(-1)) - 1
        openPicture(pictureCollection, index)
        openModule(moduleCollection, index)
        element.classList.add('visited')
    })
});

pictureCollection.forEach(picture => {
    picture.addEventListener('click', () => {
        let pictureString = picture.classList[0]
        let id = pictureString[pictureString.length - 1]
        let modal = document.getElementById('modal-' + String(id))
        let closeButton = document.getElementById('close-' + String(id))
        // modal = document.getElementById('modal-' + String(id))
        // console.log(modal)
        modal.style.display = 'block'
        overlay.classList.add('slip')

        overlay.addEventListener('click', () => {
            modal.style.display = 'none'
            overlay.classList.remove('slip')
        })

        closeButton.addEventListener('click', () => {
            modal.style.display = 'none'
            overlay.classList.remove('slip')
        })
    })    
});

function openPicture(array, index) {
    const defaultPicture = array[0]
    defaultPicture.classList.remove('showed-default')
    array.forEach(element => {
        element.classList.remove('showed')
        console.log(element)
    });
    let picture = pictureCollection[Number(index)]
    picture.classList.add('showed')
}

function openModule(array, index) {
    const defaultModule = array[0]
    defaultModule.classList.remove('mobule-active-default')
    array.forEach(element => {
        element.classList.remove('mobule-active')
    });
    let module = moduleCollection[Number(index)]
    module.classList.add('mobule-active')
}

filmButton.addEventListener('click', () => {
    filmSection.classList.add('activated')
    librarySection.classList.remove('activated')
    filmButton.classList.add('active')
    libraryButton.classList.remove('active')
})

libraryButton.addEventListener('click', () => {
    
    filmSection.classList.remove('activated')
    librarySection.classList.add('activated')
    libraryButton.classList.add('active')
    filmButton.classList.remove('active')
})