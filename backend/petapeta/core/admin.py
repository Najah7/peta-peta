from django.contrib import admin

from core import models

admin.site.register(models.CustomUser)
admin.site.register(models.Follow)
admin.site.register(models.Post)
admin.site.register(models.Phote)
admin.site.register(models.StickyNote)
admin.site.register(models.PostLike)
admin.site.register(models.StickyNoteLike)

