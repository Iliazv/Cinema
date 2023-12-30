const hall = document.querySelector('.hall')
const shade = document.querySelector('.shade')
const closeHall = document.querySelector('.hall__close')

let hallInner = document.querySelector('.hall__inner')

function openHall(pk) {
    hall.classList.add('block')
    shade.classList.add('block')
}

[shade, closeHall].forEach(function(element) {
    element.addEventListener("click", () => {
        hall.classList.remove('block')
        shade.classList.remove('block')
    });
});