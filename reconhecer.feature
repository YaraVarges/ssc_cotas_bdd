Feature: Reconhecer candidato pela foto

Scenario: Um candidato deve ser reconhecido pela foto
    Given o ambiente seja preparado com sucesso
    When a foto /home/yara/Área de trabalho/ssc_cotas_bdd/faces/elliot1.jpg de um candidato for capturada
    Then um(a) candidato deve ser reconhecido(a)
    When a foto /home/yara/Área de trabalho/ssc_cotas_bdd/faces/darlene1.jpg de um candidato for capturada
    Then um(a) candidato deve ser reconhecido(a)

Scenario: Uma pessoa que nao e candidato nao deve ser reconhecida
    Given o ambiente seja preparado com sucesso
    When a foto /home/yara/Área de trabalho/ssc_cotas_bdd/faces/angela1.jpeg de um candidato for capturada
    Then nenhum candidato deve ser reconhecido

    