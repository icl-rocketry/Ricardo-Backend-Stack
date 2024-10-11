from CommandServer.commandserver import CommandServer
from cmd2 import Cmd2ArgumentParser
import time

payload_dep_compound_reset_ap = Cmd2ArgumentParser()
payload_dep_compound_reset_ap.add_argument("--destination",type=int,required=True)

@CommandServer.register('payload_dep_compound_reset',argparse=payload_dep_compound_reset_ap)
def payload_dep_compound_reset(instance,args):

    command_packet_args = {"source":1,
                        "source_service":instance.source_service,
                        "destination":args['destination'],
                        "destination_service":10,
                        "command_id":2,
                        "command_arg":0}

    instance.send_command_packet(command_packet_args)

    time.sleep(0.001)
    command_packet_args['destination_service'] = 11
    command_packet_args['command_arg'] = 180

    instance.send_command_packet(command_packet_args)