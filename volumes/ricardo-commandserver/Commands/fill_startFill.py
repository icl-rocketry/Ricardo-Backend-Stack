from CommandServer.commandserver import CommandServer
from cmd2 import Cmd2ArgumentParser

import time

fill_startFill_ap = Cmd2ArgumentParser()


@CommandServer.register('fill_startFill',argparse=fill_startFill_ap)
def fill_startFill(instance,args):

    command_packet_args = {"source":1,
                        "source_service":instance.source_service,
                        "destination":0,
                        "destination_service":2,
                        "command_id":250,
                        "command_arg":1}

    instance.send_command_packet(command_packet_args)

    time.sleep(0.5)

    command_packet_args = {"source":1,
                        "source_service":instance.source_service,
                        "destination":0,
                        "destination_service":2,
                        "command_id":250,
                        "command_arg":1}
                    
    instance.send_command_packet(command_packet_args)
