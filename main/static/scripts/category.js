// function changeColor() {
//   var button = document.querySelector(".add-to-cart-btn");
//   var button = document.querySelector(".add-to-cart-in-item-btn");

//   button.classList.toggle("clicked");
//   button.innerText = "Добавлено";
// }
//
//function changeColor() {
//  var button = document.querySelector(".add-to-cart-in-item-btn");
//  var buttonCategory = document.querySelector(".add-to-cart-btn");
//
//  // var buttonText = button.innerText;
//
//  if (button.classList.contains("clicked")) {
//    button.classList.remove("clicked");
//    button.innerText = "В корзину";
//  } else {
//    button.classList.add("clicked");
//    button.innerText = "Добавлено";
//  }
//}






//
//function changeColorCat(buttonCategory) {
//  if (buttonCategory.classList.contains("clicked")) {
//    buttonCategory.classList.remove("clicked");
//    buttonCategory.innerText = "В корзину";
//  } else {
//    buttonCategory.classList.add("clicked");
//    buttonCategory.innerText = "Добавлено";
//  }
//}
//
//document.addEventListener("DOMContentLoaded", function() {
//  var buttonsCategory = document.querySelectorAll(".add-to-cart-btn");
//
//  buttonsCategory.forEach(function(button) {
//    button.addEventListener("click", function() {
//      changeColorCat(button);
//    });
//  });
//});











// drop list
var dropTrigger = document.getElementById("drop-trigger");
var content = document.querySelector(".content");
var angle = document.querySelector(".down-arrow");
// Обработчик события при нажатии на элемент
dropTrigger.addEventListener("click", function () {
  content.classList.toggle("show");
  angle.classList.toggle("rotate");
});




// drop list item




