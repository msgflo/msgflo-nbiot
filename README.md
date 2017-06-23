# msgflo-nbiot
Narrowband IoT gateway for MsgFlo

## How to run the tests

- create a virtualenv
- pip install -r requirements.txt
- pytest

## Docker docker, container, container

### To build and push
- docker build . -t msgflo/msgflo-nbiot
- docker login
- docker push msgflo/msgflo-nbiot

# To run
- docker run -d -p 16666:16666/udp msgflo/msgflo-nbiot
