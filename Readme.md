Steps to take after fetching the latest code:
Fetch the Latest Code from GitHub: Run the following to pull the latest changes:

bash
Copy code
git pull origin main # or the appropriate branch
Stop Gunicorn: You should stop the current Gunicorn process to release resources and ensure it picks up the latest code. You can stop Gunicorn by running:

bash
Copy code
sudo systemctl stop gunicorn # if using systemd
Or, if you're running it manually:

bash
Copy code
pkill gunicorn
Apply Any Necessary Migrations: If there are any new migrations, apply them:

bash
Copy code
python manage.py migrate
Restart Gunicorn: After stopping Gunicorn, restart it to load the latest changes:

bash
Copy code
sudo systemctl start gunicorn # if using systemd
Or, if you're running Gunicorn manually:

bash
Copy code
gunicorn --workers 3 progress_reporting.wsgi:application --bind 0.0.0.0:8000
Check Logs: After restarting, check the logs to ensure everything is running smoothly:

bash
Copy code
journalctl -u gunicorn # If using systemd
This will ensure that the changes you pulled from GitHub are reflected in the running application.
