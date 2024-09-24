from CommandServer.commandserver import CommandServer
from cmd2 import Cmd2ArgumentParser
import time

pdu_compound_golive_ap = Cmd2ArgumentParser()
pdu_compound_golive_ap.add_argument("--destination0",type=int,required=True)
pdu_compound_golive_ap.add_argument("--destination1",type=int,required=True)
@CommandServer.register('pdu_compound_golive',argparse=pdu_compound_golive_ap)
def pdu_compound_golive(instance,args):

    command_packet_args = {"source":1,
                        "source_service":instance.source_service,
                        "destination":args['destination0'],
                        "destination_service":2,
                        "command_id":2,
                        "command_arg":0}

    instance.send_command_packet(command_packet_args)

    time.sleep(0.001)
    command_packet_args['destination'] = args['destination1']

    instance.send_command_packet(command_packet_args)