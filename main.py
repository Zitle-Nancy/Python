
clientes = 'pablo, ricardo,'

def create_client(client_name):
    global clientes
    if client_name not in clientes:
        clientes += client_name
        _add_comma()
    else:
        print('Client alredy is in the client\'s list')

def _add_comma():
    global clientes
    clientes +=','

def get_client_name():
    return input('What is the cient name? ')

def list_clients():
    global clientes
    print(clientes)

def update_client(client_name, update_client_name):
    global clientes
    if client_name in clientes:
        clientes = clientes.replace(client_name + ',', update_client_name + ',')
    else:
        print('Client is not in clients list')
    


def _print_welcome():
    print('WELCOME TO PLATZI VENTAS')
    print('*' * 50)
    print('What would you like to do today? ')
    print('[C]reate client')
    print('[U]pdate client')
    print('[D]elete client')

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
        pass
    elif command == 'U':
        client_name = get_client_name()
        update_client_name = input('What is the update client name? ')
        update_client(client_name, update_client_name)
        list_clients()
    else:
        print('El comando es invalido')
    


