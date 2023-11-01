FROM python:3.11.2

LABEL QA_level='UI_tests'

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

VOLUME /app/test_results

CMD python -m pytest tests --alluredir=test_results