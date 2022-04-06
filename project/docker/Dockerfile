FROM demers/python420w4a
ADD ./requirements.txt /
RUN pip3 install -r requirements.txt
#RUN useradd tiger
#USER tiger
RUN mkdir -p /mnt/data/files
WORKDIR /mnt/app/
CMD ["./run.sh","./project/myAPI/api.py"]