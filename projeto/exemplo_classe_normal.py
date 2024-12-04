# exemplo_classe_normal.py

class Config:
    def __init__(self):
        self.settings = {}

    def set_setting(self, setting_name, value):
        self.settings[setting_name] = value

    def get_setting(self, setting_name):
        return self.settings.get(setting_name, None)

    def update_setting(self, setting_name, value):
        if setting_name in self.settings:
            self.settings[setting_name] = value
        else:
            print(f"Configuração '{setting_name}' não encontrada.")

    def remove_setting(self, setting_name):
        if setting_name in self.settings:
            del self.settings[setting_name]
        else:
            print(f"Configuração '{setting_name}' não encontrada.")

    def list_settings(self):
        return self.settings

    def exists(self, setting_name):
        return setting_name in self.settings

    def __str__(self):
        return str(self.settings)