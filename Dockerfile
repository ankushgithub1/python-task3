FROM python:3.9-slim
WORKDIR /app
RUN pip install Flask
COPY app.py /app/app.py
EXPOSE 8080
CMD ["python", "app.py"]
