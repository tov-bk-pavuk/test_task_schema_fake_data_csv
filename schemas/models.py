from django.db import models


class Schema(models.Model):
    coma = ','
    semicolon = ';'

    sep_choices = [
        (coma, 'Coma'),
        (semicolon, 'Semicolon'),
    ]

    quotes_o = "'"
    quotes_d = '"'

    string_character_choices = [
        (quotes_o, 'Single quotes'),
        (quotes_d, 'Double quotes'),
    ]

    name = models.CharField(max_length=100, blank=False, unique=True)
    separator = models.CharField(
        max_length=1,
        choices=sep_choices,
        default=coma,
    )
    string_character = models.CharField(
        max_length=1,
        choices=string_character_choices,
        default=quotes_o,
    )
    modified = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class Column(models.Model):
    undefined = 'UD'
    full_name = 'FN'
    job = 'JB'
    email = 'EM'
    domain_name = 'DN'
    phone_number = 'PN'
    company_name = 'CN'

    type_choices = [
        (undefined, 'Undefined'),
        (full_name, 'Full Name'),
        (job, 'Job'),
        (email, 'Email'),
        (domain_name, 'Domain name'),
        (phone_number, 'Phone number'),
        (company_name, 'Company name'),
    ]

    name = models.CharField(max_length=100, blank=False)
    field_type = models.CharField(
        max_length=2,
        choices=type_choices,
        default=undefined,
    )
    order = models.PositiveSmallIntegerField(default=0)
    schema = models.ForeignKey(Schema, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
