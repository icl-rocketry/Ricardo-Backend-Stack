from CommandServer.commandserver import CommandServer
from cmd2 import Cmd2ArgumentParser
import time

pdu_golive_ap = Cmd2ArgumentParser()
pdu_golive_ap.add_argument("--destination",type=int,required=True)
@CommandServer.register('pdu_golive',argparse=pdu_golive_ap)
def pdu_golive(instance,args):

    command_packet_args = {"source":1,
                        "source_service":instance.source_service,
                        "destination":args['destination'],
                        "destination_service":2,
                        "command_id":2,
                        "command_arg":0}

    instance.send_command_packet(command_packet_args)