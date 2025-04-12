# Importando/Referenciando a classe Servico (Service)
from Entities.Service import Service

# Importando o módulo datetime para trabalhar com datas
from datetime import datetime

# Classe Agendamento
class Appointment:
    def __init__(self, service: Service):
        self.service_appointment = None
        self.service = service

    def is_disponible(self, appointment_date: datetime) -> bool:
        for client in clients:
            for appointment in client.appointment:
                if appointment.service_appointment == appointment_date:
                    return False  # Já tem agendamento com essa data
        return True  # Nenhum cliente tem essa data ocupada
    
    def convert_str_to_datetime(self, date) -> datetime:
        new_date = datetime.strptime(date, "%d/%m/%Y %H:%M")
        return new_date
