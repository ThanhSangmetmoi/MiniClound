FROM mariadb:10.11

# Sao chép script khởi tạo vào container
COPY init.sql /docker-entrypoint-initdb.d/

# Cấu hình cơ bản (tùy chọn)
COPY my.cnf /etc/mysql/conf.d/my.cnf
