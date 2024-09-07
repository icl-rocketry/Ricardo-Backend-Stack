from CommandServer.commandserver import CommandServer
from cmd2 import Cmd2ArgumentParser

import time

ereg_arm_ap = Cmd2ArgumentParser()

@CommandServer.register('ereg_arm',argparse=ereg_arm_ap)
def ereg_arm(instance,args):

    command_packet_args = {"source":1,
                        "source_service":instance.source_service,
                        "destination":7,
                        "destination_service":10,
                        "command_id":3,
                        "command_arg":1}

    instance.send_command_packet(command_packet_args)
