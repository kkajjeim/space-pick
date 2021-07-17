from django.db import models


class Host(models.Model):
    name = models.CharField(max_length=10, verbose_name="호스트명")
    email = models.CharField(max_length=30, verbose_name="이메일")
    contact = models.CharField(max_length=20, verbose_name="대표 전화")
    phone = models.CharField(max_length=20, verbose_name="휴대폰")


class Location(models.Model):
    city = models.CharField(max_length=10, verbose_name="시")
    district = models.CharField(null=True, max_length=10, verbose_name="군/구")
    tag = models.CharField(max_length=20, verbose_name="노출명")


class SpaceCategory(models.Model):
    title = models.CharField(max_length=30, verbose_name="유형")
    description = models.CharField(max_length=100, verbose_name="설명")


# TODO: image, map,
class Space(models.Model):
    host = models.ForeignKey(Host, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    categories = models.ManyToManyField(SpaceCategory)
    name = models.CharField(max_length=128, verbose_name="공간명")
    summary = models.TextField(max_length=30, null=True, verbose_name="요약")
    description = models.TextField(null=True, verbose_name="소개")
    hashtag = models.CharField(max_length=128, null=True, verbose_name="태그")
    main_image = models.CharField(max_length=255, null=True, verbose_name="대표 이미지")
    open_time = models.CharField(max_length=4, verbose_name="오픈")
    close_time = models.CharField(max_length=4, verbose_name="마감")
    off_days = models.CharField(max_length=20, verbose_name="정기휴무")
    max_fit = models.IntegerField(verbose_name="최대 인원")
    activate = models.BooleanField(default=True, verbose_name="노출 여부")


class SpacePackage(models.Model):
    space = models.ForeignKey(Space, on_delete=models.CASCADE)
    price = models.IntegerField(verbose_name="가격")
    check_in = models.CharField(max_length=4, verbose_name="체크인")
    check_out = models.CharField(max_length=4, verbose_name="체크아웃")
    check_out_next_day = models.BooleanField(verbose_name="익일 체크아웃 여부")


class SpacePackageSpecialPrice(models.Model):
    package = models.ForeignKey(SpacePackage, on_delete=models.CASCADE)
    start_date = models.DateField(verbose_name="행사가 적용 시작일")
    end_date = models.DateField(verbose_name="행사가 적용 종료일")
    special_price = models.IntegerField(verbose_name="행사가격")
