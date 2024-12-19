document.getElementById('prev').addEventListener('click', () => {
    document.querySelector('.carousel').scrollBy(-1000, 0);
});

document.getElementById('next').addEventListener('click', () => {
    document.querySelector('.carousel').scrollBy(1000, 0);
});
