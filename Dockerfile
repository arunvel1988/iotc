FROM arm32v7/python:2.7.13-jessie

COPY led.py ./

RUN pip install --no-cache-dir rpi.gpio

CMD  ["python", "./led.py"]





