#INSTALLATION GUIDE
##NOTE
- Recommended environment is Python3
- Use `virtualenv -p python3 venv` to install virtual environment.

##Observed Error
- jpype를 설치할 때 virtualenv에서는 오류가 남.
- 오류 해결 방법: `~/.bash_profile` 경로에  `export JAVA_HOME=$(/usr/libexec/java_home)` 추가. 
- 기본 JVM과 현재 설치된 JVM의 경로/버전이 달라서 그런 것으로 추정. (jpype는 1.6을 찾고, 컴퓨터엔 1.8이 설치 되어 있었음).

