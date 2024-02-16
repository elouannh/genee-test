FROM postgres:15.3
ADD create.sql /docker-entrypoint-initdb.d
RUN chmod 775 /docker-entrypoint-initdb.d/create.sql