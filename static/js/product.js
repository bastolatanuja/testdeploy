let searchForm = document.querySelector('.search-form');

document.querySelector('#search-btn').onclick = () =>{
  searchForm.classList.toggle('active');
  navbar.classList.remove('active');
}

let navbar = document.querySelector('.navbar');

document.querySelector('#menu-btn').onclick = () =>{
  navbar.classList.toggle('active');
  searchForm.classList.remove('active');
}

window.onscroll = () =>{
  searchForm.classList.remove('active');
  navbar.classList.remove('active');
}


document.querySelectorAll('.small-img-1').forEach(image =>{
    image.addEventListener('click', () =>{
        var src = image.getAttribute('src');
        document.querySelector('.big-img-1').src = src;
    });
});

document.querySelectorAll('.small-img-2').forEach(image =>{
    image.addEventListener('click', () =>{
        var src = image.getAttribute('src');
        document.querySelector('.big-img-2').src = src;
    });
});

document.querySelectorAll('.small-img-3').forEach(image =>{
    image.addEventListener('click', () =>{
        var src = image.getAttribute('src');
        document.querySelector('.big-img-3').src = src;
    });
});

document.querySelectorAll('.small-img-4').forEach(image =>{
    image.addEventListener('click', () =>{
        var src = image.getAttribute('src');
        document.querySelector('.big-img-4').src = src;
    });
});

