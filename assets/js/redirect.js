function getvar(variable) {
  let query = window.location.search.substring(1);
  let vars = query.split("&");
  for (i of vars) {
    let pair = i.split("=");
    if (pair[0] === variable) {
      const regexp = new RegExp(
        "^(https?:\\/\\/)?" + // protocol
          "((([a-z\\d]([a-z\\d-]*[a-z\\d])*)\\.)+[a-z]{2,}|" + // domain name
          "((\\d{1,3}\\.){3}\\d{1,3}))" + // OR ip (v4) address
          "(\\:\\d+)?(\\/[-a-z\\d%_.~+]*)*" + // port and path
          "(\\?[;&a-z\\d%_.~+=-]*)?" + // query string
          "(\\#[-a-z\\d_]*)?$",
        "i"
      ); // fragment locator
      if (regexp.test(pair[1])) {
        return pair[1];
      }
      let invalid = document.createElement("p");
      invalid.innerHTML = "Invalid URL.";
      document.body.insertBefore(invalid, document.body.firstChild);
      return false;
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
