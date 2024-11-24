from CommandServer.commandserver import CommandServer
from cmd2 import Cmd2ArgumentParser

import time

pyro_arm_ap = Cmd2ArgumentParser()
pyro_arm_ap.add_argument("--destination",type=int,required=True)
pyro_arm_ap.add_argument("--destination_service",type=int,required=True)

@CommandServer.register('pyro_arm',argparse=pyro_arm_ap)
def pyro_arm(instance,args):

    command_packet_args = {"source":1,
                        "source_service":instance.source_service,
                        "destination":args['destination'],
                        "destination_service":args['destination_service'],
                        "command_id":3,
                        "command_arg":1}

    instance.send_command_packet(command_packet_args)
