FROM ubuntu:latest
RUN mkdir /token
RUN mkdir /token/secret
RUN echo 'hello docker' > /token/secret/rsa.txt
RUN apt-get update && apt-get install -y \
nodejs \
python3-pip \
python3-pyqt5
COPY program.js /static.js
CMD ["cat", "/token/secret/rsa.txt"]
CMD ["sh", "-c", "node static.js"]

