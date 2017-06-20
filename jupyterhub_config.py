# our user list
c.Authenticator.whitelist = [
    'jb',
    'mi',
    'an',
    'kf',
    'mo'
]

# jb and mi have access to a shared server:

c.JupyterHub.load_groups = {
    'shared': [
        'jb',
        'mi',
        'kf',
    ]
}

service_name = 'shared-notebook'
service_port = 9999
group_name = 'aqb'

# start the notebook server as a service
c.JupyterHub.services = [
    {
        'name': service_name,
        'url': 'http://127.0.0.1:{}'.format(service_port),
        'command': [
            'jupyterhub-singleuser',
            '--group=aqb',
            '--debug',
        ],
    }
]
