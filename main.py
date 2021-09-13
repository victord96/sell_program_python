import sys


clients = [
    {
        'name': 'Pablo',
        'company': 'Google',
        'email': 'pablo@google.com',
        'position': 'Software engineer',
    },
    {
        'name': 'Ricardo',
        'company': 'Facebook',
        'email': 'ricardo@facebook.com',
        'position': 'Data engineer',
    }
]

def search_id():

    client_id = int(_get_client_field('id'))

    if len(clients) -1 >= client_id:
        return client_id


def create_client(client):
    if client not in clients:
        clients.append(client)
    else:
        print('Client already is in the client\'s list') 


def fill_client():

    client = {
            'name': _get_client_field('name'),
            'company': _get_client_field('company'),
            'email': _get_client_field('email'),
            'position': _get_client_field('position'),
        }

    return client


def show_client(idx, client):

    print('{uid} | {name} | {company} | {email} | {position}'.format(
                uid = idx,
                name = client['name'],
                company = client['company'],
                email = client['email'],
                position = client['position']
        ))


def update_client():
    id = search_id()

    if id != None:
        client = fill_client()
        clients[id] = client
    else:
        _client_not_found()


def delete_client():
    id = search_id()

    if id != None:
        clients.remove(clients[id])
    else:
        _client_not_found()


def search_client():
    id = search_id()
    
    if id != None:
        for idx,client in enumerate(clients):
            if idx == id:
                show_client(idx, client)

    else:    
        print(f'The client is not in our client\s list')          


def _client_not_found():
	return print('Client id isn´t exist')


def list_clients():
    for idx,client in enumerate(clients):
        show_client(idx, client)


def _print_welcome():
    print('WELCOME TO MY SELL PROGRAM')
    print('*' * 50)
    print('What would you like to do today?')
    print('[C]reate client')
    print('[L]ist clients')
    print('[U]pdate Client')
    print('[D]elete client')
    print('[S]earch client')


def _get_client_field(field_name):
    field = None

    while not field:
        field = input(f'What is the client {field_name}? ')
    return field

def _get_client_name():
    client_name = None

    while not client_name:
        client_name = input('What is the client name? ').strip()

        if client_name == 'exit':
            client_name = None
            break

    if not client_name:
        sys.exit()

    return client_name


if __name__ == '__main__':
    _print_welcome()

    command = input()
    command = command.upper()

    if command == 'C':
        client = fill_client()
        create_client(client)
        list_clients()

    elif command == 'L':
        list_clients()    

    elif command == 'U':
        update_client()
        list_clients()
        
    elif command == 'D':
        delete_client()
        list_clients()

    elif command == 'S':
        search_client()

    else:
        print('Invalid command')