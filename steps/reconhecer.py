from behave import given, when, then
from ssc_cota import *

@given("o ambiente seja preparado com sucesso")
def given_ambiente_preparado(context):
    context.configuracao, context.dados_falsos = preparar()
    
    context.candidatos_reconhecidos = {}
    context.candidatos_perfil1 = {}
    context.candidatos_perfil2 = {}
    
    assert context.configuracao != None

@when ("a foto {foto} de um candidato for capturada")
def when_foto_capturada(context, foto):
    visitante = simular_visita(foto)
    context.reconhecido, context.candidato = reconhecer(visitante, context.configuracao, context.dados_falsos)

    assert True

@then("um(a) candidato deve ser reconhecido(a)")
def then_candidato_reconhecido(context):
    id_candidato = secrets.token_hex(nbytes=16).upper()
    context.candidatos_reconhecidos[id_candidato] = context.candidato

    assert context.reconhecido is True

@then("nenhum candidato deve ser reconhecido")
def then_candidato_nao_reconhecido(context):
    assert context.reconhecido is False