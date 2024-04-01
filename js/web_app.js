// let WebApp = window.Telegram.WebApp;

// WebApp.expand();

// WebApp.showAlert()

document.addEventListener("DOMContentLoaded", function() {
    const main = document.querySelector('main');
    const aboutGardenBtn = document.getElementById('aboutGardenBtn');
    const tasksBtn = document.getElementById('tasksBtn');
    const payBtn = document.getElementById('payBtn');
    const aboutUsBtn = document.getElementById('aboutUsBtn');

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

    function showTasks() {
        main.innerHTML = '';
  
  		const buildContainer = document.createElement('div');
  		buildContainer.innerHTML = `
    	
  		`;

  		main.appendChild(buildContainer);
    }

    function showPay() {
        main.innerHTML = '';
  
  		const buildContainer = document.createElement('div');
  		buildContainer.innerHTML = `
    	
  		`;

  		main.appendChild(buildContainer);
    }

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

    function updateCounter() {
        counter++;
        document.getElementById('count').textContent = counter;
        updateProgressBar();
    }

    // Функция для сброса счетчика и прогресса
    function resetCounter() {
        counter = 0;
        document.getElementById('count').textContent = counter;
        updateProgressBar();
    }

    // Функция для обновления прогресса
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