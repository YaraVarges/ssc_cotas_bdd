import face_recognition
import secrets
import random
import faker
import simpy
import json

FOTOS_DOS_CANDIDATOS = [
    "/home/yara/Área de trabalho/ssc_cotas/faces/angela1.jpeg",
    "/home/yara/Área de trabalho/ssc_cotas/faces/tyrell1.jpeg",
    "/home/yara/Área de trabalho/ssc_cotas/faces/price1.jpg",

    "/home/yara/Área de trabalho/ssc_cotas/faces/darlene1.jpg",
    "/home/yara/Área de trabalho/ssc_cotas/faces/darlene2.jpg",
    "/home/yara/Área de trabalho/ssc_cotas/faces/darlene3.jpg",

    "/home/yara/Área de trabalho/ssc_cotas/faces/elliot1.jpg",
    "/home/yara/Área de trabalho/ssc_cotas/faces/elliot2.jpg",
    "/home/yara/Área de trabalho/ssc_cotas/faces/elliot3.jpg"
]
#Utilizei o mesmo banco de imagem da aula, visto que o face_recognition não faz reconhecimento de cor da pele

ARQUIVO_CONFIGURACAO = "/home/yara/Área de trabalho/ssc_cotas/configuracao.json"

TEMPO_CANDIDATO = 150
TEMPO_ESCOLARIDADE = 115
TEMPO_RENDA = 165
TEMPO_COTA = 120


def preparar():
    global configuracao

    configuracao = None
    with open(ARQUIVO_CONFIGURACAO, "r") as arquivo_configuracao:
        configuracao = json.load(arquivo_configuracao)
        if configuracao:
            print("Avaliação de bolsas de estudos iniciada.")

    candidatos_reconhecidos = {}

    candidatos_perfil1 = {}

    candidatos_perfil2 = {}

    dados_falsos = faker.Faker(locale="pt_BR")

    return configuracao, dados_falsos

def simular_visita(foto):
    visitante = {
        "foto": foto,
        "ficha": None
    }

    return visitante

def reconhecer(visitante, configuracao, dados_falsos):

    print("Iniciando reconhecimento de candidato.")
    foto_visitante = face_recognition.load_image_file(visitante["foto"])
    encoding_foto_visitante = face_recognition.face_encodings(foto_visitante)[0]

    reconhecido = False
    for ficha in configuracao["candidatos"]:
        fotos_banco = ficha["fotos"]
        total_reconhecimentos = 0

        for foto in fotos_banco:
            foto_banco = face_recognition.load_image_file(foto)
            encoding_foto_banco = face_recognition.face_encodings(foto_banco)[0]

            foto_reconhecida = face_recognition.compare_faces([encoding_foto_visitante], encoding_foto_banco)[0]
            if foto_reconhecida:
                total_reconhecimentos += 1

        if total_reconhecimentos/len(fotos_banco) > 0.7:
            reconhecido = True

            visitante["ficha"] = {}
            visitante["ficha"]["nome"] = dados_falsos.name()
            visitante["ficha"]["idade"] = random.randint(7, 100)
            visitante["ficha"]["cor"] = random.choice(["Preta", "Parda", "Indigena"])
            visitante["ficha"]["escolaridade"] = random.choice(["Particular", "Publica"])
            visitante["ficha"]["renda"] = random.choice(["1212", "2456", "2985"])
            visitante["ficha"]["endereco"] = dados_falsos.address()


    return reconhecido, visitante

def imprimir_ficha(candidato):
    print("Nome Completo:", candidato["ficha"]["nome"])
    print("Idade:", candidato["ficha"]["idade"])
    print("Cota Racial: Pessoa", candidato["ficha"]["cor"])
    print("Escolaridade:", candidato["ficha"]["escolaridade"])
    print("Renda Familiar:", candidato["ficha"]["renda"])

def reconhecer_candidato(candidatos_reconhecidos):
       
    print("Reconhecendo um candidato em ciclo/tempo: ")

    visitante = simular_visita()
    reconhecido, candidato = reconhecer(visitante)
    if reconhecido:
        id_candidato = secrets.token_hex(nbytes=16).upper()
        candidatos_reconhecidos[id_candidato] = candidato

        print("Um candidato foi reconhecido. Ficha:")
        imprimir_ficha(candidato)
    else:
        print("Candidato não foi reconhecido")

        

def verificar_escolaridade(candidatos_reconhecidos, candidatos_perfil2, candidatos_perfil1, candidato):

    if len(candidatos_reconhecidos):
        print("Verificando Escolaridade do candidato em ciclo/tempo")
                    
        for id_candidato, candidato in list(candidatos_reconhecidos.items()):
            
            if((candidato["ficha"]["escolaridade"] == "Publica")):
                candidatos_perfil2[id_candidato] = candidato
                candidatos_reconhecidos.pop(id_candidato)
                print("Candidato", candidato["ficha"]["nome"], "APROVACAO COM 100% pela ESCOLARIDADE:",candidato["ficha"]["escolaridade"])
                

            if(candidato["ficha"]["escolaridade"] == "Particular"):
                candidatos_perfil1[id_candidato] = candidato
                candidatos_reconhecidos.pop(id_candidato)
                print("Candidato", candidato["ficha"]["nome"], "APROVACAO COM 50% pela ESCOLARIDADE:",candidato["ficha"]["escolaridade"])
        
    

def verificar_cota_racial(candidatos_reconhecidos, candidatos_perfil2, candidatos_perfil1, candidato):

    if len(candidatos_reconhecidos):
        print("Verificando Cota Racial do candidato em ciclo/tempo")

        for id_candidato, candidato in list(candidatos_reconhecidos.items()):
            
            if((candidato["ficha"]["cor"] == "Preta")):
                candidatos_perfil2[id_candidato] = candidato
                candidatos_reconhecidos.pop(id_candidato)
                print("Candidato", candidato["ficha"]["nome"], "APROVADO COM 100% pela COTA RACIAL: Pessoa",candidato["ficha"]["cor"])
                

            if(candidato["ficha"]["cor"] == "Indigena"):
                candidatos_perfil1[id_candidato] = candidato
                candidatos_reconhecidos.pop(id_candidato)
                print("Candidato", candidato["ficha"]["nome"], "APROVADO COM 20% pela COTA RACIAL: Pessoa",candidato["ficha"]["cor"])


def verificar_renda_familiar(candidatos_reconhecidos, candidatos_perfil2, candidatos_perfil1, candidato):

    if len(candidatos_reconhecidos):
        print("Verificando Renda familiar do candidato em ciclo/tempo")               

        for id_candidato, candidato in list(candidatos_reconhecidos.items()):
            
            if((candidato["ficha"]["renda"] == "1212")):
                candidatos_perfil2[id_candidato] = candidato
                candidatos_reconhecidos.pop(id_candidato)
                print("Candidato", candidato["ficha"]["nome"], "APROVADO COM 100% pela RENDA FAMILIAR:",candidato["ficha"]["renda"])
                

            if(candidato["ficha"]["renda"] == "2456"):
                candidatos_perfil1[id_candidato] = candidato
                candidatos_reconhecidos.pop(id_candidato)
                print("Candidato", candidato["ficha"]["nome"], "APROVADO COM 50% pela RENDA FAMILIAR:",candidato["ficha"]["renda"])



