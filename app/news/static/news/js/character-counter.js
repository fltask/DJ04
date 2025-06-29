document.addEventListener('DOMContentLoaded', function () {
    // Получаем элементы формы
    const titleInput = document.querySelector('#id_title');
    const descriptionInput = document.querySelector('#id_short_description');
    const titleCount = document.querySelector('#title-count');
    const descriptionCount = document.querySelector('#description-count');

    // Функция обновления счетчика
    function updateCount(input, counter, maxLength) {
        if (!input || !counter) return;

        const currentLength = input.value.length;
        counter.textContent = currentLength;

        // Изменяем цвет в зависимости от количества символов
        if (currentLength > maxLength * 0.9) {
            counter.style.color = '#dc3545'; // красный цвет
        } else if (currentLength > maxLength * 0.7) {
            counter.style.color = '#ffc107'; // желтый цвет
        } else {
            counter.style.color = '#6c757d'; // серый цвет
        }
    }

    // Обработчик для поля заголовка
    if (titleInput && titleCount) {
        titleInput.addEventListener('input', function () {
            updateCount(this, titleCount, window.titleMaxLength || 100);
        });
        // Инициализация при загрузке
        updateCount(titleInput, titleCount, window.titleMaxLength || 100);
    }

    // Обработчик для поля описания
    if (descriptionInput && descriptionCount) {
        descriptionInput.addEventListener('input', function () {
            updateCount(this, descriptionCount, window.descriptionMaxLength || 200);
        });
        // Инициализация при загрузке
        updateCount(descriptionInput, descriptionCount, window.descriptionMaxLength || 200);
    }
});
