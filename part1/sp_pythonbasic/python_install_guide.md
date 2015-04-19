<h2>파이썬 설치 가이드</h2>

---

설치 관련 사이트 소개

[파이썬 공식 다운로드](https://www.python.org/downloads/)

[파이썬 모듈 설치 Doc](https://docs.python.org/2.7//installing/index.html)

---

바이오 스핀 과거 자료 

[ipython 설치 + 소개](http://nbviewer.ipython.org/gist/irobii/014b8aa3574090a0d04a)

[ipython + notebook 설치 가이드](http://nbviewer.ipython.org/github/lexifdev/uds_study_7th/blob/master/src/__setup.ipynb)

---

<h1>1. 파이썬 설치</h1>

<h3>1.1 우분투 설치</h3>

리눅스에는 기본적으로 파이썬이 설치되어 있음.

**파이썬 모듈 관리 프로그램 pip 깔기** (파이썬 버전 2.7.9 부터는 이미 설치되어 있다.)

	> sudo apt-get install python-pip

**파이썬 가상환경 프로그램 깔기**

 (의존성 라이브러리를 독립적인 공간에 설치해준다. 필수는 아니지만, 추천사항)

	> sudo pip install virtualenv

**'myenv' 라는 이름의 가상환경 사용**

	# 가상환경 만들기
	> virtualenv myenv

	# 가상환경 들어가기
	> source myenv/bin/activate

    # 원하는 모듈 설치 및 작업
	# 해당 모듈은 myenv 안에만 설치된다.
	# 만약 가상환경 내부가 아니라면, 전역에 설치되는 것이라 sudo pip install 로 설치해야 한다.
	(myenv)> pip install ...

	# 가상환경 끝내기
	(myenv)> deactivate
	>

(추가 사항)

[virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/install.html) 라는 프로그램은 virtualenv 여러개를 편하게 활성화 시키고 관리할 수 있게 해준다.

설치가 약간 복잡하다. 관심있으면 위 가이드대로 천천히 실행하면 됨.

<br/>

<h3>1.2 윈도우 설치</h3>

**파이썬 설치**

[다운로드 https://www.python.org/downloads/](https://www.python.org/downloads/) 사이트에서 받아서 설치 (현재 최신버전 2.7.9)

그런데 설치해도, 아직 cmd 창에서 python 입력해도 실행이 안된다.

아직 path 추가가 안됬기 때문.

(Path 에 추가해야만 운영체제가 해당 프로그램을 찾을 수 있다.)

<br/>

**파이썬 Path 추가**

내컴퓨터 -> 속성 -> 고급시스템 설정 -> 환경변수

방법1. 시스템 변수 탭(모든 사용자에게 영향)에서 Path 값에 ;C:\Python27 추가

방법2. 사용자 변수 탭에서 Path 값에 (없으면 만들어서) ;C:\Python27 추가

(개인적으로 방법2 추천)

이제 cmd 창에서 python 입력하면 실행되는 것을 확인할 수 있음

(환경변수 등을 변경했을시에는, 새 cmd 창을 띄워야 적용된다.)

<br/>

**pip 설치**

2.7.9 버전 이후부터는 이미 파이썬에 같이 들어가있다. 

확인하고 싶으면, cmd 창에서 python -m pip freeze 라고 쳐보면 된다.

[get-pip.py](https://raw.githubusercontent.com/pypa/pip/master/contrib/get-pip.py) 파일을 다운받아, 이 파일이 있는 디렉토리 cmd 창에서 아래처럼 치면된다.
	
	> python get-pip.py

**virtualenv 설치**

	> python -m pip install virtualenv

**'myenv' 라는 가상환경 다루기**

	# 가상환경 생성
	> python -m virtualenv myenv

	# 가상환경 활성화
	> cd myenv/Scripts
	> activate
	(myenv)>

	# 다른 모듈 설치 및 작업
	(myenv)> pip install ...

	# 가상환경 끄기
	(myenv)> deactivate
	>


<h1>2. ipython + notebook 설치</h1>

**ipython 설치**

	> pip install ipython

(우분투의 경우, pyzmq 설치에서 에러가 발생하는데, stackoverflow 에 나온 해결 방법)

	> sudo apt-get install build-essential autoconf libtool pkg-config python-opengl python-imaging python-pyrex python-pyside.qtopengl idle-python2.7 qt4-dev-tools qt4-designer libqtgui4 libqtcore4 libqt4-xml libqt4-test libqt4-script libqt4-network libqt4-dbus python-qt4 python-qt4-gl libgle3 python-dev

**notebook 실행에 필요한 모듈들 설치**

([ipython notebook 소개 블로그](https://blog.ansuchan.com/documentation-with-ipython-notebook/) 참고하였음)

	> pip install jinja2 sphinx pyzmq pygments tornado nose readline  

**notebook 실행**

	# (--pylab inline 이라는 인자를 주어야 브러우저 내에서 그래프가 그려진다.)
	> ipython notebook --pylab inline

그러면, notebook 서버가 실행되고, 브라우저로 창이 뜬다.

브러우저 창에서 python_beginner.ipynb 파일을 열면, 파이썬 기초 설명 내용이 나온다.
