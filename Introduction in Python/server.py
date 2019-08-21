# создание сокета, сервер
# host = "127.0.0.1"
# port = 8888
def run_server(host, port):

    import asyncio
    
    storage = {}

    def check_time(key, new_time):
        for index, item in enumerate(storage[key]):
            time, value = item

            if time == new_time:
                storage[key].pop(index)



    class ClientServerProtocol(asyncio.Protocol):
        def __init__(self):
            super().__init__()
            self.error_text = 'error\nwrong command\n\n'
            self.success_text = 'ok\n\n'

        @staticmethod
        def join_get(item, key):
            return '\n'.join([f'{key} {value} {time}' for (time, value) in item]) + '\n'

        def connection_made(self, transport):
            peer_name = transport.get_extra_info('peername')
            print('Connection from {}'.format(peer_name))
            self.transport = transport

        def data_received(self, data):
            resp = self.process_data(data.decode('utf8'))
            self.transport.write(resp.encode('utf8'))

        def process_data(self, data):
            if data.startswith('put'):
                return self.put_data(data)
            elif data.startswith('get'):
                return self.get_data(data)
            else:
                return self.error_text
        def clean_get(self,str):
            return str.replace('get ','').replace('\n','')

        def clean_put(self,str):
            return list(filter(None,str.replace('put ','').split('\n')))

        def get_data(self, key):
            key = self.clean_get(key)
            result = ''
            if key == '*':
                for key, value in storage.items():
                    result += self.join_get(value, key)
            elif key not in storage:
                return self.success_text
            else:
                result = self.join_get(storage[key], key)
            return 'ok\n'+result + '\n'

        def put_data(self, data):
            items = self.clean_put(data)
            for item in items:
                key, value, time = item.split(' ')
                if key in storage:
                    check_time(key, time)
                    storage[key].append((time,value))
                else:
                    storage[key] = [(time, value)]

            return self.success_text



    loop = asyncio.get_event_loop()
    coro = loop.create_server(
        ClientServerProtocol,
        host, port
    )

    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()

# run_server(host, port)