FROM python:3.11
ENV PORT=8088

COPY ./*.py ./
COPY ./*.txt ./

# install requirements
RUN pip install -r requirements.txt

EXPOSE ${PORT}


RUN echo "App port: ${PORT}"

CMD ["python", "app.py", "--port", "8088"]