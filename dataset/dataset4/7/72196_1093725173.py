_NODE_GETTERS_WIN32 = [_windll_getnode, _netbios_getnode, _ipconfig_getnode]

_NODE_GETTERS_UNIX = [_unix_getnode, _ifconfig_getnode, _ip_getnode,
                      _arp_getnode, _lanscan_getnode, _netstat_getnode]