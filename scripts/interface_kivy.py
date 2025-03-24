from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.core.window import Window
import random
import json
import os

Window.clearcolor = (1, 1, 1, 1)  # Fundo branco

CAMINHO_JSON = os.path.abspath(os.path.join(os.path.dirname(__file__), 'perguntas_show_do_milhao.json'))

with open(CAMINHO_JSON, 'r', encoding='utf-8') as f:
    perguntas = json.load(f)

class ShowLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=10, **kwargs)

        self.perguntas = perguntas
        self.usadas = []
        self.pontuacao = 0
        self.ajudas = {"dica": 1, "pular": 1, "eliminar": 1}
        self.rodada = 0

        self.label_pergunta = Label(text="Clique em Começar para iniciar o jogo", font_size=20, halign='center', valign='middle')
        self.add_widget(self.label_pergunta)

        self.botoes_opcao = []
        for _ in range(4):
            btn = Button(text="", size_hint_y=None, height=50, background_color=(0.9, 0.9, 0.9, 1))
            btn.bind(on_press=self.responder)
            self.add_widget(btn)
            self.botoes_opcao.append(btn)

        self.botoes_ajuda = BoxLayout(size_hint_y=None, height=40, spacing=10)
        for nome, func in [("Dica", self.usar_dica), ("Pular", self.pular), ("Eliminar", self.eliminar)]:
            btn = Button(text=nome, background_color=(0.8, 0.2, 0.2, 1))
            btn.bind(on_press=func)
            self.botoes_ajuda.add_widget(btn)
        self.add_widget(self.botoes_ajuda)

        self.btn_comecar = Button(text="Começar Jogo", size_hint_y=None, height=50, background_color=(0.2, 0.6, 0.2, 1))
        self.btn_comecar.bind(on_press=self.nova_pergunta)
        self.add_widget(self.btn_comecar)

    def nova_pergunta(self, instance=None):
        if self.rodada >= 10:
            self.label_pergunta.text = f"Fim de jogo! Sua pontuação: {self.pontuacao}"
            return

        disponiveis = [i for i in range(len(self.perguntas)) if i not in self.usadas]
        if not disponiveis:
            self.label_pergunta.text = "Acabaram as perguntas."
            return

        self.rodada += 1
        self.indice_atual = random.choice(disponiveis)
        self.pergunta_atual = self.perguntas[self.indice_atual]
        self.usadas.append(self.indice_atual)

        self.label_pergunta.text = f"Pergunta {self.rodada}: {self.pergunta_atual['pergunta']}"
        opcoes = self.pergunta_atual['opcoes']
        random.shuffle(opcoes)
        for i, btn in enumerate(self.botoes_opcao):
            btn.text = opcoes[i]
            btn.disabled = False

    def responder(self, instance):
        if instance.text == self.pergunta_atual['resposta']:
            self.pontuacao += 10
            self.popup("Resposta correta!")
        else:
            self.popup(f"Errado! A correta era: {self.pergunta_atual['resposta']}")
        self.nova_pergunta()

    def usar_dica(self, instance):
        if self.ajudas['dica'] > 0:
            self.popup(f"Dica: {self.pergunta_atual['dica']}")
            self.ajudas['dica'] -= 1
        else:
            self.popup("Você já usou sua dica.")

    def pular(self, instance):
        if self.ajudas['pular'] > 0:
            self.ajudas['pular'] -= 1
            self.nova_pergunta()
        else:
            self.popup("Você já usou seu pulo.")

    def eliminar(self, instance):
        if self.ajudas['eliminar'] > 0:
            self.ajudas['eliminar'] -= 1
            resposta = self.pergunta_atual['resposta']
            erradas = [op for op in self.pergunta_atual['opcoes'] if op != resposta]
            eliminadas = random.sample(erradas, 2)
            for btn in self.botoes_opcao:
                if btn.text in eliminadas:
                    btn.disabled = True
        else:
            self.popup("Você já usou a eliminação.")

    def popup(self, mensagem):
        pop = Popup(title='Informativo', content=Label(text=mensagem), size_hint=(None, None), size=(400, 200))
        pop.open()

class ShowDoMilhaoApp(App):
    def build(self):
        return ShowLayout()

if __name__ == '__main__':
    ShowDoMilhaoApp().run()
