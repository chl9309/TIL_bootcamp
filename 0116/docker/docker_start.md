# Docker

## 개요

도커란 가상머신과 유사하지만 각 게스트 머신마다 OS를 설치하는 가상머신과 달리 가볍게 동작합니다.
호스트 OS의 리눅스 커널을 활용하는 도커 엔진 위에서 동작하여 게스트 머신마다 OS를 설치 할 필요가 없는 것이 장점입니다.


## 시작하기

도커는 리눅스 환경에서 동작합니다. 윈도우 설치용 도커도 있으나 이 문서에선 리눅스 도커를 설치 할 예정입니다. 따라서 리눅스 OS가 설치 된 PC, AWS의 ec2 나 Azure의 VM 같은 클라우드의 가상머신, 혹은 윈도우 WSL2가 설치된 리눅스 환경 준비가 사전에 필요합니다.
이 문서는 WSL2로 우분투 22.04.1 LTS 버전을 설치하여 진행합니다.


도커 데스크탑과 도커 엔진



wsl2 를 활용하여 윈도우에서 도커 실행하기



```bash
sudo apt remove docker-desktop
```

```bash
sudo apt-get install ./docker-desktop-<version>-<arch>.deb
```

```
sudo apt install docker.io
```

```
docker version
```



도커 엔진 설치

```
sudo apt-get update
sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
```

```
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
```

```
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

```
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin
```





