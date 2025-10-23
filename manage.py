#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":

   
    unicode = str
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "livingarchive.settings.production")

    from django.core.management import execute_from_command_line
    from django.core.management.commands.runserver import Command as runserver
    runserver.default_port = "8005"

    execute_from_command_line(sys.argv)
