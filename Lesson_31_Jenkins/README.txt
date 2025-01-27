1) Build test docker based on jenkins docker with chrome and python installed
docker build -t test_jenkins .

2)
docker run --rm -d --privileged --network=host -v <YOUR_LOCAL_DIR>/jenkins_home:/var/jenkins_home test_jenkins:latest

3) Open UI and setup jenkins
127.0.0.1:8080

4) Install selected plugins ( Git, Github, Mailer)

5) Additionally install such plugins ( Manage Jenkins -> Plugins - > Available plugins)
Allure, JUnit, Lockable Resources,Credentials, Pyenv Pipeline, Rebuilder

6) Create "git-creds" credentials ManageJenkins ->Credentials and add your username with private RSA ssh key
https://devjorgecastro.medium.com/setting-up-ssh-keys-for-jenkins-and-github-integration-22ce79f96fcf

7) ManageJenkins -> Tools -> Allure Commandline installations  set name "allure"

8) ManageJenkins -> Security -> Git Host Key Verification Configuration  set "No verification"

9) Create first job and add pipeline code