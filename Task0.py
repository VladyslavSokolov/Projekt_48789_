#installResources
import subprocess

def install_components():
    components = [
        "komponent1",
        "komponent2",
        "komponent3",
    ]

    for component in components:
        from pip._internal.utils import subprocess
        subprocess.check_call(["pip", "install", component])

