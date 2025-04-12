# Importando/Referenciando a classe Agendamento (Appointment)
from Entities.Appointment import Appointment

# Importando a estrutura do tipo lista 
from typing import List

# Classe Cliente
class Client:
    def __init__(self, client_id: int, client_name: str, client_email: str, client_cellphone: int):
        self.client_id = client_id
        self.client_name = client_name
        self.client_email = client_email
        self.client_cellphone = client_cellphone
        self.total_price_service = 0
        self.appointment: List[Appointment] = []

    def list_empty(self) -> bool:
        return len(self.appointment) == 0

    def get_client_details(self):
        print(f"Client ID: {self.client_id} - Client: {self.client_name} - Email: {self.client_email} - Cellphone: {self.client_cellphone}")
        for appointment in self.appointment:
            print(f"--Appointment date: {appointment.service_appointment}")
            print(f"--Service: {appointment.service.service_name}")
            print(f"--Service price: ${appointment.service.price:,.2f}\n")
            

    def get_total_value(self) -> float:
        total_value = 0
        for list in self.appointment:
            total_value += list.service.price
        return total_value