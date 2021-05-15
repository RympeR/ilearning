import os
import random
import string
from rest_framework import pagination
from rest_framework.response import Response


def id_generator(size=12, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def set_unique_file_name(file):
    if file:
        end_extension = file.rsplit('.', 1)[1]
        file_name = id_generator() + '.' + end_extension
        return file_name
    else:
        return None


def user_avatar(instance, filename):
    instance.original_file_name = filename
    file = set_unique_file_name(filename)
    return os.path.join('user', filename)


def attachments(instance, filename):
    instance.original_file_name = filename
    file = set_unique_file_name(filename)
    return os.path.join('attachments', filename)


def card_attachment(instance, filename):
    instance.original_file_name = filename
    file = set_unique_file_name(filename)
    return os.path.join('card_attachment', filename)
