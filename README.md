# Automação de Extração de Extratos FUNDEB

Este script automatiza o download dos arquivos csv do site de demonstrativos do Banco do Brasil para os municípios do Maranhão.

## Requisitos

Antes de executar o script, certifique-se de ter:

- Python instalado

- Google Chrome instalado

- ChromeDriver compatível com a versão do seu navegador

As bibliotecas Python necessárias:
- Selenium

Use: ```pip install selenium```

## Como Executar

Use: ```python extrato_fundeb.py```

Insira o mês e o ano no formato MM / AAAA quando solicitado (respeite o espaço).

O script processará os municípios e baixará os arquivos na pasta de downloads padrão.
Após isso, o script gerará um arquivo TXT de saída com os resultados dos municípios processados, separando os com erro e os bem-sucedidos.

## Tratamento de Erros

Municípios que apresentarem falha na consulta serão listados no arquivo de erro.

O script aguarda até 15 segundos para cada elemento antes de gerar erro.

Caso o site seja atualizado, os seletores XPath podem precisar de ajustes.

## Observação sobre os arquivos baixados:

Os municípios Barão de Grajaú e Godofredo Viana estavam sendo baixados duas vezes, em vez de o sistema considerar corretamente Grajaú e Viana como municípios distintos. Em razão dessa duplicidade, Viana e Grajaú acabaram sendo removidos da lista e é preciso realizar o download manual.

## Download Manual:
- Viana
- Grajaú

## Observações para o processamento dos arquivos:

Após concatenar os arquivos .csv, padronizar as datas substituindo as barras ```( / )``` por hifens ```( - )```.

No campo cnpj_titular, remover os caracteres de pontuação ```(. , / , -)```.

```Importante: manter este campo como texto (string), para evitar perda de zeros à esquerda ou alterações de formatação automática.```

## Padrão de Formatação Numérica:

Ao registrar valores monetários ou numéricos, deve-se substituir a vírgula (,) pelo ponto (.) como separador decimal e não utilizar ponto (.) como separador de milhar.

Formato incorreto: 34.153.652,22

Formato correto: 34153652.22
