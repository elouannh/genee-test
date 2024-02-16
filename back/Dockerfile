FROM python:3.11.4-bookworm

RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install -y postgresql-client vim

COPY ./ /code/
WORKDIR /code
run ls

ENV PYTHONPATH=/code/src

RUN CPUCOUNT=1 pip install -r src/requirements.txt

EXPOSE 5001

ENTRYPOINT [ "bash", "-cl", "./back-start.sh" ]