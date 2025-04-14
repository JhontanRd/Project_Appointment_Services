# Importando as classes necessarias para o projeto
from Entities.Client import Client
from Entities.Service_Provider import Service_Provider
from Entities.Service import Service
from Entities.Appointment import Appointment
from datetime import datetime

# Projeto principal (main)
def main():
    print("Management System of Service's Appointment\n")

    # Dicionario para guardar os clientes com uma identificação 
    clients_list: dict[int, Client] = {}

    option = 1
    while option > 0 and option < 4:

        option = int(input("To add a new client press......(1)\n"
                            "To add a new service press.....(2)\n"
                            "To list appointments press.....(3)\n"
                            "To exit of system press........(4)\n"
                            "Choose your option: "))
        
        # Função de cadastrar clientes caso seja escolhido a opção 1
        if option == 1:
            quantity = int(input("\nHow many clients will be added: "))
            print()

            for i in range(1, quantity + 1):
                print(f"DATA FROM CLIENT: #{i}")
                client_id = int(input("Enter with a client ID: ")) # Vou colocar esse dado como atributo da classe cliente
                client_name = str(input("Enter with your name: "))
                client_email = str(input("Enter with your email: "))
                client_cellphone = int(input("Enter with your cellphone number (only numbers): "))

                # Intanciando o objeto Cliente
                new_client = Client(client_id, client_name, client_email, client_cellphone)

                if len(clients_list) != 0:

                    # Verificando se a lista esta vazia 
                    for id, my_client in clients_list.items():

                        # Verificando se o ID do cliente ja existe para nao sobrepor um cliente ja existente
                        if my_client.client_id != client_id:
                            clients_list[client_id] = new_client
                            print("\n*\u2705 NEW CLIENT ADDED!*\n")
                            break
                        else:
                            print("\n*\u274C [ERROR]* This client ID already exists and was not added. Please enter a different ID.\n")
                            break
                else:
                    clients_list[client_id] = new_client
                    print("\n*\u2705 NEW CLIENT ADDED!*\n")
                        
        # Função de fazer agendamentos caso seja escolhido a opção 1
        elif option == 2:
            print("\nCLIENTS LIST:\n")

            # Listagem do Cliente + ID
            for client_id, client in clients_list.items():
                print(f"Client ID: {client.client_id} - Client name: {client.client_name}")
            
            search_id = int(input("\nEnter the client ID that is requesting a service: "))

            if search_id in clients_list:
                client = clients_list[search_id]
                quantity = int(input("How many services will be added: "))
                print()

                for i in range(1, quantity + 1):
                    print(f"DATA FROM SERVICE: #{i}")
                    service_name = str(input("Enter with service name: "))
                    price = float(input("Enter with service price: "))
                    service_provider_name = str(input("Enter with service provider name: "))
                    service_provider_cellphone = int(input("Enter with service provider cellphone: "))

                    # Instanciando Prestador do serviço
                    new_service_provider = Service_Provider(service_provider_name, service_provider_cellphone)

                    # Instanciando o Serviço
                    new_service = Service(service_name, price, new_service_provider)
                    appointment_date = str(input("Enter with date of appointment service (DD/MM/YYYY HH:MM): "))
                    appointment_date = datetime.strptime(appointment_date, "%d/%m/%Y %H:%M")

                    if len(clients_list) != 0:
                        # Verificando se a lista esta vazia 
                        for id, my_client in clients_list.items():
                            if my_client.get_appoinments(appointment_date) == False:
                                new_appointment = Appointment(new_service, appointment_date)
                                client.appointment.append(new_appointment)
                                print("\n*\u2705 APPOINTMENT AND SERVICE ADDED!*\n")
                                break
                            else:
                                print("\n*\u274C [ERROR] This ID already ocupped, the client is not added.*\n")
                                break
                    else:
                        # Instanciando o Agendamento
                        new_appointment = Appointment(new_service, appointment_date)
                        
                        # Adiciona o Agendamento ao client
                        client.appointment.append(new_appointment)
                        print("\n*\u2705 APPOINTMENT AND SERVICE ADDED!*\n")
            else:
                print("\n*\u274C [ERROR]* Client not found.")
            
        # Função de listar os agendamentos caso seja escolhido a opção 3
        elif option == 3:
            print("\nLIST OF CLIENTS AND APPOINTMENTS:")
            for client_id, client in clients_list.items():
                client.get_client_details()
                total_price = client.get_total_value()
                print(f"Total value: ${total_price:,.2f}")
                print("==========================\n")
        else:
            # Caso o usuario digite 4 ou algum outro numero maior que 4 o sistema se encerra.
            option = 5
            print("\n\nEnd of system.\n")


# Run do sistema
if __name__ == "__main__":
    main()