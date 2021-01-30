function displayState(boolean) {
    let bloco = document.getElementById("resultado")

    if(!boolean) {
        bloco.style.display = "none"
    } else {
        bloco.style.display = "block"
    }
}