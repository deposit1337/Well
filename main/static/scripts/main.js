document.addEventListener("click", function (event) {
  if (
    event.target.tagName === "A" &&
    event.target.getAttribute("href").startsWith("#")
  ) {
    event.preventDefault();

    var targetId = event.target.getAttribute("href").slice(1);
    var targetElement = document.getElementById(targetId);

    if (targetElement) {
      var offsetTop = targetElement.offsetTop;

      window.scrollTo({
        top: offsetTop,
        behavior: "smooth",
      });
    }
  }
});

