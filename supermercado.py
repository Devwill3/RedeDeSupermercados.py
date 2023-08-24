# A rede de suprermercados União inalgurou 4 novos supermercados em 4 bairros diferentes. Agora, precisamos saber qual o tamanho dos novos supermercados, bairro, CEP  e dia de inalguração.

# LARGURA EM METROS E LARGURA
largura = 250
comprimento = 235

# NOMES DAS RUAS 

ruas = {
    "rua calango verde" : 135,
    "rua calango azul" : 161,
    "rua calango branco" : 140,
    "rua calango amarelo" : 111
}
# CEP DAS RUAS
ceps = [
    69300-000,
    69240-000,
    69222-000,
    67215-123
]

# DATA DE INALGURAÇÃO
datas = [
    "01/06/2023",
    "07/06/2023",
    "14/06/2023",
    "21//06/2023"

] 

def multiplica(largura, comprimento):
    resultado = largura * comprimento
    return resultado
resultadoDoMetro = (largura * comprimento)

print(f"Olá! Aqui está o formulário com as informações dos novos supermercados. Cada supermercado tem uma largura de: {largura} e comprimento de:{comprimento}  que no total dão {resultadoDoMetro}m2; as ruas são  essas: {ruas}, os ceps das ruas {ceps} e suas datas de inalgurção {datas}.")

