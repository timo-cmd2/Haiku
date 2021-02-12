FROM ubuntu:latest

RUN sudo apt-get install -y update && \
sudo apt-get -y update && \
sudo apt-get install -y g++ cmake git curl && \
sudo git clone https://github.com/timo-cmd2/Haiku.git && \
cd Haiku && \
sudo cmake && \
cd builds/bin && \
sudo ./node
