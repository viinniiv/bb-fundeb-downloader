from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException

def processar_municipios(municipios: list, mes_ano: str):

    valor_mes, valor_ano = mes_ano.split(" / ")
    arquivo_saida = f"resultado_fundeb_{valor_mes}_{valor_ano}.txt"
    
    navegador = webdriver.Chrome()
    municipios_com_erro = []
    municipios_sucesso = []
    
    for municipio in municipios:
        try:
            navegador.get('https://demonstrativos.apps.bb.com.br/extrato')
            
            WebDriverWait(navegador, 15).until(
                EC.presence_of_element_located((By.XPATH, "//input[@formcontrolname='nomeBeneficiarioEntrada']"))
            ).send_keys(municipio)
            
            WebDriverWait(navegador, 15).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Continuar']"))
            ).click()
            
            WebDriverWait(navegador, 15).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Beneficiário']"))
            ).click()
            
            while True:
                try:
                    WebDriverWait(navegador, 15).until(
                        EC.element_to_be_clickable((By.XPATH, f"//a[@role='menuitem' and contains(., '{municipio} - MA')]"))
                    ).click()
                    break
                except StaleElementReferenceException:
                    pass
            
            WebDriverWait(navegador, 15).until(
                EC.presence_of_element_located((By.XPATH, "//input[@placeholder='MM / AAAA']"))
            ).send_keys(mes_ano)
            
            botao_conta = WebDriverWait(navegador, 15).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Conta']"))
            )
            navegador.execute_script("arguments[0].scrollIntoView(true);", botao_conta)
            navegador.execute_script("arguments[0].click();", botao_conta)
            
            WebDriverWait(navegador, 15).until(
                EC.element_to_be_clickable((By.XPATH, "//span[@class='menu-title']"))
            ).click()
            
            WebDriverWait(navegador, 15).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Continuar']"))
            ).click()
            
            try:
                WebDriverWait(navegador, 2).until(
                    EC.presence_of_element_located((By.XPATH, "//h2[contains(text(), 'Ocorreu um erro')]"))
                )
                municipios_com_erro.append(municipio)
                continue  
            except TimeoutException:
                municipios_sucesso.append(municipio)
                
                WebDriverWait(navegador, 15).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[.//bb-icon[@icon='download']]"))
                ).click()
                
                WebDriverWait(navegador, 15).until(
                    EC.element_to_be_clickable((By.XPATH, "//span[@class='menu-title' and text()='CSV']"))
                ).click()
        
        except Exception:
            municipios_com_erro.append(municipio)
            continue  

    with open(arquivo_saida, "w", encoding="utf-8") as f:
        f.write("Municípios com sucesso:\n" + "\n".join(municipios_sucesso) + "\n\n")
        f.write("Municípios com erro:\n" + "\n".join(municipios_com_erro) + "\n")
    
    print("Municípios com sucesso:", municipios_sucesso)
    print("Municípios com erro:", municipios_com_erro)

if __name__ == "__main__":
    mes_ano = input("Digite o mês e ano no formato 'MM / AAAA': ")
    municipios_maranhao = ['ACAILANDIA', 'AFONSO CUNHA', 'AGUA DOCE DO MARANHAO','ALCANTARA', 'ALDEIAS ALTAS', 'ALTAMIRA DO MARANHAO', 'ALTO ALEGRE DO MARANHAO', 'ALTO ALEGRE DO PINDARE', 'ALTO PARNAIBA', 'AMAPA DO MARANHAO', 'AMARANTE DO MARANHAO', 'ANAJATUBA', 'ANAPURUS', 'APICUM-ACU', 'ARAGUANA', 'ARAIOSES', 'ARAME', 'ARARI', 'AXIXA', 'BACABAL', 'BACABEIRA', 'BACURI', 'BACURITUBA', 'BALSAS', 'BARAO DE GRAJAU', 'BARRA DO CORDA', 'BARREIRINHAS', 'BELAGUA', 'BELA VISTA DO MARANHAO', 'BENEDITO LEITE', 'BEQUIMAO', 'BERNARDO DO MEARIM', 'BOA VISTA DO GURUPI', 'BOM JARDIM', 'BOM JESUS DAS SELVAS', 'BOM LUGAR', 'BREJO', 'BREJO DE AREIA', 'BURITI', 'BURITI BRAVO', 'BURITICUPU', 'BURITIRANA', 'CACHOEIRA GRANDE', 'CAJAPIO', 'CAJARI', 'CAMPESTRE DO MARANHAO', 'CANDIDO MENDES', 'CANTANHEDE', 'CAPINZAL DO NORTE', 'CAROLINA', 'CARUTAPERA', 'CAXIAS', 'CEDRAL', 'CENTRAL DO MARANHAO', 'CENTRO DO GUILHERME', 'CENTRO NOVO DO MARANHAO', 'CHAPADINHA', 'CIDELANDIA', 'CODO', 'COELHO NETO', 'COLINAS', 'CONCEICAO DO LAGO-ACU', 'COROATA', 'CURURUPU', 'DAVINOPOLIS', 'DOM PEDRO', 'DUQUE BACELAR', 'ESPERANTINOPOLIS', 'ESTREITO', 'FEIRA NOVA DO MARANHAO', 'FERNANDO FALCAO', 'FORMOSA DA SERRA NEGRA', 'FORTALEZA DOS NOGUEIRAS', 'FORTUNA', 'GODOFREDO VIANA', 'GONCALVES DIAS', 'GOVERNADOR ARCHER', 'GOVERNADOR EDISON LOBAO', 'GOVERNADOR EUGENIO BARROS', 'GOVERNADOR LUIZ ROCHA', 'GOVERNADOR NEWTON BELLO', 'GOVERNADOR NUNES FREIRE', 'GRACA ARANHA', 'GRAJAU', 'GUIMARAES', 'HUMBERTO DE CAMPOS', 'ICATU', 'IGARAPE DO MEIO', 'IGARAPE GRANDE', 'IMPERATRIZ', 'ITAIPAVA DO GRAJAU', 'ITAPECURU MIRIM', 'ITINGA DO MARANHAO', 'JATOBA', 'JENIPAPO DOS VIEIRAS', 'JOAO LISBOA', 'JOSELANDIA', 'JUNCO DO MARANHAO', 'LAGO DA PEDRA', 'LAGO DO JUNCO', 'LAGO VERDE', 'LAGOA DO MATO', 'LAGO DOS RODRIGUES', 'LAGOA GRANDE DO MARANHAO', 'LAJEADO NOVO', 'LIMA CAMPOS', 'LORETO', 'LUIS DOMINGUES', 'MAGALHAES DE ALMEIDA', 'MARACACUME', 'MARAJA DO SENA', 'MARANHAOZINHO', 'MATA ROMA', 'MATINHA', 'MATOES', 'MATOES DO NORTE', 'MILAGRES DO MARANHAO', 'MIRADOR', 'MIRANDA DO NORTE', 'MIRINZAL', 'MONCAO', 'MONTES ALTOS', 'MORROS', 'NINA RODRIGUES', 'NOVA COLINAS', 'NOVA IORQUE', 'NOVA OLINDA DO MARANHAO', "OLHO D'AGUA DAS CUNHAS", 'OLINDA NOVA DO MARANHAO', 'PACO DO LUMIAR', 'PALMEIRANDIA', 'PARAIBANO', 'PARNARAMA', 'PASSAGEM FRANCA', 'PASTOS BONS', 'PAULINO NEVES', 'PAULO RAMOS', 'PEDREIRAS', 'PEDRO DO ROSARIO', 'PENALVA', 'PERI MIRIM', 'PERITORO', 'PINDARE MIRIM', 'PINHEIRO', 'PIO XII', 'PIRAPEMAS', 'POCAO DE PEDRAS', 'PORTO FRANCO', 'PORTO RICO DO MARANHAO', 'PRESIDENTE DUTRA', 'PRESIDENTE JUSCELINO', 'PRESIDENTE MEDICI', 'PRESIDENTE SARNEY', 'PRESIDENTE VARGAS', 'PRIMEIRA CRUZ', 'RAPOSA', 'RIACHAO', 'RIBAMAR FIQUENE', 'ROSARIO', 'SAMBAIBA', 'SANTA FILOMENA DO MARANHAO', 'SANTA HELENA', 'SANTA INES', 'SANTA LUZIA', 'SANTA LUZIA DO PARUA', 'SANTA QUITERIA DO MARANHAO', 'SANTA RITA', 'SANTANA DO MARANHAO', 'SANTO AMARO DO MARANHAO', 'SANTO ANTONIO DOS LOPES', 'SAO BENEDITO DO RIO PRETO', 'SAO BENTO', 'SAO BERNARDO', 'SAO DOMINGOS DO AZEITAO', 'SAO DOMINGOS DO MARANHAO', 'SAO FELIX DE BALSAS', 'SAO FRANCISCO DO BREJAO', 'SAO FRANCISCO DO MARANHAO', 'SAO JOAO BATISTA', 'SAO JOAO DO CARU', 'SAO JOAO DO PARAISO', 'SAO JOAO DO SOTER', 'SAO JOAO DOS PATOS', 'SAO JOSE DE RIBAMAR', 'SAO JOSE DOS BASILIOS', 'SAO LUIS', 'SAO LUIS GONZAGA DO MARANHAO', 'SAO MATEUS DO MARANHAO', 'SAO PEDRO DA AGUA BRANCA', 'SAO PEDRO DOS CRENTES', 'SAO RAIMUNDO DAS MANGABEIRAS', 'SAO RAIMUNDO DO DOCA BEZERRA', 'SAO ROBERTO', 'SAO VICENTE FERRER', 'SATUBINHA', 'SENADOR ALEXANDRE COSTA', 'SENADOR LA ROCQUE', 'SERRANO DO MARANHAO', 'SITIO NOVO', 'SUCUPIRA DO NORTE', 'SUCUPIRA DO RIACHAO', 'TASSO FRAGOSO', 'TIMBIRAS', 'TIMON', 'TRIZIDELA DO VALE', 'TUFILANDIA', 'TUNTUM', 'TURIACU', 'TURILANDIA', 'TUTOIA', 'URBANO SANTOS', 'VARGEM GRANDE', 'VIANA', 'VILA NOVA DOS MARTIRIOS', 'VITORIA DO MEARIM', 'VITORINO FREIRE', 'ZE DOCA']
    processar_municipios(municipios_maranhao, mes_ano)
