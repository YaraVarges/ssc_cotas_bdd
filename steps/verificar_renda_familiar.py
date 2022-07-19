from behave import given, when, then
from ssc_cota import *

@then ("a renda familiar do candidato deve ser impressa")
def verificar_renda_familiar(context):
    assert context.reconhecido is True

