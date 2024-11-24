from CommandServer.commandserver import CommandServer
from cmd2 import Cmd2ArgumentParser

import time

hotfire_abortTest_ap = Cmd2ArgumentParser()


@CommandServer.register('hotfire_abortTest',argparse=hotfire_abortTest_ap)
def hotfire_abortTest(instance,args):

    command_packet_args = {"source":1,
                        "source_service":instance.source_service,
                        "destination":10,
                        "destination_service":10,
                        "command_id":2,
                        "command_arg":2}

    instance.send_command_packet(command_packet_args)

    time.sleep(0.05)

    command_packet_args = {"source":1,
                        "source_service":instance.source_service,
                        "destination":13,
                        "destination_service":10,
                        "command_id":2,
                        "command_arg":2}
                    
    instance.send_command_packet(command_packet_args)
