from CommandServer.commandserver import CommandServer
from cmd2 import Cmd2ArgumentParser
import time

pdu_toready_ap = Cmd2ArgumentParser()
pdu_toready_ap.add_argument("--destination",type=int,required=True)
@CommandServer.register('pdu_toready',argparse=pdu_toready_ap)
def pdu_toready(instance,args):

    command_packet_args = {"source":1,
                        "source_service":instance.source_service,
                        "destination":args['destination'],
                        "destination_service":2,
                        "command_id":1,
                        "command_arg":0}

    instance.send_command_packet(command_packet_args)