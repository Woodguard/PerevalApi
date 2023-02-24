from django.db import models
from django.contrib.auth.models import User


class Pereval_add(models.Model):
    new = 'NW'
    pending = 'PG'
    accepted = 'AD'
    rejected = 'RJ'
    STATUS = [(new, 'новая'), (pending, 'в работе'), (accepted, 'успешно'), (rejected, 'не принято')]

    foot = 'FT'
    ski = 'SK'
    catamaran = 'CM'
    kayak = 'KK'
    raft = 'RT'
    rafting = 'RG'
    bicycle = 'BC'
    car = 'CR'
    bike = 'BK'
    sail = 'SL'
    horseback = 'HB'
    ACTIVITY = [(foot, 'ходьба'), (ski, 'лыжи'), (catamaran, 'катамаран'), (kayak, 'байдарка'), (raft, 'плот'), (rafting, 'сплав'),
                (bicycle, 'велосипед'), (car, 'автомобиль'), (bike, 'мотоцикл'), (sail, 'парус'), (horseback, 'верхом')]

    winter = 'WR'
    spring = 'SG'
    summer = 'SR'
    autumn = 'AN'
    WEATHER = [(winter, 'Зима'), (spring, 'Весна'), (summer, 'Лето'), (autumn, 'Осень')]

    easy = 'EY'
    temperate = 'TE'
    normal = 'NL'
    hard = 'HD'
    LEVEL = [(easy, 'Легкий'), (temperate, 'Умеренный'), (normal, 'Средний'), (hard, 'Сложный')]

    a1 = 'AA'
    a2 = 'AQ'
    a3 = 'AX'
    b1 = 'BA'
    b2 = 'BQ'
    b3 = 'BX'
    absent = 'AT'
    DIFFICULTY = [(a1, '1А'), (a2, '2А'), (a3, '3А'), (b1, '1Б'), (b2, '2Б'), (b3, '3Б'), (absent, 'отсутствуют')]

    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    weather = models.CharField(max_length=2, choices=WEATHER, verbose_name='Сезон', default=summer)
    activity = models.CharField(max_length=2, choices=ACTIVITY, verbose_name='Категория туризма', default=foot)
    level = models.CharField(max_length=2, choices=LEVEL, verbose_name='Сложность маршрута', default=easy)
    difficulty = models.CharField(max_length=2, choices=DIFFICULTY, verbose_name='Сложность перевалов', default=absent)
    text = models.TextField(max_length=2750, verbose_name='Описание путишествия', blank=False)
    details = models.BooleanField(default=False, verbose_name='Дополнительные трудности')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=STATUS, verbose_name='Статус', default=new)

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = 'Подробности путей'
        verbose_name_plural = 'Подробности путей'


class Pereval_images(models.Model):
    earth = 'EA'
    pamal = 'PL'
    altai = 'AL'
    sevchuh = 'SH'
    yuchuh = 'YH'
    katun = 'KN'
    fansk = 'FA'
    gissah = 'GH'
    matchuz = 'MZ'
    gutak = 'GK'
    halai = 'HI'
    kivalai = 'KI'
    aladaglar = 'AR'
    tavr = 'TR'
    sayani = 'SI'
    listvya = 'LY'
    ivanovskii = 'II'
    mungun = 'MU'
    cagan = 'CN'
    chihach = 'CC'
    shapshal = 'SS'
    yugaltai = 'YA'
    mangolaltai = 'MI'
    zasayan = 'ZY'
    vasayan = 'VY'
    alatau = 'AU'
    kura = 'KA'
    AREAS = [(earth, 'Планета Земля'), (pamal, 'Памиро-Алай'), (altai, 'Алтай'), (sevchuh, 'Северо-Чуйский хребет'),
             (yuchuh, 'Южно-Чуйский хребет'), (katun, 'Катунский хребет'), (fansk, 'Фанские горы'), (gissah, 'Гиссарский хребет (участок западнее перевала Анзоб)'),
             (matchuz, 'Матчинский горный узел'), (gutak, 'Горный узел Такали, Туркестанский хребет'), (halai, 'Высокий Алай'),
             (kivalai, 'Кичик-Алай и Восточный Алай'), (aladaglar, 'Аладаглар'), (tavr, 'Тавр'), (sayani, 'Саяны'),
             (listvya, 'Хребет Листвяга'), (ivanovskii, 'Ивановский хребет'), (mungun, 'Массив Мунгун-Тайга'),
             (cagan, 'Хребет Цаган-Шибэту'), (chihach, 'Хребет Чихачева (Сайлюгем)'), (shapshal, 'Шапшальский хребет'),
             (yugaltai, 'Хребет Южный Алтай'), (mangolaltai, 'Хребет Монгольский Алтай'), (zasayan, 'Западный Саян'),
             (vasayan, 'Восточный Саян'), (alatau, 'Кузнецкий Алатау'), (kura, 'Курайский хребет')]

    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    areas = models.CharField(max_length=2, choices=AREAS, verbose_name='Район', default=earth)
    img = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
    time_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.areas

    class Meta:
        verbose_name = 'Фотографии'
        verbose_name_plural = 'Фотографии'
