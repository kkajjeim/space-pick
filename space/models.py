from django.db import models

from common.mixin import TimeStampMixin


class Host(TimeStampMixin):
    name = models.CharField(max_length=10, verbose_name="호스트명")
    email = models.CharField(max_length=30, verbose_name="이메일")
    contact = models.CharField(max_length=20, verbose_name="대표 전화")
    phone = models.CharField(max_length=20, verbose_name="휴대폰")

    def __str__(self):
        return f'{self.name}-{self.id}'

    class Meta:
        verbose_name = "호스트"
        verbose_name_plural = "호스트"


class Location(models.Model):
    city = models.CharField(max_length=10, verbose_name="시")
    district = models.CharField(null=True, max_length=10, verbose_name="군/구")
    name = models.CharField(max_length=20, verbose_name="지역명")

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "지역"
        verbose_name_plural = "지역"


class SpaceCategory(models.Model):
    title = models.CharField(max_length=30, verbose_name="공간 분류")
    description = models.CharField(max_length=100, verbose_name="유형 소개")

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = "공간 유형"
        verbose_name_plural = "공간 유형"


# TODO: image, map,
class Space(TimeStampMixin):
    host = models.ForeignKey(Host, on_delete=models.CASCADE, verbose_name="호스트")
    location = models.ForeignKey(Location, on_delete=models.CASCADE, verbose_name="위치")
    categories = models.ManyToManyField(SpaceCategory, verbose_name="공간 유형")
    address = models.CharField(max_length=255, verbose_name="주소")
    name = models.CharField(max_length=128, verbose_name="공간명")
    summary = models.TextField(max_length=30, null=True, blank=True, verbose_name="한 줄 소개")
    description = models.TextField(null=True, blank=True, verbose_name="소개")
    hashtag = models.CharField(max_length=128, null=True, blank=True, verbose_name="태그")
    main_image = models.CharField(max_length=255, verbose_name="대표 이미지")
    open_time = models.CharField(max_length=4, verbose_name="운영 시작 시간 (ex: 0900)")
    close_time = models.CharField(max_length=4, verbose_name="운영 마감 시간 (ex: 2400)")
    off_days = models.CharField(max_length=20, null=True, verbose_name="정기휴무 (월 0 일 6 ex: [0, 1, 6]")
    max_fit = models.IntegerField(verbose_name="최대 인원")
    activate = models.BooleanField(default=True, verbose_name="활성화 여부")

    def __str__(self):
        return f'{self.location.name}-{self.name}'

    class Meta:
        verbose_name = "공간"
        verbose_name_plural = "공간"


class SpacePackage(TimeStampMixin):
    space = models.ForeignKey(Space, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, verbose_name="패키지명")
    price = models.IntegerField(verbose_name="패키지 가격")
    check_in = models.CharField(max_length=4, verbose_name="체크인 (ex: 1800)")
    check_out = models.CharField(max_length=4, verbose_name="체크아웃 (ex: 0700)")
    check_out_next_day = models.BooleanField(verbose_name="익일 체크아웃 여부")

    def __str__(self):
        return f'{self.space}-{self.name}'

    class Meta:
        verbose_name = "패키지"
        verbose_name_plural = "패키지"


class SpacePackageSpecialPrice(TimeStampMixin):
    package = models.ForeignKey(SpacePackage, on_delete=models.CASCADE)
    start_date = models.DateField(verbose_name="행사가 적용 시작일")
    end_date = models.DateField(verbose_name="행사가 적용 종료일")
    special_price = models.IntegerField(verbose_name="행사가")

    class Meta:
        verbose_name = "패키지 행사가"
        verbose_name_plural = "패키지 행사가"


