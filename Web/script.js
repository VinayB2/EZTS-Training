var audio = new Audio('click3.mp3');
var view = document.body
document.addEventListener("keydown", () => {
    var randomColor = '#' + Math.floor(Math.random() * 16777215).toString(16).padStart(6, '0');
    view.style.backgroundColor = randomColor;
    audio.pause();
    audio.currentTime = 0;
    audio.play();
});
