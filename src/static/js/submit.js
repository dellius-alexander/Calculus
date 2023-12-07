
function submit() {
    let form = document.getElementById("form");
    console.dir(form);
    let data = new FormData(form);
    console.dir(data);
    let xhr = new XMLHttpRequest();
    xhr.open("POST", "/api/submit", true);
    xhr.onload = function () {
        let response = JSON.parse(this.responseText);
        if (response.status == "success") {
            alert("Submitted successfully");
        } else {
            alert("Error: " + response.message);
        }
    };
    xhr.send(data);
}


/**
 * The function is a variation of submit function, but it uses
 * XMLHttpRequest Level 2 FormData API to send the form data and
 * redirect the server response to the results.html page.
 */
function api_submit(event, method = "POST", url = "/submit") {
    try {
        event.preventDefault();
        let form = document.getElementById("form");
        console.dir(form);
        let data = new FormData(form);
        console.dir(data);
        let xhr = new XMLHttpRequest();
        xhr.open(method, url, true);
        xhr.onload = function () {
            let response = JSON.parse(this.responseText);
            if (response.status === "success") {
                window.location.href = "/results.html";
            } else {
                alert("Error: " + response.message);
            }
        };
        xhr.send(data);
    } catch (error) {
        console.error(error);
    }
}