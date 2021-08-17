import os

from obsei.configuration import ObseiConfiguration

# Read workflow config file
current_path = os.path.dirname(os.path.realpath(__file__))
filename = "workflow.yml"
obsei_configuration = ObseiConfiguration(
     config_path=current_path,
     config_filename=filename
)

# Initialize Observer based on workflow
source_config = obsei_configuration.initialize_instance("source_config")
source = obsei_configuration.initialize_instance("source")

# Initialize Analyzer based on workflow
analyzer = obsei_configuration.initialize_instance("analyzer")
analyzer_config = obsei_configuration.initialize_instance("analyzer_config")

# Initialize Informer based on workflow
sink_config = obsei_configuration.initialize_instance("sink_config")
sink = obsei_configuration.initialize_instance("sink")

# Execute Observer to fetch result
source_response_list = source.lookup(source_config)

# Execute Analyzer to perform analysis on Observer's output with given analyzer config
analyzer_response_list = analyzer.analyze_input(
     source_response_list=source_response_list, analyzer_config=analyzer_config
)

# Send analyzed result to Informer
sink_response_list = sink.send_data(analyzer_response_list, sink_config)
