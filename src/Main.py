from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QSizePolicy

class JanelaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        
        # Configurações da Janela
        self.setWindowTitle("Minha Janela Personalizada")
        self.resize(800, 500)
        
        # Criando os Layouts
        layout_principal = QHBoxLayout()
        layout_esquerdo = QVBoxLayout()
        layout_direito = QVBoxLayout()
        
        # Criando os Widgets
        coluna_esquerda = QWidget()
        coluna_esquerda.setStyleSheet("background-color: #d9d9d9")
        
        # Definindo largura fixa para a coluna da esquerda: 200 pixels
        coluna_esquerda.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        coluna_esquerda.setMinimumSize(200, 0)
        
        # Adicionando botão na coluna esquerda
        button = QPushButton("Clique Aqui")
        button.clicked.connect(self.on_button_click)  # Conectando o sinal clicked do botão ao método on_button_click
        
        layout_esquerdo.addWidget(button)
        
        # Adicionando coluna esquerda ao layout principal
        layout_principal.addLayout(layout_esquerdo)
        
        # Adicionando div_direita à coluna direita
        div_direita = QWidget()
        div_direita.setStyleSheet("background-color: #e3e3e3")
        
        # Definindo largura fixa para a coluna direita: 600 pixels
        div_direita.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        div_direita.setMinimumSize(600, 0)
        
        layout_direito.addWidget(div_direita)
        
        # Ajustando os Layouts
        layout_principal.addLayout(layout_esquerdo)
        layout_principal.addLayout(layout_direito)
        
        # Definindo o Layout Principal
        self.setLayout(layout_principal)
    
    def on_button_click(self):
        # Método chamado quando o botão é clicado
        # Atualiza o texto de um QLabel na div direita
        novo_texto = "Texto Atualizado"
        
        # Acessando o layout direito a partir do widget div_direita
        layout_direito = self.layout_principal.itemAt(1).layout()  # Supondo que a posição 1 contenha o layout_direito
        
        if layout_direito.count() > 1:  # Verifica se há um QLabel na div direita
            label = layout_direito.itemAt(1).widget()  # Obtém o widget QLabel da div direita
            if isinstance(label, QLabel):
                label.setText(novo_texto)



app = QApplication([])
janela = JanelaPrincipal()
janela.show()
app.exec_()
