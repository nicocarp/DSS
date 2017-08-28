# Antes crear volumen -> docker volume create dss_bd_tp3
docker run -d -p 5432:5432 -v dss_bd_tp3:/var/lib/postgresql/data --name postgres_container postgres
echo "Run postgres_container"
