FROM python:3.9-slim
ENV APP_HOME /app
COPY . $APP_HOME
WORKDIR $APP_HOME
RUN pip install -r ./src/requirements.txt
CMD [ "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000" ]