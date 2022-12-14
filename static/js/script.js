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
        caruselControllerItem.push(document.createElement('span'));
        caruselControllerItem[i].classList.add('carusel-controller_item');
        caruselControllerItem[i].setAttribute('data-slide-to', i);
        caruselController.append(caruselControllerItem[i]);
    }
    caruselControllerItem[0].classList.add('active');

    function setController(index){
        offset = -(+width.slice(0, width.length-2)*index)
        caruselItemMover.style.transform = `translateX(${offset}px)`;
        caruselControllerItem[index].classList.add('active');
    }

    next.addEventListener('click', function(){
        caruselItemMover.style.transition = 'all 0.5s linear';
        caruselControllerItem[index].classList.remove('active');
        width = getComputedStyle(caruselItems[index]).width;
        if (index == caruselItems.length-1){
            index = 0;
        }
        else{
            index += 1;
        }
        setController(index);
    })
    prew.addEventListener('click', function(){
        caruselItemMover.style.transition = 'all 0.5s linear';
        caruselControllerItem[index].classList.remove('active');
        width = getComputedStyle(caruselItems[index]).width;
        if (index == 0){
            index = caruselItems.length-1;
        }
        else{
            index -= 1;
        }
        setController(index);
    })
    

    caruselControllerItem.forEach(item => {
        item.addEventListener('click', e => {
            caruselItemMover.style.transition = 'all 0.5s linear';
            const slideTo = e.target.getAttribute('data-slide-to');
            caruselControllerItem[index].classList.remove('active');
            index = +slideTo;
            setController(index);
        })
    })

    const workItems = document.querySelector('.work_items'),
    workItem = document.querySelectorAll('.work_item'),
    workNext = document.querySelector('.work-next'),
    workPrew = document.querySelector('.work-prew');
    let workIndex = 0, workOffset = 0,  workWidth = 0, resize = 2;
    workItems.style.width = (workItem.length * 50)+'%';

    if(+width.slice(0, width.length-2) <= 992){
        responsWork();
    }
    function responsWork(){
        workItems.style.width = (workItem.length * 410)+'px'; 
        resize = 1;
    }

    window.addEventListener('resize', function(){
        width = getComputedStyle(carusel).width;
        caruselItemMover.style.transition = 'none';
        setController(index);
        
        if (+width.slice(0, width.length-2) <= 992){
            responsWork();
        }
        else{
            workItems.style.width = (workItem.length *50)+'%';
            resize = 2;
            if (workIndex == workItem.length-1){
                workIndex = workItem.length - 2;
                setWorkControl(workIndex);
            }
        }
    })
    

    function setWorkControl(workIndex){
        workWidth = getComputedStyle(workItems).width
        workOffset = -(+workWidth.slice(0, workWidth.length-2)/workItem.length*workIndex);
        workItems.style.transform = `translateX(${workOffset}px)`;
    }
    
    workNext.addEventListener('click', function(){
        if (workIndex == workItem.length-resize){
            workIndex = 0;
        }
        else{
            workIndex += 1;
        }
        setWorkControl(workIndex);
    })
    workPrew.addEventListener('click', function(){
        if (workIndex <= 0){
            workIndex = workItem.length-resize;
        }
        else{
            workIndex -= 1;
        }
        setWorkControl(workIndex);
    })

    
}) 
