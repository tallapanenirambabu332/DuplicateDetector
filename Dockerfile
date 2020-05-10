FROM python:3.7.5-slim
RUN mkdir -p /temp
WORKDIR /temp
RUN python -m pip install \
        parse \
        realpython-reader
COPY duplicate_detector.py testingfile_1 testingfile_2 testingfile_3 /temp/
CMD ["python", "duplicate_detector.py", "/temp" ]
