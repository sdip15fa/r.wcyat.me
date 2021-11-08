function getvar(variable) {
    let query = window.location.search.substring(1);
    let vars = query.split("&");
    for (let i = 0; i < vars.length; i++) {
        let pair = vars[i].split("=");
        if (pair[0] === variable) {
            return pair[1];
        }
    }
    let notfound = document.createElement("p");
    notfound.innerHTML = "No URL provided.";
    document.body.insertBefore(notfound, document.body.firstChild);
    return false;
}

if (getvar("link")) {
    window.location.href = getvar("link");
}