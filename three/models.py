from django.db import models

# DB에서 테이블의 역할을 하는 클래스 작성 파일
# model을 설정하는 파일

class Food(models.Model):
    name = models.CharField(max_length=20)
    adr = models.CharField(max_length=50)
    # 비밀번호를 설정하고 싶은 경우 - 길이 20자, 공백 비허용
    pw = models.CharField(max_length=20, default=None, null=True)

    create_day = models.DateTimeField(auto_now_add=True)
    update_day = models.DateTimeField(auto_now=True)


class Review(models.Model):
    score = models.IntegerField()
    comment = models.CharField(max_length=100)

    # Food가 지워진다면 on_delete로 CASCADE(종속)된 Review도 같이 지워진다.
    # Food : Review >> one to many
    res = models.ForeignKey(Food, on_delete=models.CASCADE)

    # Food가 지워져도 아무런 일도 하지 않는다.
    # res = models.ForeignKey(Food, on_delete=models.DO_NOTHING)

    # Food가 지워지면 Food 속성이 NULL 값으로 채워진다.
    # res = models.ForeignKey(Food, on_delete=models.SET_NULL())

    create_day = models.DateTimeField(auto_now_add=True)
    update_day = models.DateTimeField(auto_now=True)