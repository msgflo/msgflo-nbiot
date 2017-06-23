FROM python
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
ADD test_udp.py test_udp.py
ADD msgflo_nbiot/ msgflo_nbiot/
ADD sensors.json sensors.json
EXPOSE 16666
CMD python3 msgflo_nbiot/server.py