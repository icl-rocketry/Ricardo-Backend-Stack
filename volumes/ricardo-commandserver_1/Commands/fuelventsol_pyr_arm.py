from CommandServer.commandserver import CommandServer
import time

@CommandServer.register('fuelventsol_pyr_arm')
def fuelventsol_pyr_arm(instance,args):

    command_packet_args = {"source":1,
                        "source_service":instance.source_service,
                        "destination":107,
                        "destination_service":11,
                        "command_id":3,
                        "command_arg":0}

    instance.send_command_packet(command_packet_args)