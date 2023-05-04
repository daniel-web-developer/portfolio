const menuAction = document.querySelector('#menuid');
const overAnimation = document.querySelector('#over');
const overMenu = document.querySelector('#menuMobile');
const buttons = document.querySelectorAll("[data-button]");

menuAction.addEventListener('click', () => {
    if(menuAction.classList.contains('open')){
        menuAction.classList.remove('open');
    }
    else{
        menuAction.classList.add('open');
    }
    if(overAnimation.classList.contains('overlay-span-activate')){
        overAnimation.classList.remove('overlay-span-activate');
    }
    else{
        overAnimation.classList.add('overlay-span-activate');
    }
    if(overMenu.classList.contains('menu-mobile-span-activate')){
        overMenu.classList.remove('menu-mobile-span-activate');
    }
    else{
        overMenu.classList.add('menu-mobile-span-activate');
    }
});

buttons.forEach(button => {
    button.addEventListener('click', () => {

        let slideChange = 0

        if(button.dataset.carouselButton === "next"){
            slideChange = 1;
        }
        else{
            slideChange = -1;
        }
        
        const slides = button.closest("[data-carousel]").querySelector("[data-slides]")

        const currentSlide = slides.querySelector("[data-active]");
        
        let newSlide = [...slides.children].indexOf(currentSlide) + slideChange;

        if(newSlide >= slides.children.length){
            newSlide = 0;
        }

        if(newSlide < 0){
            newSlide = slides.children.length - 1;
        }

        slides.children[newSlide].dataset.active = true;
        delete currentSlide.dataset.active

    })
})