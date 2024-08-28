url ="bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"

print(url)

indice_fatiamento = url.find('?')
url_base = url[0:indice_fatiamento]
print(url_base)


url_parametros = url[indice_fatiamento+1:]
print(url_parametros)

parametro_busca = 'moedaOrigem'
indice_fatiamento = url_parametros.find(parametro_busca)

print(indice_fatiamento)

indice_valor = 


