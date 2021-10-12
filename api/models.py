from django.utils import timezone
from django.contrib import admin
from django.db import models

TRAINING_PLACE = [
    ("home", "Home"),
    ("zym", 'Zym'),
    ('others', 'Others'),
]

EVALUATION_PLACE = [
    ("excellent", '☆'),
    ("good", '◎'),
    ("normal", '〇'),
    ('bad', '×'),
]


class Training(models.Model):
    body_weight_10 = models.PositiveIntegerField(default=700)
    review = models.CharField(max_length=100, null=True, blank=True)
    evaluation = models.CharField(max_length=10,
                                  choices=EVALUATION_PLACE,
                                  default="good")
    place = models.CharField("Place",
                             max_length=10,
                             choices=TRAINING_PLACE,
                             default="home")
    created_at = models.DateField("Date", default=timezone.now(), )
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.created_at)

    @admin.display(
        description="Morning body-weight",
    )
    def body_weight(self):
        return f"{self.body_weight_10 / 10}Kg"


TRAINING_CHOICES = [
    ('push-up_normal', '腕立て(normal)'),
    ('push-up_wide', '腕立て(wide)'),
    ('bench_press', 'ベンチプレス'),
    ('arm_variations', '上腕総合（家）'),
    ('shoulder_press', 'ショルダーバックプレス'),
    ('side_rise', 'サイドレイズ'),
    ('arm_curl', 'アームカール'),
    ('kick_back', 'キックバック'),
    ('something_new', '新種目'),
]


class Content(models.Model):
    created_at = models.ForeignKey(Training, on_delete=models.CASCADE)
    training_type = models.CharField(max_length=40, choices=TRAINING_CHOICES)
    weight = models.PositiveIntegerField("Weight[Kg]", default=12)
    set1 = models.PositiveIntegerField(default=10)
    set2 = models.PositiveIntegerField(default=9, null=True, blank=True)
    set3 = models.PositiveIntegerField(default=8, null=True, blank=True)

    def __str__(self):
        return f"{self.training_type} : {self.weight}Kg"

    @admin.display(
        boolean=True,
        ordering='created_at',
        description='enough weight?',
    )
    def weight_is_enough(self):
        if (self.training_type == "push-up_normal") or (self.training_type == "bench_press"):
            return ((self.set1 + self.set2 + self.set3) <= 29) and (self.set3 <= 8)
        elif self.set1 >= 18 or self.set2 >= 15:
            return False
        else:
            return True

    @admin.display(
        ordering='created_at',
        description='weight amounts',
    )
    def weight_amounts(self):
        if self.set1 and self.set2 and self.set3:
            return f"{self.weight}Kg * ( {self.set1} + {self.set2} + {self.set3} )"
        elif self.set1 and self.set2:
            return f"{self.weight}Kg * ( {self.set1} + {self.set2} )"
        elif self.set1:
            return f"{self.weight}Kg * {self.set1}"
