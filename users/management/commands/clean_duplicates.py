# clean_duplicates.py
from django.contrib.auth.models import User
from django.db.models import Count
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Clean duplicate users from database'

    def handle(self, *args, **kwargs):
        duplicates = User.objects.values('username').annotate(count=Count('id')).filter(count__gt=1)

        for dup in duplicates:
            username = dup['username']
            users = User.objects.filter(username=username).order_by('date_joined')
            # Keep the first user, delete the rest
            for user in users[1:]:
                user.delete()
                print(f"Deleted duplicate user: {username}")