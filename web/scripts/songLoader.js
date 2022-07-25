
async function loadSongs() {
    var response = await callEndpoint("GET", serverUrl + "/songs/getAll");
    if (response.ERROR == null) {
        let songs = response.SONGS;
        let tbl = document.getElementById("songTable");
        clearTable(tbl);

        for (let i = 0; i < songs.length; i++) {
            addRow(tbl, [
                {"text": songs[i], "attributes": [{"name": "onclick", "value": `play("${serverUrl}/songs/${songs[i]}")`}]}
            ]);
        }
    }
    else {
        alert(response.ERROR);
    }
}