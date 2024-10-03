from CommandServer.commandserver import CommandServer
import time

@CommandServer.register('pickle_ignition')
def pickle_ignition(instance,args):

    command_packet_args = {"source":1,
                        "source_service":instance.source_service,
                        "destination":2,
                        "destination_service":2,
                        "command_id":69,
                        "command_arg":0}

    instance.send_command_packet(command_packet_args)