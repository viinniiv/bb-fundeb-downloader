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
