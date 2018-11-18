import platform

# Com o módulo platform é possível obter características do processador, como nome e modelo. Aém disso, estão disponíveis informações sobre o sistema operacional

print(platform.processor()) #retorna o nome do processador associado à quantidade de bits que ele trabalha (32 bits ou 64 bits, normalmente).

print(platform.node()) #indica o nome do computador na rede

print(platform.platform()) #maiores detalhes sobre o sistema operacional

print(platform.system()) # indica o nome do sistema operacional