FROM python:3.8

RUN mkdir -p /home/proj
WORKDIR /home/proj
COPY . .

RUN pip3 install -r requirements.txt
RUN pyinstaller hello.py
RUN ls

CMD /home/proj/dist/hello/hello

