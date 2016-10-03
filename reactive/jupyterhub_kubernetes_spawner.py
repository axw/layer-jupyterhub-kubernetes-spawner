import subprocess

from charms.reactive import when, when_not, set_state
from charmhelpers.core import templating

@when_not('jupyterhub-kubernetes-spawner.installed')
def install_jupyterhub_kubernetes_spawner():
    subprocess.check_call(
        ['python3', 'setup.py', 'install'],
        cwd='jupyterhub-kubernetes-spawner',
    )
    set_state('jupyterhub-kubernetes-spawner.installed')


@when('jupyterhub-kubernetes-spawner.installed')
@when('jupyterhub.available')
@when('kubernetes-api.available')
def update_config(kubernetes_api, jupyterhub):
    service = kubernetes_api.services()[0]
    service_host = service['hosts'][0]
    spawner_config = {
      'KubeSpawner.kube_api_endpoint': 'https://{hostname}:{port}'.format(**service_host),
      'KubeSpawner.kube_ca_path': False,
      'KubeSpawner.start_timeout': 60*5,
    }
    jupyterhub.set_spawner('kubespawner.KubeSpawner', spawner_config)

