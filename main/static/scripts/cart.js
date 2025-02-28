// $(".cross").on("click", function () {
//   var item = $(this).closest(".cart__item");
//   item.addClass("removing");
//   setTimeout(function () {
//     item.remove();
//   }, 300); // Удалить элемент после завершения анимации (в миллисекундах)
// });

$(".cross").on("click", function () {
  var item = $(this).closest(".cart__item");
  var container = $(".cart__list");

  var marginBetweenItems = 10;

  item.animate(
    {
      opacity: 0,
      marginBottom: 0,
      height: 0,
    },
    300,
    function () {
      item.remove();

      var items = container.children(".cart__item:visible");

      var currentTop = 0;

      items.each(function (index, element) {
        var $element = $(element);

        $element.css("margin-bottom", marginBetweenItems + "px");

        currentTop += $element.outerHeight(true) + marginBetweenItems;
      });

      container.animate({ height: currentTop - marginBetweenItems }, 300);
    }
  );
});

