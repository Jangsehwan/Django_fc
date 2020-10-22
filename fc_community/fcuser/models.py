from django.db import models

# Create your models here.


class Fcuser(models.Model):
    username = models.CharField(max_length=32,
                                verbose_name='사용자명')
    password = models.CharField(max_length=64,
                                verbose_name='비밀번호')
    registered_dttn = models.DateTimeField(auto_now_add=True,
                                           verbose_name='등록시간')

    class Meta:
        db_table = 'festclub_fuser'


# db에 makemigrations,migrate 이 두가지 명령어로 반영할수있게돼
# python manage.py makemigrations -생성
#  python manage.py migrate - db에 반영
