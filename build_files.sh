echo "BUILD START"
python3.8.10 -m pip install ir requirements.txt
python3.8.10 manage.py collectstatic --noinput --clear
echo "BUILD end"
