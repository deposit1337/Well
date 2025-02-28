var dropTriggerComp = document.getElementById("drop-trigger-comp");
var contentComp = document.querySelector(".content-comp");
var arrow = document.querySelector(".down-arrow");

dropTriggerComp.addEventListener("click", function () {
  contentComp.classList.toggle("show");
  arrow.classList.toggle("rotate");
});

