FROM jenkins/jenkins:2.440.3
USER root
RUN apt-get update && apt-get install -y wget python3 python3-venv python3-pip
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google.list
RUN apt-get update && apt-get install -y google-chrome-stable
USER jenkins