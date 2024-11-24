from CommandServer.commandserver import CommandServer
from cmd2 import Cmd2ArgumentParser

import time

hotfire_startTest_ap = Cmd2ArgumentParser()


@CommandServer.register('hotfire_startTest',argparse=hotfire_startTest_ap)
def hotfire_startTest(instance,args):

    command_packet_args = {"source":1,
                        "source_service":instance.source_service,
                        "destination":10,
                        "destination_service":10,
                        "command_id":2,
                        "command_arg":1}

    instance.send_command_packet(command_packet_args)

    time.sleep(0.5)

    command_packet_args = {"source":1,
                        "source_service":instance.source_service,
                        "destination":13,
                        "destination_service":10,
                        "command_id":2,
                        "command_arg":1}
                    
    instance.send_command_packet(command_packet_args)
