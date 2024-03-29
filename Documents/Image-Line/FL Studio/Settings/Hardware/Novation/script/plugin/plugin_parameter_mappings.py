from script.plugin.native_plugin_parameter_mappings import native_plugin_parameter_mappings
from script.plugin.plugin_parameter_mapping_dictionary import PluginParameterMappingDictionary
from script.plugin.user_plugin_parameter_mappings import user_plugin_parameter_mappings

__all__ = ["plugin_parameter_mappings"]

plugin_parameter_mappings = PluginParameterMappingDictionary(
    native_plugin_parameter_mappings | user_plugin_parameter_mappings
)
