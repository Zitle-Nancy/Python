
clientes = 'pablo, ricardo,'

def create_client(client_name):
    global clientes
    clientes += client_name
    _add_comma()

def _add_comma():
    global clientes
    clientes +=','

def list_clients():
    global clientes
    print(clientes)


if __name__ == '__main__':
    list_clients()

    create_client('yo')
		
    list_clients()


