# main.py

from exemplo_classe_normal import Config
from exemplo_singleton import SingletonConfig

# Usando a classe normal
print("Usando a classe normal (Config):")
config1 = Config()
config1.set_setting("Database", "MySQL")
config1.set_setting("Cache", "Redis")

print("Config1 Settings:")
print(config1.list_settings())

# Criando uma nova instância da classe normal
config2 = Config()
config2.set_setting("Database", "PostgreSQL")

print("\nConfig2 Settings (nova instância):")
print(config2.list_settings())  # Deve mostrar apenas as configurações de config2

# Configurações de config1 não são afetadas
print("\nConfig1 Settings após criar config2:")
print(config1.list_settings())  # Deve mostrar as configurações originais

# Usando o Singleton
print("\nUsando o Singleton (SingletonConfig):")
singleton_config1 = SingletonConfig()
singleton_config1.set_setting("Database", "PostgreSQL")
singleton_config1.set_setting("Cache", "Memcached")

print("Singleton Config1 Settings:")
print(singleton_config1.list_settings())

# Criando uma nova referência do Singleton
singleton_config2 = SingletonConfig()  # Tentativa de criar uma nova instância
singleton_config2.set_setting("Cache", "Redis")

print("\nSingleton Config2 Settings (mesma instância):")
print(singleton_config2.list_settings())  # Deve mostrar as configurações de singleton_config1

# Ambas as variáveis apontam para a mesma instância
print("\nVerificando se singleton_config1 e singleton_config2 são a mesma instância:")
print(singleton_config1 is singleton_config2)  # Saída: True

# Verificando se uma configuração existe
print("\nVerificando se a configuração 'Cache' existe no Singleton:")
print(singleton_config2.exists("Cache"))  # Saída: True
print("Verificando se a configuração 'Database' existe no Singleton:")
print(singleton_config2.exists("Database"))  # Saída: True

# Comparando as configurações do Singleton e da classe normal
print("\nComparando configurações entre Config e SingletonConfig:")
print("Config1 Settings:")
print(config1.list_settings())
print("Singleton Config Settings:")
print(singleton_config1.list_settings())