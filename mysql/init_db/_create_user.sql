-- Không thể dùng tài khoản root để kết nối từ xa --> tạo mới
-- Tạo tài khoản "nguoicaotuoi" với password "12345"
-- Tài khoản này đc sử dụng trong mysql_api để kết nối

CREATE USER 'nguoicaotuoi'@'%' IDENTIFIED BY '12345';
GRANT ALL PRIVILEGES ON *.* TO 'nguoicaotuoi'@'%';
FLUSH PRIVILEGES;