# encoding: utf-8

from ckan.plugins import implements, SingletonPlugin
from ckan.plugins import IConfigurer
import ckan.plugins.toolkit as toolkit
import os

class OpencityPlugin(SingletonPlugin):
    implements(IConfigurer)

    def update_config(self, config_):
        # Get root directory of the plugin
        root_path = os.path.dirname(__file__)

        # Add public and template folders
        toolkit.add_template_directory(config_, os.path.join(root_path, 'templates'))
        toolkit.add_public_directory(config_, os.path.join(root_path, 'public'))