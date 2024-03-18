sudo apt update
sudo apt install git
git --version
git clone https://github.com/Buchdd/AdminLR3.git

Для установки Docker на Ubuntu следуйте этим шагам:

1. Обновите индекс пакетов APT:
sudo apt update

2. Установите необходимые пакеты, позволяющие apt использовать репозитории по протоколу HTTPS:
sudo apt install apt-transport-https ca-certificates curl software-properties-common

3. Добавьте официальный ключ GPG Docker:
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

4. Добавьте репозиторий Docker в список источников пакетов APT:
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

5. Обновите индекс пакетов с добавленным репозиторием Docker:
sudo apt update

6. Установите Docker:
sudo apt install docker-ce

7. После установки Docker добавьте своего пользователя в группу docker, чтобы избежать использования sudo при запуске Docker команд:
sudo usermod -aG docker $USER

8. Перезапустите компьютер или перезапустите службу Docker:
sudo systemctl restart docker

Теперь Docker должен быть успешно установлен на Вашем Ubuntu. Вы можете проверить установку, запустив команду:
docker --version
