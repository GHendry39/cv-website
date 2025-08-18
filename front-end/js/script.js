// let visitorCount = +localStorage.getItem("visitors");
// localStorage.setItem("visitors", (visitorCount += 1));

// // Update visitor counter
// const counterEl = document.getElementById("counter");
// counterEl.innerText = visitorCount;

// Define the API endpoint.
const API_ENDPOINT =
  "https://90j8tk09la.execute-api.eu-west-2.amazonaws.com/dev";

// Get references to our HTML element
const counterEl = document.getElementById("counter");

//Initialise visitor counter
const visitorCount = +counterEl.textContent;
console.log(visitorCount);

//EventListener for window load event
window.addEventListener("load", handleLoad);

async function handleLoad() {
  const browserCount = visitorCount + 1;
  console.log(browserCount);
  response = await fetch(API_ENDPOINT, {
    method: "POST", // We are sending data, so it's a POST request.
    headers: {
      "content-type": "application/json",
    },
    body: JSON.stringify({ browserCount: browserCount }), // Convert our JavaScript object to a JSON string.
  });
  console.log(response.json());

  const newCount = response.result.message;
  console.log(newCount);
}
