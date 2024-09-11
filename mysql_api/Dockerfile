FROM python:3.9-slim
ENV APP_HOME /api
COPY . $APP_HOME
WORKDIR $APP_HOME
RUN pip install -r ./app/requirements.txt
CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000" ]