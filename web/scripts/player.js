
function play(path) {
    const audio = new Audio(path);
    audio.load();
    audio.play();
}