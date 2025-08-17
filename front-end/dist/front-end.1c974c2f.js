// let visitorCount = +localStorage.getItem("visitors");
// localStorage.setItem("visitors", (visitorCount += 1));
// // Update visitor counter
// const counterEl = document.getElementById("counter");
// counterEl.innerText = visitorCount;
// Define the API endpoint.
const API_ENDPOINT = "https://ngy5d143vj.execute-api.eu-west-2.amazonaws.com/dev/";
// Get references to our HTML element
const counterEl = document.getElementById("counter");
//Initialise visitor counter
const visitorCount = +counterEl.textContent;
console.log(visitorCount);
//EventListener for window load event
window.addEventListener("load", handleLoad);
function handleLoad() {
    const browserCount = visitorCount + 1;
    console.log(browserCount);
    fetch(API_ENDPOINT, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            browserCount: browserCount
        })
    }).then();
}

//# sourceMappingURL=front-end.1c974c2f.js.map
