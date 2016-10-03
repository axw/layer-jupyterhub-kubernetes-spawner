c.KubeSpawner.kube_api_endpoint = 'https://{{kube_hostname}}:{{kube_port}}'
c.KubeSpawner.kube_ca_path = False
c.KubeSpawner.start_timeout = 60 * 5  # First pulls can be really slow

