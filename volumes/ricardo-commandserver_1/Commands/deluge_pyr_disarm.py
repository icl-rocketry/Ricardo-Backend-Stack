from CommandServer.commandserver import CommandServer
import time

@CommandServer.register('deluge_pyr_disarm')
def deluge_pyr_disarm(instance,args):

    command_packet_args = {"source":1,
                        "source_service":instance.source_service,
                        "destination":107,
                        "destination_service":13,
                        "command_id":4,
                        "command_arg":0}

    instance.send_command_packet(command_packet_args)