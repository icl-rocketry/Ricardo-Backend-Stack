from CommandServer.commandserver import CommandServer
from cmd2 import Cmd2ArgumentParser

import time

toothless_disarm_ap = Cmd2ArgumentParser()

@CommandServer.register('toothless_disarm',argparse=toothless_disarm_ap)
def toothless_disarm(instance,args):

    command_packet_args = {"source":1,
                        "source_service":instance.source_service,
                        "destination":10,
                        "destination_service":10,
                        "command_id":4,
                        "command_arg":0}

    instance.send_command_packet(command_packet_args)
