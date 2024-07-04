from CommandServer.commandserver import CommandServer
import time

@CommandServer.register('ereg_close')
def ereg_close(instance,args):

    command_packet_args = {"source":1,
                        "source_service":instance.source_service,
                        "destination":108,
                        "destination_service":10,
                        "command_id":2,
                        "command_arg":2}

    instance.send_command_packet(command_packet_args)

