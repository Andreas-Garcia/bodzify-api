sudo -u postgres dropdb -e bodzify_api
sudo -u postgres -H -- psql -c "
create database bodzify_api with owner django;"
sudo rm -r ~/Git/bodzify-api/bodzify_api/migrations/*
python3 ~/Git/bodzify-api/manage.py migrate
python3 ~/Git/bodzify-api/manage.py migrate --fake
python3 ~/Git/bodzify-api/manage.py makemigrations 
python3 ~/Git/bodzify-api/manage.py migrate --fake-initial
python3 ~/Git/bodzify-api/manage.py migrate
python3 ~/Git/bodzify-api/manage.py makemigrations bodzify_api
cp ~/Git/bodzify-api/bodzify_api/migrations_initial_data/0002_populate.py ~/Git/bodzify-api/bodzify_api/migrations/
python3 ~/Git/bodzify-api/manage.py migrate
python3 ~/Git/bodzify-api/manage.py createsuperuser --username admin --email admin@bodzify.com