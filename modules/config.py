import json

from pathlib import Path


class Config:
    def __init__(self, ui_main):
        self.ui_main = ui_main
        self.work_path = Path.cwd()
        self.config_file = self.work_path / "config.json"

        self.setting = self.get_setting()
        self._update_setting()

    def _update_setting(self):
        update = self.setting.get("update")
        self.ui_main.actionCheckRun.setChecked(update)

    def _set_default_setting(self):
        self.default_setting = {
            "update": True
        }

        self.set_setting(self.default_setting)

    def get_path(self):
        return self.work_path

    def get_setting(self):
        if not self.config_file.exists():
            self._set_default_setting()

        with open(self.config_file, "r") as f:
            return json.load(f)

    def set_setting(self, setting):
        with open(self.config_file, "w") as f:
            json.dump(setting, f)
