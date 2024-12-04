# exemplo_singleton.py

import json

class SingletonConfig:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(SingletonConfig, cls).__new__(cls)
            cls._instance.settings = {}
        return cls._instance

    def set_setting(self, setting_name, value):
        """Define uma configuração com um nome e valor especificados."""
        self.settings[setting_name] = value

    def get_setting(self, setting_name):
        """Retorna o valor de uma configuração especificada pelo nome."""
        return self.settings.get(setting_name, None)

    def update_setting(self, setting_name, value):
        """Atualiza o valor de uma configuração existente."""
        if setting_name in self.settings:
            self.settings[setting_name] = value
        else:
            print(f"Configuração '{setting_name}' não encontrada.")

    def remove_setting(self, setting_name):
        """Remove uma configuração especificada pelo nome."""
        if setting_name in self.settings:
            del self.settings[setting_name]
        else:
            print(f"Configuração '{setting_name}' não encontrada.")

    def save_to_file(self, filename):
        """Salva as configurações em um arquivo JSON."""
        with open(filename, 'w') as file:
            json.dump(self.settings, file)

    def load_from_file(self, filename):
        """Carrega as configurações de um arquivo JSON."""
        try:
            with open(filename, 'r') as file:
                self.settings = json.load(file)
        except FileNotFoundError:
            print(f"Arquivo '{filename}' não encontrado.")
        except json.JSONDecodeError:
            print(f"Erro ao decodificar o arquivo '{filename}'.")

    def exists(self, setting_name):
        """Verifica se uma configuração existe."""
        return setting_name in self.settings

    def list_settings(self):
        """Lista todas as configurações armazenadas."""
        return self.settings

    def __str__(self):
        """Retorna uma representação em string das configurações."""
        return str(self.settings)