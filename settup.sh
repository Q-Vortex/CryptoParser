read -p "Language? (eng/ru): " answer


if [ "$answer" = "eng" ]; then
  echo "First, register a user to proceed with package installation"
  sudo echo "Registration successful"
  
  which python3 --version >/dev/null 2>&1
  if [ $? -ne 0 ]; then
    echo "Checking..."
    if [ -e settup.sh ]; then
      if [ -d venv ]; then
        source venv/bin/activate
        pip show selenium >/dev/null 2>&1
        if [ $? -eq 0 ]; then
          echo "Everything is already installed"
          read -p "Do you want to run the program? (y/n): " answer
          if [ "$answer" = "y" ]; then
            python3 main.py
          fi
        else
          pip install selenium
        fi
      else
        echo "Creating virtual environment..."
        python3 -m venv venv
        source venv/bin/activate
        pip install selenium
      fi
    else
      echo "An error occurred — please enter the program directory first"
    fi
  else
    sudo apt install python3 -y
  
    echo "Creating virtual environment..."
    python3 -m venv venv
    source venv/bin/activate
  
    pip install selenium
  fi
  
  google-chrome --version
  if [ $? -ne 0 ]; then
    echo "Google Chrome is not installed"
    read -p "Do you want to install Google Chrome? (y/n): " answer
    if [ "$answer" = "y" ]; then
      wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
      sudo apt install ./google-chrome-stable_current_amd64.deb
    fi
  fi
else
  echo "Для начала зарегистрируй пользователя для дальнейшей скачки пакетов"
  sudo echo "Успешная регистрация"

  which python3 --version >/dev/null 2>&1
  if [ $? -ne 0 ]; then
    echo Проверка...
    if [ -e settup.sh ]; then
      if [ -d venv ]; then
        source venv/bin/activate
        pip show selenium >/dev/null 2>&1
        if [ $? -eq 0 ]; then
          echo "У тебя и так всё установлено"
          read -p "Зупустить прогу? (y/n): " answer
          if [ "$answer" = "y" ]; then
            python3 main.py
          fi
        else
          pip install selenium
        fi
      else
        echo "Создание venv..."
        python3 -m venv venv
        source venv/bin/activate
        pip install selenium
      fi
    else
      echo "Произошла ошибка, зайди сначала в папку с программой"
    fi
  else
    sudo apt install python3 -y

    echo "Создание venv..."
    python3 -m venv venv
    source venv/bin/activate

    pip install selenium
  fi

  google-chrome --version
  if [ $? -ne 0 ]; then
    echo "Google Chrome не установлен"
    read -p "Установить Google Chrome? (y/n): " answer
    if [ "$answer" = "y" ]; then
      wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
      sudo apt install ./google-chrome-stable_current_amd64.deb
    fi
  fi
fi

