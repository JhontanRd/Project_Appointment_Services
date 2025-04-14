# Importando/Referenciando a classe Servico (Service)
from Entities.Service import Service

# Importando o módulo datetime para trabalhar com datas
from datetime import datetime

# Classe Agendamento
class Appointment:
    def __init__(self, service: Service, date: str):
        self.service_appointment = date
        self.service = service
  
    def convert_str_to_datetime(self, date: str) -> datetime:
        new_date = datetime.strptime(date, "%d/%m/%Y %H:%M")
        return new_date
