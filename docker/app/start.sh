#!/usr/bin/env bash

# Add migrations to docker, part 2

# [bash_init]-[BEGIN]
# Exit whenever it encounters an error, also known as a non–zero exit code.
set -o errexit
# Return value of a pipeline is the value of the last (rightmost) command to exit with a non-zero status,
#   or zero if all commands in the pipeline exit successfully.
set -o pipefail
# Treat unset variables and parameters other than the special parameters ‘@’ or ‘*’ as an error when performing parameter expansion.
set -o nounset
# Print a trace of commands.
set -o xtrace
# [bash_init]-[END]

# Apply database migrations.
python manage.py migrate

# Execute custom commands.
python manage.py generate_contacts

# Run application.contacts_contact
python manage.py runserver 0.0.0.0:8000
