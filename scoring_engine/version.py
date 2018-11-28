import os

from scoring_engine.config import config


version = "0.1.0"

# If we're in debug mode, just say dev
if config.web_debug is True:
    version = 'dev'

# If we specify the version specifically then use that one
if 'SCORINGENGINE_VERSION' in os.environ:
    version = os.environ['SCORINGENGINE_VERSION']
