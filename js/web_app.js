/**
 * Документация для JavaScript-файла web_app.js
 */
// let WebApp = window.Telegram.WebApp;

// WebApp.expand();

// WebApp.showAlert()

document.addEventListener("DOMContentLoaded", function() {
    const main = document.querySelector('main');
    const aboutGardenBtn = document.getElementById('aboutGardenBtn');
    const tasksBtn = document.getElementById('tasksBtn');
    const payBtn = document.getElementById('payBtn');
    const aboutUsBtn = document.getElementById('aboutUsBtn');

    /**
    * Функция для отображения информации о саде.
    * Очищает основной контент и добавляет информацию о саде.
    */

    function showAboutGarden() {
        main.innerHTML = '';
  
  		const buildContainer = document.createElement('div');
  		buildContainer.innerHTML = `
    	<p>Уральский сад лечебных культур им.проф. Л.И. Вигорова - это ботанический сад УГЛТУ с уникальной коллекцией древесных растений, накапливающих в различных органах биологически активные вещества (БАВ) в эффективных колличествах. Сад был заложен в 1950 году профессором Леонидом Ивановичем Вигоровым.</p>
    	<br>
    	<p>Ботанический сад открыт для экскурсий по предварительной записи</p>
    	<br>
    	<p>Адрес: г. Екатеринбург, Сибирский тракт, 35Б</p>
  		`;

  		main.appendChild(buildContainer);
    }


    /**
    * Функция для отображения заданий.
    * Очищает основной контент и подготавливает контейнер для заданий.
    */

    function showTasks() {
        main.innerHTML = '';
  
  		const buildContainer = document.createElement('div');
  		buildContainer.innerHTML = `
    	
  		`;

  		main.appendChild(buildContainer);
    }

    /**
    * Функция для отображения информации о платежах.
    * Очищает основной контент и подготавливает контейнер для информации о платежах.
    */

    function showPay() {
        main.innerHTML = '';
  
  		const buildContainer = document.createElement('div');
  		buildContainer.innerHTML = `
    	
  		`;

  		main.appendChild(buildContainer);
    }

    /**
    * Функция для отображения информации о компании.
    * Очищает основной контент и добавляет информацию о компании NFTree.
    */

    function showAboutUs() {
        main.innerHTML = '';
  
  		const buildContainer = document.createElement('div');
  		buildContainer.innerHTML = `
   	 	<h2>NFTree</h2>
    	<p>@NFTree</p>
    	<p>NFTree@yandex.ru</p>
  		`;
  
  		main.appendChild(buildContainer);
    }

    aboutGardenBtn.addEventListener('click', showAboutGarden);
    tasksBtn.addEventListener('click', showTasks);
    payBtn.addEventListener('click', showPay);
    aboutUsBtn.addEventListener('click', showAboutUs);

    // Функция для обновления счетчика и прогресса
    var counter = 0;

    /**
    * Функция для обновления счетчика и прогресса.
    * Увеличивает счетчик на 1, обновляет значение счетчика и прогресс-бар.
    */

    function updateCounter() {
        counter++;
        document.getElementById('count').textContent = counter;
        updateProgressBar();
    }

    // Функция для сброса счетчика и прогресса

    /**
    * Функция для сброса счетчика и прогресса.
    * Сбрасывает счетчик на 0, обновляет значение счетчика и прогресс-бар.
    */

    function resetCounter() {
        counter = 0;
        document.getElementById('count').textContent = counter;
        updateProgressBar();
    }

    // Функция для обновления прогресса

    /**
    * Функция для обновления прогресса.
    * Вычисляет и обновляет значение прогресса и его отображение.
    */

    function updateProgressBar() {
        var progress = (counter / 1000) * 100;
        document.getElementById('progress').style.width = progress + '%';
        document.getElementById('progress').textContent = progress.toFixed(1) + '%';
        if (progress >= 100) {
            document.getElementById('progress').style.backgroundColor = 'red';
        }
    }

    // Добавляем обработчик события клика для изображения дерева
    document.getElementById('tree-image').addEventListener('click', function() {
        updateCounter();
    });

    // Добавляем обработчик события клика для сброса счетчика
    document.getElementById('progress').addEventListener('click', resetCounter);
});