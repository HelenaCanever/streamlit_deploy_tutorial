FROM python:3.11-slim
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 80
WORKDIR /app
ENTRYPOINT ["streamlit", "run"]
CMD ["main.py"]