FROM mysql

ENV MYSQL_ROOT_PASSWORD root

ADD ./init_db /docker-entrypoint-initdb.d
EXPOSE 3306