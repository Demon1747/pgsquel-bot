FROM python:alpine

COPY requirements.txt ./
RUN python3 -m pip install -r requirements.txt

RUN mkdir /dist
COPY main.py config.py handlers.py /dist/
COPY --chmod=555 build/entrypoint.sh /

ENTRYPOINT ["/entrypoint.sh"]
