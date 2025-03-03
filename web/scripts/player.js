var audioPlayer = null;

function play(path) {
    if (audioPlayer == null) {
        audioPlayer = new Audio(path);
        audioPlayer.load();
    }
    audioPlayer.play();
}