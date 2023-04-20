import os
import warnings
from file.xml_reader import XmlReader
from util.clear import clear

warnings.filterwarnings("ignore")

os.system('pip install -r requirements.txt')

home_directory = os.path.expanduser( '~' )
clear()

from core.environment_executor import EnvironmentExecutor
from provider.impl.health_check_request_xml_provider import HealthCheckRequestXmlProvider

executor = EnvironmentExecutor(HealthCheckRequestXmlProvider())
executor.execute()