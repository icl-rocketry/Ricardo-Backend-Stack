from CommandServer.commandserver import CommandServer
from cmd2 import Cmd2ArgumentParser

import time
pyro_disarm_ap = Cmd2ArgumentParser()
pyro_disarm_ap.add_argument("--destination",type=int,required=True)
pyro_disarm_ap.add_argument("--destination_service",type=int,required=True)

@CommandServer.register('pyro_disarm',argparse=pyro_disarm_ap)
def pyro_disarm(instance,args):

    command_packet_args = {"source":1,
                        "source_service":instance.source_service,
                        "destination":args['destination'],
                        "destination_service":args['destination_service'],
                        "command_id":4,
                        "command_arg":0}

    instance.send_command_packet(command_packet_args)
