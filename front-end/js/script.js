let visitorCount = localStorage.getItem("visitors");

if (visitorCount === null) localStorage.setItem("visitors", 0);

window.addEventListener("load", () => {
  localStorage.setItem("visitors", visitorCount++);
  console.log(visitorCount);
});
