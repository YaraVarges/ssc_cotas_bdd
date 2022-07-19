from behave import given, when, then
from ssc_cota import *

@then ("a escolaridade do candidato deve ser impressa")
def verificar_escolaridade(context):
    assert context.reconhecido is True

