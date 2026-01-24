import version
import requests

from PySide6.QtWidgets import QMessageBox


def _check_update():
    repo = version.__github_url__.split("/")
    user, project = repo[-2], repo[-1]
    api_url = f"https://api.github.com/repos/{user}/{project}/releases/latest"
    current_version = [int(x) for x in version.__version__.split(".")]

    response = requests.get(api_url, timeout=5)
    if response.status_code == 200:
        data = response.json()

        last_version = data["tag_name"].lstrip("v")
        last_version = [int(x) for x in last_version.split(".")]

        if last_version > current_version:
            return True

    return False


class Update:
    def __init__(self, ui_main):
        self.ui_main = ui_main

    def _update_true(self):
        title = "Actualización"
        message = f"""
                    <h3>¡Hay una nueva versión disponible!</h3>

                    <p>Se ha encontrado la version <b>{version.__version__}</b> lista para descargar.</p>
                    <p>Puedes descargarla desde <a href='{version.__github_url__ + '/releases/latest'}'>aquí</a> o desde el repositorio del proyecto en GitHub:</p>
                    <p>{version.__github_url__}</p>
                    """

        QMessageBox.information(self.ui_main, title, message)

    def _update_false(self):
        title = "Actualización"
        message = f"""
                    <h3>¡Tu aplicación ya está actualizada!</h3>

                    <p>La versión actual es la <b>{version.__version__}</b>.</p>
                    <p>No hay nuevas versiones disponibles en este momento.</p>
                    """

        QMessageBox.information(self.ui_main, title, message)

    def man_check_update(self):
        if _check_update():
            self._update_true()

        else:
            self._update_false()

    def auto_check_update(self):
        if _check_update():
            self._update_true()
