# Scraper de Dados Dinâmicos com Interface Gráfica

✨ Recursos

Interface Gráfica (GUI): Desenvolvida com Tkinter, proporciona uma experiência de uso amigável para configurar parâmetros do scraper.
Extração Dinâmica de Dados: Usa Selenium WebDriver para interagir com páginas web que carregam conteúdo dinamicamente (como carrosséis, tabelas e dados carregados via JavaScript).

Compatibilidade com Navegadores: Configurado para trabalhar com Google Chrome, mas pode ser ajustado para outros navegadores suportados pelo Selenium.

Personalização de Busca: O usuário pode inserir URLs, selecionar elementos específicos e iniciar o scraper diretamente pela interface.

Automação de Interações: Possui suporte para cliques, rolagens e espera dinâmica (ideal para páginas que demoram a carregar).


🛠️ Tecnologias Utilizadas

Python 3.8+
Tkinter: Para criação da interface gráfica.
Selenium WebDriver: Para controle automatizado do navegador e scraping dinâmico.

📋 Como Funciona

O usuário insere uma URL e define os seletores dos elementos que deseja capturar.
O scraper utiliza o Selenium para abrir o navegador, acessar a URL e interagir com os elementos dinâmicos.
Os dados extraídos são exibidos na interface ou salvos em um arquivo local, como CSV ou TXT.

🚀 Como Executar

Pré-requisitos:

- Python 3.8 ou superior instalado.
- Google Chrome e o ChromeDriver correspondente instalado.

pip install -r requirements.txt

python3 scraper.py

📁 Scraper-dados-dinamicos/
├── scraper.py            # Script principal do scraper
├── requirements.txt      # Dependências do projeto
├── README.md             # Documentação do projeto


🖼️ Demonstração

<img width="310" alt="image" src="https://github.com/user-attachments/assets/a2db5c66-f72e-483d-ad5a-a82056c8e5e7" />

⚠️ Aviso

Este projeto deve ser usado apenas para fins educacionais ou pessoais. Respeite as políticas de uso dos sites antes de realizar scraping.
