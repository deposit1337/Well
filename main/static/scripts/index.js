$(document).ready(function () {
    var searchForm = $(".search-form");
    var searchIcon = $("#search-icon");
    var findButton = $(".find-btn");

    // Обработка клика вне формы
    $(document).on("click", function (event) {
        if (!searchForm.is(event.target) && searchForm.has(event.target).length === 0) {
            if (searchForm.hasClass("expanded")) {
                closeSearchForm();
            }
        }
    });

    // Обработка клика по иконке поиска
    searchIcon.click(function () {
        if (searchForm.hasClass("expanded")) {
            closeSearchForm();
        } else {
            openSearchForm();
        }
    });

    // Функция для открытия формы поиска
    function openSearchForm() {
        searchIcon.hide();
        searchForm.removeClass("hidden").css({ width: 0, visibility: "visible" });

        // Проверка ширины окна
        var newWidth = $(window).width() < 1200 ? 120 : 300; // Устанавливаем ширину в зависимости от ширины окна

        searchForm.animate({ width: newWidth, opacity: 1 }, 300, function () {
            findButton.css("opacity", 1);
            searchForm.addClass("expanded");
            findButton.addClass("test");
        });
    }

    // Функция для закрытия формы поиска
    function closeSearchForm() {
        searchForm.animate({ width: 0, opacity: 0 }, 300, function () {
            searchForm.removeClass("expanded").addClass("hidden").css({ width: "100%", visibility: "hidden" });
            findButton.css("opacity", 0);
            searchIcon.fadeIn(100);
        });
    }
});