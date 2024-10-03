from CommandServer.commandserver import CommandServer
from cmd2 import Cmd2ArgumentParser

import time

canard_wiggle_ap = Cmd2ArgumentParser()
canard_wiggle_ap.add_argument("--destination",type=int,required=True)

@CommandServer.register('canard_wiggle',argparse=canard_wiggle_ap)
def canard_wiggle(instance,args):

    command_packet_args = {"source":1,
                        "source_service":instance.source_service,
                        "destination":args['destination'],
                        "destination_service":10,
                        "command_id":6,
                        "command_arg":0}

    instance.send_command_packet(command_packet_args)

