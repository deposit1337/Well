const firstElement = document.getElementById("trigger-element");
const secondElement = document.getElementById("change-element");
const thirdElement = document.getElementById("element-replacement");

function checkWidthAndAddEvents() {
  if (window.innerWidth >= 1440) {
    firstElement.addEventListener("mouseover", function () {
      secondElement.classList.add("not");
      thirdElement.classList.remove("not");
      thirdElement.classList.remove("none");
    });

    firstElement.addEventListener("mouseout", function () {
      firstElement.classList.remove("not");
      thirdElement.classList.add("not");
      secondElement.classList.remove("not");
    });
  }
}

// Проверка ширины при загрузке страницы
checkWidthAndAddEvents();

// Проверка ширины при изменении размера окна
window.addEventListener("resize", checkWidthAndAddEvents);
