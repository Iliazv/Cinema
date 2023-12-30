const filmPreview = document.querySelector('.film__preview')
const modalPreview = document.getElementById('modal-preview')
const modalPicture = document.getElementById('modal-picture')

let overlay = document.querySelector('.overlay')
const crossButton1 = document.getElementById('close-button1')
const crossButton2 = document.getElementById('close-button2')
const renderedPart = document.querySelectorAll('.film__thumb')
const previewImage = document.getElementById('preview')

const leftArrow = document.querySelector('.left')
const rightArrow = document.querySelector('.right')
const mainPicture = document.querySelector('.film__picture')
const player = document.querySelector('.main__player')
const innerImage = document.querySelector('.main__inner')

const allImages = [...renderedPart]
let renderedImages = allImages.slice(0, 3)
let leftImage = 0
let rightImage = 2
renderImage(allImages, renderedImages)

filmPreview.addEventListener('click', () => {
    let playerStyle = player.style.display
    console.log(playerStyle)
    if (playerStyle != 'none') {
        modalPreview.style.display = 'block'
        overlay.classList.add('slip')

        overlay.addEventListener('click', () => {
            modalPreview.style.display = 'none'
            overlay.classList.remove('slip')
        })

        crossButton1.addEventListener('click', () => {
            modalPreview.style.display = 'none'
            overlay.classList.remove('slip')
        })
    } else {
        let newSrc = mainPicture.src
        innerImage.src = newSrc
        modalPicture.style.display = 'block'
        overlay.classList.add('slip')

        overlay.addEventListener('click', () => {
            modalPicture.style.display = 'none'
            overlay.classList.remove('slip')
        })

        crossButton2.addEventListener('click', () => {
            modalPicture.style.display = 'none'
            overlay.classList.remove('slip')
        })
    }
})

rightArrow.addEventListener('click', rightShiftImages, false);
rightArrow.allImages = allImages
rightArrow.renderedImages = renderedImages
rightArrow.rightArrow = rightArrow
rightArrow.leftArrow = leftArrow

leftArrow.addEventListener('click', leftShiftImages, false);
leftArrow.allImages = allImages
leftArrow.renderedImages = renderedImages
leftArrow.rightArrow = rightArrow
leftArrow.leftArrow = leftArrow

function rightShiftImages(event) {
    console.log(allImages)
    if (rightImage == allImages.length - 1 || allImages.length <= 3) {
        return
    }
    renderedImages.shift()
    leftImage += 1
    rightImage += 1
    let newImage = allImages[rightImage]
    renderedImages.push(newImage)
    renderImage(allImages, renderedImages)
}

function leftShiftImages(event) {
    if (leftImage == 0) {
        return
    }
    renderedImages.pop()
    leftImage -= 1
    rightImage -= 1
    let newImage = allImages[leftImage]
    renderedImages.unshift(newImage)
    renderImage(allImages, renderedImages)
}

function renderImage(allImages, renderedImages) {
    allImages.forEach(element => {
        element.style.display = 'none'
    });
    renderedImages.forEach(element => {
        element.style.display = 'block'
    });
}

function selectImage(id) {
    if (id == 'preview') {
        player.style.display = 'block'
    } else {
        player.style.display = 'none'
    }
    let clickedImage = document.getElementById(id)
    mainPicture.src = clickedImage.src
}