# POO-RPG-Simulador

🛡️ **Padrão de Projeto: Singleton**  
🔐 **Pré-requisitos:** Node.js, TypeScript

## Padrão Singleton

### Passos a serem seguidos:
- **Passo 01:** Introdução ao padrão Singleton e seus contextos de aplicação.
- **Passo 02:** Implementação do padrão Singleton em TypeScript.
- **Passo 03:** Refatorando a gestão de instâncias no projeto POO-RPG-Simulador usando Singleton.
- **Passo 04:** Aplicação prática do padrão Singleton para garantir que uma classe tenha apenas uma instância e fornecer um ponto de acesso global a ela.

⚙️ **Executando o Projeto**

🔍 **Sobre o Trabalho**  
Este projeto demonstra o uso do padrão Singleton para gerenciar a criação de instâncias no projeto POO-RPG-Simulador. Ao utilizar o Singleton, garantimos que uma única instância de uma classe seja criada e utilizada em todo o sistema, promovendo a consistência e evitando a duplicação de recursos.

### Implementação do Padrão Singleton
O padrão Singleton foi implementado na classe `GerenciadorDeJogo` (arquivo `src/GerenciadorDeJogo.ts`). Esta classe é responsável por gerenciar o estado do jogo e garantir que apenas uma instância dela exista durante a execução do programa. A implementação do Singleton é feita através de um construtor privado e um método estático que fornece acesso à instância única.

```typescript
class GerenciadorDeJogo {
    private static instancia: GerenciadorDeJogo;

    private constructor() {
        // Inicialização do gerenciador de jogo
    }

    public static getInstancia(): GerenciadorDeJogo {
        if (!GerenciadorDeJogo.instancia) {
            GerenciadorDeJogo.instancia = new GerenciadorDeJogo();
        }
        return GerenciadorDeJogo.instancia;
    }

    // Métodos para gerenciar o jogo
}

Link do video de apresentação- https://youtu.be/R_OSaBHf__g
