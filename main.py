
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

def list_clients():
    global clientes
    print(clientes)

def _print_welcome():
    print('WELCOME TO PLATZI VENTAS')
    print('*' * 50)
    print('What would you like to do today')
    print('[C]reate client')
    print('[D]elete client')

if __name__ == '__main__':
    list_clients()
    _print_welcome()
    command = input()
    if command == 'c' or command == 'C':
        client_name = input('What is the cient name?')
        create_client(client_name)
        list_clients()
    elif command == 'd' or command == 'D':
        pass
    else:
        print('El comando es invalido')
    


