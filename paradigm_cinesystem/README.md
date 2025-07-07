# 🎬 Paradigm CineSystem

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.7+-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
  <img src="https://img.shields.io/badge/GUI-CustomTkinter-orange.svg" alt="GUI Framework">
  <img src="https://img.shields.io/badge/Database-SQLite-lightgrey.svg" alt="Database">
</div>

## 📖 Sobre o Projeto

O **Paradigm CineSystem** é uma aplicação moderna de reserva de ingressos de cinema desenvolvida em Python. Com uma interface gráfica elegante e intuitiva, o sistema permite aos usuários visualizar filmes disponíveis, verificar preços e realizar compras de ingressos de forma simples e eficiente.

### ✨ Principais Características

- 🎨 **Interface Moderna**: Desenvolvida com CustomTkinter para uma experiência visual atraente
- 📊 **Visualização em Tempo Real**: Tabela interativa mostrando disponibilidade de ingressos
- 💾 **Persistência de Dados**: Banco de dados SQLite para armazenamento confiável
- 🎫 **Comprovantes**: Geração automática de recibos de compra
- 🔄 **Atualizações Automáticas**: Sincronização instantânea do estoque após compras

## 🚀 Funcionalidades

### 🎪 Tela Inicial
- Splash screen com design customizado
- Botão de inicialização com animações suaves

### 🎯 Sistema de Reservas
- **Seleção de Filmes**: Visualize todos os filmes disponíveis
- **Controle de Quantidade**: Escolha de 1 a 3 ingressos por compra
- **Validação Inteligente**: Verificação automática de disponibilidade
- **Confirmação de Compra**: Feedback visual da transação

### 📋 Gerenciamento de Dados
- **Banco de Dados**: SQLite com tabela otimizada para tickets
- **Arquivo de Logs**: Histórico completo de todas as transações
- **Validação de Entrada**: Proteção contra dados inválidos

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Versão | Propósito |
|-----------|--------|-----------|
| **Python** | 3.7+ | Linguagem principal |
| **CustomTkinter** | Latest | Interface gráfica moderna |
| **Tkinter** | Built-in | Widgets complementares |
| **SQLite3** | Built-in | Banco de dados |

## 📦 Instalação

### Pré-requisitos
- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)

### 🔧 Passos de Instalação

1. **Clone o repositório**
   ```bash
   git clone https://github.com/deerws/oop_pratices/paradigm_cinesystem.git
   cd ParadigmCineSystem
   ```

2. **Instale as dependências**
   ```bash
   pip install customtkinter
   ```

3. **Execute a aplicação**
   ```bash
   python main.py
   ```

## 🗂️ Estrutura do Projeto

```
ParadigmCineSystem/
├── 📁 assets/
│   ├── 0.png              # Imagem da tela inicial
│   └── 1.png              # Imagem da tela principal
├── 📄 database.py         # Operações do banco de dados
├── 📄 main.py            # Lógica principal da aplicação
├── 📄 Reservation.db     # Banco de dados SQLite (auto-gerado)
├── 📄 Tickets.txt        # Arquivo de comprovantes (auto-gerado)
└── 📄 README.md          # Documentação do projeto
```

## 🎯 Como Usar

### 1️⃣ Iniciando a Aplicação
- Execute o arquivo `main.py`
- Clique no botão **"Start"** na tela inicial

### 2️⃣ Comprando Ingressos
1. **Selecione um filme** na tabela de filmes disponíveis
2. **Digite seu nome** no campo "Username"
3. **Escolha a quantidade** de ingressos (1-3)
4. **Clique em "Buy Tickets"** para confirmar

### 3️⃣ Confirmação
- ✅ Mensagem de sucesso será exibida
- 📋 Comprovante será salvo em `Tickets.txt`
- 🔄 Estoque será atualizado automaticamente

## 🗄️ Estrutura do Banco de Dados

### Tabela: `Tickets`
| Campo | Tipo | Descrição |
|-------|------|-----------|
| `ticket_id` | INTEGER | Identificador único do ingresso |
| `movie_name` | TEXT | Nome do filme |
| `ticket_quantity` | INTEGER | Quantidade disponível |
| `ticket_price` | REAL | Preço por ingresso |

## 📱 Interface do Usuário

### Componentes Principais
- **Treeview**: Exibição tabular dos filmes
- **Entry Field**: Campo de entrada para nome do usuário
- **ComboBox**: Seleção de quantidade de ingressos
- **Botões**: Interação com o sistema
- **Labels**: Informações e feedback

### Esquema de Cores
- **Fundo**: `#18161D` (Cinza escuro)
- **Destaque**: `#6ECF00` (Verde vibrante)
- **Texto**: `#FFFFFF` (Branco)
- **Componentes**: `#000000` (Preto)

## 🔧 Personalização

### Modificando Filmes
Edite o arquivo `database.py` para adicionar/remover filmes:

```python
# Exemplo de inserção
cursor.execute("INSERT INTO Tickets VALUES (?, ?, ?, ?)", 
               (4, "Novo Filme", 10, 25.00))
```

### Alterando Limites
Modifique a lista `self.options` em `main.py` para alterar a quantidade máxima de ingressos:

```python
self.options = ['1', '2', '3', '4', '5']  # Permite até 5 ingressos
```

## 🤝 Contribuindo

Contribuições são bem-vindas! Para contribuir:

1. 🍴 Faça um fork do projeto
2. 🌟 Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. 💾 Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. 📤 Push para a branch (`git push origin feature/AmazingFeature`)
5. 🔍 Abra um Pull Request

## 📋 Roadmap

- [ ] 🌐 Interface web complementar
- [ ] 🎨 Temas personalizáveis
- [ ] 📊 Relatórios de vendas
- [ ] 🔐 Sistema de autenticação
- [ ] 💳 Integração com pagamentos
- [ ] 📱 Versão mobile

## 🐛 Problemas Conhecidos

- Imagens devem estar no diretório raiz
- Quantidade máxima limitada a 3 ingressos
- Validação básica de entrada

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 👨‍💻 Autor

**Seu Nome**
- GitHub: [@deerws](https://github.com/deerws)
- Email: seu.email@example.com

---

<div align="center">
  <p>⭐ Se este projeto foi útil para você, considere dar uma estrela!</p>
  <p>🎬 Feito com ❤️ para entusiastas de cinema</p>
</div>
