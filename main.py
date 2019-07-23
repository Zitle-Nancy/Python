
clientes = 'pablo,ricardo,'

def create_client(client_name):
    global clientes
    if client_name not in clientes:
        clientes += client_name
        _add_comma()
    else:
        print('Wii Client alredy is in the client\'s list')

def _add_comma():
    global clientes
    clientes +=','

def get_client_name():
    return input('What is the client name? ')

def message_client_not_found():
    print('Client is not in clients list')

def list_clients():
    global clientes
    print(clientes)

def update_client(client_name):
    global clientes
    if client_name in clientes:
        update_client_name = input('What is the update client name? ')
        clientes = clientes.replace(client_name + ',', update_client_name + ',')
    else:
        message_client_not_found()

def delete_client(client_name):
    global clientes
    if client_name in clientes:
        clientes = clientes.replace(client_name + ',', '')
    else:
        message_client_not_found()


def search_client(client_name):
    global clientes

    clients_list = clientes.split(',')

    for client in clients_list:
        if client != client_name:
            continue
        else:
            return True


def _print_welcome():
    print('WELCOME TO PLATZI VENTAS')
    print('*' * 50)
    print('What would you like to do today? ')
    print('[C]reate client')
    print('[L]ist client')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')

if __name__ == '__main__':
    list_clients()
    _print_welcome()

    command = input()
    command = command.upper()

    if command == 'c' or command == 'C':
        client_name = get_client_name()
        create_client(client_name)
        list_clients()
    elif command == 'd' or command == 'D':
        client_name = get_client_name()
        delete_client(client_name)
        list_clients()
    elif command == 'U':
        client_name = get_client_name()
        update_client(client_name)
        list_clients()
    elif command == 'L' or command == 'l':
        list_clients()
    elif command == 'S' or command =='s':
        client_name = get_client_name()
        isExist = search_client(client_name)
        
        if isExist:
            print('The client is in the client\'s list')
        else:
            print('The client: {} is not our client\'s list'.format(client_name))
    else:
        print('El comando es invalido')
    


