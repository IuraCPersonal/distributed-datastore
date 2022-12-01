import time
import requests
import random

from app.modules import SERVER_DATA, SERVERS_LIST, CLUSTER, NAME


class ManageCluster:

    @staticmethod
    def dist_data(datastore):
        if SERVER_DATA['is_leader']:
            content = datastore.copy()

            # Split data in chunks of 75%.
            first_half = dict(list(content.items())[:int(len(content)//1.32)])
            second_half = dict(list(content.items())[int(len(content)//1.32):])

            length = len(SERVERS_LIST)
            subteam = [0] * length + [1] * length
            
            random.shuffle(subteam)

            for index, node in enumerate(SERVERS_LIST):
                if node != NAME:
                    # Distributed storage logic implemented.
                    try:
                        _ = requests.post(
                            url=f'http://server-{node}:{CLUSTER[node]["http"]}/',
                            json= first_half if subteam[index] else second_half
                        )
                    except TypeError:
                        pass

                    time.sleep(1)

            print("Data Distributed...")