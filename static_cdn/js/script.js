window.addEventListener('DOMContentLoaded', ()=>{
    // const loader = document.querySelector('#loader');
    // setTimeout(function(){
    //     loader.classList.add('ops0');
    //     setTimeout(()=>{
    //         loader.classList.add('none')
    //     }, 1000)
        
    // }, 1000)

    const menuButton = document.querySelector('#menu-bar'),
    navigation = document.querySelector('.navigation'),
    navigationMenu = document.querySelector('.navigation-menu');

    menuButton.addEventListener('click', function(){
        navigation.classList.toggle('mobile');
        navigationMenu.classList.toggle('opacity');
    })

    const prew = document.querySelector('#prew'),
    next = document.querySelector('#next'),
    carusel = document.querySelector('.carusel'),
    spacer = document.querySelectorAll('.spacer'),
    caruselItemMover = document.querySelector('.carusel-items'),
    caruselItems = document.querySelectorAll('.carusel-item'),
    caruselController = document.querySelector('.carusel-controller'),
    caruselControllerItem = [];

    let index = 0, n=0, offset = 0, width = getComputedStyle(carusel).width;

    for (let i=0; i<spacer.length; i++) {
        spacer[i].classList.remove('spacer');
        spacer[i].classList.add(`spacer${i%3}`);
        n++;
    }
    caruselItemMover.style.width = 100 * caruselItems.length +"%";

    for (i = 0; i < caruselItems.length; i++) {
        caruselControllerItem.push(document.createElement('span'))
        caruselControllerItem[i].classList.add('carusel-controller_item')
        caruselControllerItem[i].setAttribute('data-slide-to', i)
        caruselController.append(caruselControllerItem[i])
    }

    
}) 
