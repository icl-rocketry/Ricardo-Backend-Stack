from CommandServer.commandserver import CommandServer
from cmd2 import Cmd2ArgumentParser

import time

canard_arm_ap = Cmd2ArgumentParser()

canard_arm_ap.add_argument("--destination",type=int,required=True)
@CommandServer.register('canard_arm',argparse=canard_arm_ap)


def canard_arm(instance,args):

    command_packet_args = {"source":1,
                        "source_service":instance.source_service,
                        "destination":args['destination'],
                        "destination_service":10,
                        "command_id":3,
                        "command_arg":1}

    instance.send_command_packet(command_packet_args)
