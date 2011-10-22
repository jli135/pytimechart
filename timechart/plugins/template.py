from timechart.plugin import *
from timechart import colors
from timechart.model import tcProcess

# to use with start_spi.sh
class template(plugin):
    additional_colors = """
template_bg		      #80ff80
"""
    additional_ftrace_parsers = [
        ]
    additional_process_types = {
            "template":(tcProcess, MISC_TRACES_CLASS),
        }
    @staticmethod
    def do_function_my_start_function(proj,event):
        """This method will be called when the function "my_start_function" appears in the trace
        in this example, we start a process, and mark its caller as waked it
        """
        process = proj.generic_find_process(0,"template","template")
        caller = proj.generic_find_process(0,event.caller,"template")
        proj.generic_process_start(process,event)

        proj.generic_process_single_event(caller,event)
        proj.generic_add_wake(caller, process,event)

    @staticmethod
    def do_function_my_stop_function(proj,event):
        """This method will be called when the function "my_stop_function" appears in the trace
        in this example, we stop the "template" process
        """
        process = proj.generic_find_process(0,"template","template")
        proj.generic_process_stop(prev,event)

# this plugin is disabled... uncomment to enable it.
#plugin_register(template)
