#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

# python alg/manage.py collectstatic --no-input
# python alg/manage.py migrate