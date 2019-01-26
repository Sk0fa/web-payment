#!/bin/sh

python migrations/manage.py version_control postgresql://$DB_USER:$DB_PASSWORD@$DB_HOST/$DB_NAME migrations
python manage.py upgrade
python server/run.py