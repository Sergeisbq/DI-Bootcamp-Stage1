#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python3 alg/manage.py collectstatic --no-input
python3 alg/manage.py migrate