Feature: Verificando a cota racial do candidato

Scenario: Um candidato reconhecido para verificar a cota racial
    Given o ambiente seja preparado com sucesso
    When a foto /home/yara/Área de trabalho/ssc_cotas_bdd/faces/elliot1.jpg de um candidato for capturada
    Then um(a) candidato deve ser reconhecido(a)
    Then a cota racial do candidato deve ser impressa