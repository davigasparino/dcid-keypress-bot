from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QSizePolicy, QLineEdit

class JanelaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Minha Janela Personalizada")
        self.resize(800, 500)
        
        layout_principal = QHBoxLayout()
        layout_esquerdo = QVBoxLayout()
        self.layout_direito = QVBoxLayout()  # Defina layout_direito como um atributo da classe
        
        coluna_esquerda = QWidget()
        coluna_esquerda.setStyleSheet("background-color: #d9d9d9")
        coluna_esquerda.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        coluna_esquerda.setMinimumSize(200, 0)
        
        button = QPushButton("Clique Aqui")
        button.clicked.connect(self.on_button_click)
        layout_esquerdo.addWidget(button)
        
        div_direita = QWidget()
        div_direita.setStyleSheet("background-color: #e3e3e3")
        div_direita.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        div_direita.setMinimumSize(600, 0)
        
        self.layout_direito.addWidget(div_direita)  # Adicione div_direita ao layout_direito
        
        layout_principal.addLayout(layout_esquerdo)
        layout_principal.addLayout(self.layout_direito)  # Use self.layout_direito aqui
        self.setLayout(layout_principal)

    def on_button_click(self):
        # Crie um novo QLineEdit (campo de entrada de texto)
        novo_input_texto = QLineEdit()
        self.layout_direito.addWidget(novo_input_texto)  # Adicione-o ao layout_direito

app = QApplication([])
janela = JanelaPrincipal()
janela.show()
app.exec_()
