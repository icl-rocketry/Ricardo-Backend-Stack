from CommandServer.commandserver import CommandServer
from cmd2 import Cmd2ArgumentParser

import time

toothless_arm_ap = Cmd2ArgumentParser()
toothless_arm_ap.add_argument("--argument",type=int,required=True)

@CommandServer.register('toothless_arm',argparse=toothless_arm_ap)
def toothless_arm(instance,args):

    command_packet_args = {
        "source":1,
        "source_service":instance.source_service,
        "destination":10,
        "destination_service":10,
        "command_id":3,
        "command_arg":args['argument'],
    }

    instance.send_command_packet(command_packet_args)
