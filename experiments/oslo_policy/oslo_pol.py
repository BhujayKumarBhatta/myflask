 from oslo_config import cfg
 from oslo_policy import policy
 from sahara.common import policies
 
CONF = cfg.CONF

CONF(['--config-file', '/etc/sahara/sahara.conf'])  
CONF.list_all_sections()
#['DEFAULT', 'database', 'keystone_authtoken', 'object_store_access', 'oslo_messaging_notifications', 'oslo_messaging_rabbit', 'oslo_policy', 'profiler']
ENFORCER = policy.Enforcer(CONF)
ENFORCER
dir(ENFORCER)
#['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_cycle_check', '_file_cache', '_get_policy_path', '_informed_no_policy_file', '_is_directory_updated', '_load_policy_file', '_loaded_files', '_policy_dir_mtimes', '_record_file_rules', '_undefined_check', '_walk_through_policy_directory', 'authorize', 'check_rules', 'clear', 'conf', 'default_rule', 'enforce', 'file_rules', 'load_rules', 'overwrite', 'policy_file', 'policy_path', 'register_default', 'register_defaults', 'registered_rules', 'rules', 'set_rules', 'use_conf']
e = ENFORCER
e.policy_file
e.load_rules() 
e.rules
rls = e.rules
r = rls.get('data-processing:clusters:get_all')

ru = policy.Rules.load('"data-processing:job-types:get_all": ""')
ru
{'data-processing:job-types:get_all': <oslo_policy._checks.TrueCheck object at 0x7f0fd5054750>}


'''
e.rules is a dictionary and r is an object
'''
{u'data-processing:jobs:get_all': <oslo_policy._checks.TrueCheck object at 0x7f0fd50547d0>, u'data-processing:clusters:modify': <oslo_policy._checks.TrueCheck object at 0x7f0fd5054b10>, u'data-processing:images:register': <oslo_policy._checks.TrueCheck object at 0x7f0fd5054850>, u'data-processing:plugins:patch': <oslo_policy._checks.RoleCheck object at 0x7f0fd5054910>, u'data-processing:job-binaries:create': <oslo_policy._checks.TrueCheck object at 0x7f0fd5054890>, u'data-processing:node-group-templates:modify': <oslo_policy._checks.TrueCheck object at 0x7f0fd50548d0>, u'data-processing:job-executions:modify': <oslo_policy._checks.TrueCheck object at 0x7f0fd5054950>, u'data-processing:job-types:get_all': <oslo_policy._checks.TrueCheck object at 0x7f0fd5054990>, u'data-processing:plugins:get': <oslo_policy._checks.TrueCheck object at 0x7f0fd50549d0>, u'data-processing:cluster-templates:create': <oslo_policy._checks.TrueCheck object at 0x7f0fd5054a10>, u'data-processing:job-binaries:delete': <oslo_policy._checks.TrueCheck object at 0x7f0fd5054a50>, u'data-processing:plugins:get_version': <oslo_policy._checks.TrueCheck object at 0x7f0fd5054a90>, u'data-processing:cluster-templates:get_all': <oslo_policy._checks.TrueCheck object at 0x7f0fd5054ad0>, u'data-processing:job-binaries:modify': <oslo_policy._checks.TrueCheck object at 0x7f0fd5054c90>, 
u'data-processing:clusters:get': <oslo_policy._checks.TrueCheck object at 0x7f0fd5063290>, u'data-processing:job-binary-internals:get_all': <oslo_policy._checks.TrueCheck object at 0x7f0fd5054b90>, u'data-processing:job-executions:delete': <oslo_policy._checks.TrueCheck object at 0x7f0fd5054bd0>, u'data-processing:job-binary-internals:create': <oslo_policy._checks.TrueCheck object at 0x7f0fd5054c10>, u'data-processing:job-executions:cancel': <oslo_policy._checks.TrueCheck object at 0x7f0fd5054c50>, u'data-processing:images:add_tags': <oslo_policy._checks.TrueCheck object at 0x7f0fd5054810>, u'data-processing:job-binaries:get_all': <oslo_policy._checks.TrueCheck object at 0x7f0fd5054cd0>, u'data-processing:clusters:create': <oslo_policy._checks.TrueCheck object at 0x7f0fd5054d10>, u'data-processing:node-group-templates:delete': <oslo_policy._checks.TrueCheck object at 0x7f0fd5054d50>, u'data-processing:clusters:scale': <oslo_policy._checks.TrueCheck object at 0x7f0fd5054d90>, u'data-processing:job-executions:refresh_status': <oslo_policy._checks.TrueCheck object at 0x7f0fd5054dd0>, u'data-processing:plugins:get_all': <oslo_policy._checks.TrueCheck object at 0x7f0fd5054e10>, u'data-processing:jobs:get': <oslo_policy._checks.TrueCheck object at 0x7f0fd5054e90>, u'data-processing:job-binary-internals:delete': <oslo_policy._checks.TrueCheck object at 0x7f0fd5054ed0>, u'data-processing:job-executions:get': <oslo_policy._checks.TrueCheck object at 0x7f0fd5054f10>, u'data-processing:clusters:delete': <oslo_policy._checks.TrueCheck object at 0x7f0fd5054f50>, u'data-processing:jobs:get_config_hints': <oslo_policy._checks.TrueCheck object at 0x7f0fd5054f90>, u'data-processing:images:get_all': <oslo_policy._checks.TrueCheck object at 0x7f0fd5054fd0>, u'data-processing:images:get': <oslo_policy._checks.TrueCheck object at 0x7f0fd5063050>, u'data-processing:job-binaries:get': <oslo_policy._checks.TrueCheck object at 0x7f0fd5054790>, u'data-processing:job-binary-internals:get_data': <oslo_policy._checks.TrueCheck object at 0x7f0fd50630d0>, u'data-processing:node-group-templates:get': <oslo_policy._checks.TrueCheck object at 0x7f0fd5063110>, u'data-processing:images:set_tags': <oslo_policy._checks.TrueCheck object at 0x7f0fd5063090>, 
u'data-processing:clusters:get_all': <oslo_policy._checks.TrueCheck object at 0x7f0fd5063150>, u'data-processing:images:unregister': <oslo_policy._checks.TrueCheck object at 0x7f0fd50631d0>, u'data-processing:cluster-templates:modify': <oslo_policy._checks.TrueCheck object at 0x7f0fd5063210>, u'data-processing:data-sources:modify': <oslo_policy._checks.TrueCheck object at 0x7f0fd5063190>, u'data-processing:job-binary-internals:get': <oslo_policy._checks.TrueCheck object at 0x7f0fd5054e50>, u'data-processing:data-sources:delete': <oslo_policy._checks.TrueCheck object at 0x7f0fd5054b50>, u'data-processing:jobs:delete': <oslo_policy._checks.TrueCheck object at 0x7f0fd50632d0>, u'data-processing:node-group-templates:create': <oslo_policy._checks.TrueCheck object at 0x7f0fd5063350>, u'data-processing:plugins:convert_config': <oslo_policy._checks.TrueCheck object at 0x7f0fd5063390>, u'data-processing:job-executions:get_all': <oslo_policy._checks.TrueCheck object at 0x7f0fd50633d0>, u'data-processing:jobs:execute': <oslo_policy._checks.TrueCheck object at 0x7f0fd5063410>, u'data-processing:cluster-templates:delete': <oslo_policy._checks.TrueCheck object at 0x7f0fd5063450>, u'data-processing:job-binaries:get_data': <oslo_policy._checks.TrueCheck object at 0x7f0fd5063490>, u'default': <oslo_policy._checks.TrueCheck object at 0x7f0fd50634d0>, u'data-processing:data-sources:get_all': <oslo_policy._checks.TrueCheck object at 0x7f0fd5063510>, u'data-processing:cluster-templates:get': <oslo_policy._checks.TrueCheck object at 0x7f0fd5063550>, u'data-processing:images:remove_tags': <oslo_policy._checks.TrueCheck object at 0x7f0fd5063590>, u'data-processing:node-group-templates:get_all': <oslo_policy._checks.TrueCheck object at 0x7f0fd50635d0>, u'data-processing:data-sources:get': <oslo_policy._checks.TrueCheck object at 0x7f0fd5063610>, u'context_is_admin': <oslo_policy._checks.RoleCheck object at 0x7f0fd5063310>, u'data-processing:jobs:modify': <oslo_policy._checks.TrueCheck object at 0x7f0fd5063650>, u'data-processing:data-sources:register': <oslo_policy._checks.TrueCheck object at 0x7f0fd5063250>, u'data-processing:job-binary-internals:modify': <oslo_policy._checks.TrueCheck object at 0x7f0fd5063690>, u'data-processing:jobs:create': <oslo_policy._checks.TrueCheck object at 0x7f0fd50636d0>}

<oslo_policy._checks.TrueCheck object at 0x7f0fd5063150>
class TrueCheck(BaseCheck)
 |  A policy check that always returns ``True`` (allow).


we have to undersatand how load_policy converting the policy.json to such object and what we can do
with that object
