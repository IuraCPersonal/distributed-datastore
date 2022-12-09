import time
import requests

from app.modules import *
from threading import Thread


# Extend the Thread class to create Threads for the Manager.
class Manager(Thread):
    def __init__(self, manager_name, *args, **kwargs):
        super(Manager, self).__init__(name=f'Manager-{manager_name}', *args, **kwargs)
        self.manager_name = manager_name


    # Overide the run() method of the Thread class.
    def run(self) -> None:
        while True:
            time.sleep(60)
            for node in SERVERS_LIST:
                time.sleep(5)
                try:
                    if node != NAME:
                        port = CLUSTER.get(str(node)).get('http')
                        url = f'http://server-{node}:{port}'

                        response = requests.get(
                            url=url
                        ).json()

                        self.__update_datastore(response)

                        _ = requests.post(
                            url=url,
                            json=response
                        )

                        print('[SYNC]: STATUS DONE')
                except ValueError:
                    pass
    

    def __update_datastore(self, response_datastore):
        for key, value in datastore.items():
            if key in response_datastore.keys():
                response_datastore.update({key: value})