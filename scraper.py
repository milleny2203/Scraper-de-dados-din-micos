import tkinter as tk
from tkinter import messagebox, ttk
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class WebScraperApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Scraper de Dados Dinâmicos")
        
        ##Configurando a interface
        self.url_label = tk.Label(root, text="URL:")
        self.url_label.grid(row=0, column=0, padx=5, pady=5)
        self.url_entry = tk.Entry(root, width=40, background='pink', takefocus=0)
        self.url_entry.grid(row=0,column=1,padx=5,pady=5)
        
        self.xpath_label = tk.Label(root, text="XPath do elemento:")
        self.xpath_label.grid(row=1,column=0,padx=5,pady=5)
        self.xpath_entry = tk.Entry(root, width=40,background='pink',takefocus=1)
        self.xpath_entry.grid(row=1,column=1,padx=5,pady=5)
        
        self.xpath_label = tk.Label(root, text="Clique para coletar os dados:")
        self.xpath_label.grid(row=2,column=0,padx=5,pady=5)
        self.scrape_button = tk.Button(root, text="Coletar Dados", command= self.scrape_data,takefocus=2)
        self.scrape_button.grid(row=2,column=0,columnspan=10,pady=5,padx=5)
        
        self.results_label = tk.Label(root, text="Resultados:")
        self.results_label.grid(row=3,column=0,padx=5,pady=5)
        self.results_text = tk.Text(root, height=10, width=50, borderwidth=5, relief="groove")
        self.results_text.grid(row=4,column=0,columnspan=2,padx=5,pady=5)
        
    def scrape_data(self):
        url = self.url_entry.get()
        xpath = self.xpath_entry.get()
            
        if not url or not xpath:
            messagebox.showerror("Erro", "Preencha todos os campos!")
            return
            
        try:
            driver = webdriver.Chrome()
            driver.get(url)
            time.sleep(5)
                
            elements = driver.find_elements(By.XPATH, xpath)
            results = [element.text for element in elements]
            driver.quit
                
            self.results_text.delete("1.0", tk.END)
            if results:
                self.results_text.insert(tk.END, '\n'.join(results))
            else:
                self.results_text.insert(tk.END, "Nenhum dado foi encontrado para o XPath informado")
        except Exception as e:
            messagebox.showerror("Erro", "Erro ao coletar os dados: {str(e)}")
        
##Inicializar app 
if __name__ == "__main__":
    root = tk.Tk()
    app = WebScraperApp(root)
    root.mainloop()