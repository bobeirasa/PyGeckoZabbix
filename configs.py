geckoboardapikey = 'put your geckoboard api key here'
zabbixapiurl = 'your zabbix url'
zabbixapilogin = 'your zabbix login'
zabbixapipasswd = 'your zabbix passwd'

notriggersmessage = 'Good job, infra! Nothing is triggered on Zabbix :-)'

pieces = [
    {
        'type': 'Zabbix Item',
        'kind': 'Item',
        'name': 'Sample name',
        'zid': 25188,
        'widget_key': 'xxx',
        'mintrigger': 1,
        'maxtrigger': 50,
        'percenttrigger': 40,
        'colortrigger': '9d3926',
        'unit': '%',
    },
    {
        'type': 'Zabbix Item',
        'kind': 'Monitoring',
        'httpcodezid': 28985,
        'httpexpectedcode': 200,
        'httptimezid': 28984,
        'httplasterrorzid': 28982,
        'name': 'psafe.com',
        'widget_key': 'xxx',
    },
    {
        'type': 'Zabbix Item',
        'kind': 'Triggers',
        'name': 'Unack issues',
        'widget_key': 'xxx',
    },
]