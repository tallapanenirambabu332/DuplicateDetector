FROM python:3.7.5-slim
RUN mkdir -p /temp
WORKDIR /temp
RUN python -m pip install \
        parse \
        realpython-reader
COPY duplicate_detector.py test1 test2 test3 /temp/
CMD ["python", "duplicate_detector.py", "/temp" ]
