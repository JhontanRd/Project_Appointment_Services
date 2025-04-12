# Importando/Referenciando a classe Prestador (Service_Provider)
from Entities.Service_Provider import Service_Provider

# Classe Serviço
class Service:
    def __init__(self, service_name: str, price: float, service_provider: Service_Provider):
        self.service_name = service_name
        self.price = price
        self.service_provider = service_provider