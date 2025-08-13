let visitorCount = +localStorage.getItem("visitors");
localStorage.setItem("visitors", (visitorCount += 1));

// Update visitor counter
const counterEl = document.getElementById("counter");
counterEl.innerText = visitorCount;
