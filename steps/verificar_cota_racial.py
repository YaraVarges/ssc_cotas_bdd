from behave import given, when, then
from ssc_cota import *

@then ("a cota racial do candidato deve ser impressa")
def verificar_cota_racial(context):
    assert context.reconhecido is True

