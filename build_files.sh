echo "Installing dependencies..."

python manage.py migrate
python manage.py collectstatic --noinput