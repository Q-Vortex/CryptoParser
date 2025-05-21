# CryptoParser
## RU
Привет, эта прога предназначена для того чтобы "тырить" с сайта [TradingView](https://www.tradingview.com) инфу о крипте. 
Эту программу я использовал для своего проекта, ну а если тебе надо, забирай, мне почти не жалко😊  
[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)

Она основана на создание скринов *(это костюмные либо уже готовые сборки для визуализации определённой инфы о крипте)*, и в последствии их использование для культурного заимствования.

## Для начала:
1. Зайди на сайт [TradingView](https://www.tradingview.com)
2. Зарегистрируйся.
3. Настрой свой скрин.
4. Нажми на кнопку *Save*:  
Она находится в левом верхнем углу:    
![image](https://github.com/user-attachments/assets/594ef7f2-2481-426e-9555-5ce653d62b57)
5. Скопируй url сайта.

## Если тебе лень писать уйму команд то просто запусти команду:

```bash
  # Первый скрипт отвечает за скачку а другой запускает прогу.
  ./settup.sh && run.sh
```
Уж прости, тут без команд не обайтимь😅  

## Если тебе всётаки не лень или эта фигня не работает:

```bash
# Если у тебя нет питона то:
sudo apt install python3

# Создаёшь venv и запускаешь его, предварительно зайдя на рут папку проекта:
python3 -m venv venv
source venv/bin/activate
pip install selenium

# Запускаешь прогу
python3 main.py

# Иногда может не работать pip так что просто переташи проект в другую папку на пример в домашнею директорию
cd ..
mv cryptoParser ~/cryptoParser
cd ~
git clone <мой_репозиторий>
```

## Дальше нужно всего лишь настроить прогу:
Это делается очень легко. В папке программы найди **config.json** и следуй параметрам.  
Ну или что будет более правильным, запустить программу и она сома тебе поможет с этим.

## ⚠️ Примечание
TradingView требуют уже зарегистрированного пользователя чтобы работать со скринами так что нужно перед запуском программы получить куку что хранит инфу о твоём аканте.

1. Зайди на сайт [TradingView](https://www.tradingview.com).
2. Нажми на **F12** или **Ctrl+Shift+I** ну или **правая кнопка мыши и в низу будет "Просмотреть код элемента"**, для того чтобы открыть инструменты разработчика.
3. Найди в верхней панели "Console".
4. Пропиши команду для получения куки.

```js
document.cookie
```

5. Скопируй то что тебе выдала консоль.
6. Запусти программу
7. Вставь куку в месте с другими параметрами

Это всё сохранится в **config.json** так что если нужно будет ты найдёшь их легко.

Удачного использования😉😁!

# ENG

Hi! This program is made to "borrow" some crypto data from [TradingView](https://www.tradingview.com).  
I originally used it for my own project — but if you need it too, go ahead and take it, I almost don’t mind 😊  
[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)

It works by using **screens** *(which are either prebuilt or custom views for visualizing crypto data)* — and then uses them for some polite data borrowing.

## Getting Started:

1. Go to [TradingView](https://www.tradingview.com)  
2. Sign up  
3. Set up your screen  
4. Click the *Save* button (top-left corner):  
   ![image](https://github.com/user-attachments/assets/594ef7f2-2481-426e-9555-5ce653d62b57)  
5. Copy the page URL

## If you're too lazy to type commands — just run:

```bash
  # The first script handles setup and the second one runs the program.
  ./settup.sh && run.sh
```
Уж прости, тут без команд не обайтимь😅
## If you’re not lazy, or the script doesn’t work:

```bash
# If you don’t have Python installed:
sudo apt install python3

# Create a virtual environment and activate it (from the root project folder)::
python3 -m venv venv
source venv/bin/activate
pip install selenium

# Run the program
python3 main.py

# If pip fails, try moving the project to another folder, like your home directory:
cd ..
mv cryptoParser ~/cryptoParser
cd ~
git clone https://github.com/Q-Vortex/CryptoParser.git
```

## Now just configure the program:

It’s easy. Open the config.json file in the project folder and edit the settings.  
Or just run the program — it’ll help you set everything up interactively.

## ⚠️ Note
TradingView requires a logged-in user to access screens, so before using the program, you need to get your cookie containing login info. 

1. Go to [TradingView](https://www.tradingview.com)  
2. Press **F12**, or **Ctrl+Shift+I**, or right-click and choose **"Inspect"** to open dev tools  
3. Go to the **Console** tab  
4. Run this command:

```js
document.cookie
```

5. Copy the output  
6. Launch the program  
7. Paste the cookie along with the other config values

Everything will be saved to **config.json**, so you can easily find or change it later.

Enjoy and happy scraping! 😉😁

