# SSAFY Docker 설치 가이드 문서

부울경 8기 최홍준
{: .text-right}


## 0. 목차




- 개요

  - 도커 엔진과 도커 데스크탑의 차이


- 시작하기

  - 리눅스 환경에서 도커 엔진 설치하기

  - 




## 1. 개요


도커란 가상머신과 유사하게 동작하는 듯 하지만 각 게스트 머신마다 OS를 설치하는 가상머신과 세부 구조가 다릅니다.
호스트 OS의 리눅스 커널을 활용하는 도커 엔진 위에서 동작하여 게스트 머신마다 OS를 설치 할 필요가 없는 것이 장점입니다.

도커 설치는 리눅스와 윈도우에서의 설치 방법이 다릅니다.
이 문서는 두 환경 모두의 설치가이드를 준비했습니다.



### 1.1. 도커 엔진과 도커 데스크탑의 차이


도커 엔진은 애플리케이션을 빌드하고 컨테이너화하기 위한 오픈 소스 컨테이너화 기술입니다. 도커 데스크탑은 도커 엔진에 컨테이너, 이미지를 관리 할 수 있는 기능과 이러저러한 편의기능을 덧붙인 프로그램입니다.


## 2. 시작하기




### 2.1. 리눅스 환경에서 도커엔진 설치하기


#### 2.1.1. AWS EC2 환경에서 도커 설치하기



이 문서에선 AWS의 EC2 서버에 우분투 CLI 환경을 구성 한 뒤 도커를 설치하였습니다.










#### 2.1.2. VMware를 이용한 리눅스 가상환경


이 문서에선 VMware에 우분투 gui 환경을 설치하여 도커를 설치 하였습니다.

진행 과정은 2.1.1. 의 과정과 매우 유사합니다.


리눅스 환경 터미널에서 다음 명령어를 입력합니다.

`sudo apt-get update`

```
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


위 명령어들로 도커 레포지토리를 설치 할 수 있습니다.

그리고 도커 설치를 위해 다음 명령어를 입력합니다.

`sudo apt-get update`
`sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin`

그러면 다음과 같이 설치가 진행됩니다.


![Alt text](cap/Cap%202023-01-17%2014-46-16-114.png)


`sudo docker version`을 입력하여 도커가 설치된 것을 확인 할 수 있습니다.

![Alt text](cap/Cap%202023-01-17%2014-58-05-235.png)


`systemctl status docker.service`를 입력하여 도커가 실행중인지 확인합니다.

![Alt text](cap/Cap%202023-01-17%2014-46-48-608.png)

만약 위처럼 도커가 실행중이 아니라면

`systemctl start docker.service`를 입력하여 도커를 실행시킵니다.


`sudo docker run hello-wolrd`를 입력하여 도커 이미지를 실행을 테스트합니다.

![Alt text](cap/Cap%202023-01-17%2014-47-18-038.png)  





### 2.2. 윈도우 WSL2을 활용하여 설치하기


도커는 리눅스 환경에서 동작하기 때문에 윈도우 하위 리눅스 시스템인 WSL2에 설치할 수 있습니다. WSL2 환경 셋팅이 되어있다는 전제하에 진행하겠습니다.
이 문서에선 우분투 22.04.1 LTS 버전을 선택하여 진행하겠습니다.


![Alt text](cap/Cap%202023-01-16%2010-39-33-332.png)




윈도우 환경에서 도커 데스크탑 [다운로드](https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe) 합니다.

설치 도중 WSL2 기반 엔진 사용 확인란을 선택하고 설치를 진행합니다.

![Alt text](cap/Cap%202023-01-16%2014-28-28-795.png)

설치가 되면 PC 재부팅을 하게 됩니다.

![Alt text](cap/Cap%202023-01-16%2014-28-28-795.png)

설정 일반 탭에서 Use the WSL 2 based engine이 체크 되어있는지 확인합니다.

![Alt text](cap/Cap%202023-01-16%2014-43-13-572.png)

설정 리소스 탭에서 WSL 로 설치한 이미지를 골라 체크 합니다.

![Alt text](cap/Cap%202023-01-16%2014-44-17-034.png)


> 주의!
> 도커 데스크탑은 Hyper-V 가상환경을 사용하기 때문에 VMware나 VirtualBox이 같이 사용되지 않습니다.




우분투 환경에서 `sudo docker version`을 입력하여 설치가 되어있음을 확인합니다.


![Alt text](cap/Cap%202023-01-16%2017-35-08-809.png)


`sudo docker run hello-world`를 입력하면 hello world 컨테이너가 생성되고 실행 됨을 확인 할 수 있습니다.


![Alt text](cap/Cap%202023-01-16%2017-37-33-348.png)






## 3. 주요 명령어




- `dockser create      ` : 새 컨테이너를 만듭니다.

- `dockser run         ` : 새 컨테이너를 실행시킵니다.

- `dockser start       ` : 정지한 컨테이너를 실행시킵니다.

- `dockser restart     ` : 컨테이너를 재시작 합니다.

- `dockser pause       ` : 컨테이너의 프로세스를 일시중지합니다.

- `dockser stop        ` : 컨테이너를 종료합니다.

- `dockser kill        ` : 컨테이너를 강제종료합니다.

- `dockser rm          ` : 컨테이너를 삭제합니다.

- `dockser unpause     ` : 일시정지한 컨테이너를 다시 동작합니다.

- `dockser images      ` : 이미지 리스트를 출력합니다.

- `dockser history     ` : 이미지의 과거 이력을 출력합니다.

- `dockser update      ` : 컨테이너 구성을 업데이트합니다.

- `dockser rename      ` : 컨테이너의 이름을 재지정합니다.

- `dockser logs        ` : 컨테이너의 로그를 출력합니다.

- `dockser ps          ` : 컨테이너 리스트를 나열합니다.

- `dockser container ls` : 컨테이너 리스트를 나열합니다.

- `dockser version     ` : 도커의 버전 정보를 표시합니다.


