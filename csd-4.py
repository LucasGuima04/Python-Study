import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, 
    QHBoxLayout, QLabel, QFrame, QSizePolicy
)
from PyQt5.QtGui import QFont, QPalette, QColor, QIcon, QLinearGradient, QBrush
from PyQt5.QtCore import Qt
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np

# Configuração de estilo para o Matplotlib (fundo escuro e fontes limpas)
plt.style.use('dark_background')

class Estilo:
    COR_PRIMARIA = "#1D3557"   # Navy Blue
    COR_SECUNDARIA = "#457B9D" # Steel Blue
    COR_TERCIARIA = "#F1FAEE"   # Off-White
    COR_TEXTO_GRAFICO = "#FFFFFF"
    COR_LINHA_GRID = "#3A3A3A"
    COR_EIXOS = "#A0A0A0"
    FONTE_TITULO = "Helvetica Neue"
    FONTE_CORPO = "Arial"

class GraficoSwaption(FigureCanvas):
    def __init__(self, parent=None, is_payer=True, width=5, height=4, dpi=100):
        self.is_payer = is_payer
        # Usando a classe Estilo diretamente
        fig, self.ax = plt.subplots(figsize=(width, height), dpi=dpi)
        super(GraficoSwaption, self).__init__(fig)
        self.setParent(parent)
        self.setup_plot()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

    def setup_plot(self):
        # Parâmetros de simulação (para 1 ano de opção)
        notional = 500  # USD M
        strike = 3.6    # %
        preço_spread = 0.5 # % a.a.

        # Geração de dados
        # Taxa SOFR no vencimento da opção (1 ano)
        sofr_vencimento = np.linspace(2.0, 8.0, 100)
        
        if self.is_payer:
            # Payoff da Payer Swaption no vencimento da OPÇÃO
            # Exercida se SOFR > Strike
            payoff = np.maximum(0, sofr_vencimento - strike) * notional / 100
            título = "CENÁRIO 1: PAYER SWAPTION - PAYOFF\nNO VENCIMENTO (USD MILHÕES)"
            cor_linha = "#F4A261" # Laranja quente para payer
        else:
            # Payoff da Receiver Swaption no vencimento da OPÇÃO
            # Exercida se SOFR < Strike
            payoff = np.maximum(0, strike - sofr_vencimento) * notional / 100
            título = "CENÁRIO 2: RECEIVER SWAPTION - PAYOFF\nNO VENCIMENTO (USD MILHÕES)"
            cor_linha = "#E76F51" # Vermelho/laranja escuro para receiver

        # Plotagem
        self.ax.plot(sofr_vencimento, payoff, color=cor_linha, linewidth=2.5, marker='.', markersize=4, markerfacecolor='white', markeredgecolor=cor_linha)

        # Configuração de Eixos (L-shape limpo como na referência)
        self.ax.spines['top'].set_visible(False)
        self.ax.spines['right'].set_visible(False)
        self.ax.spines['left'].set_color(Estilo.COR_EIXOS)
        self.ax.spines['bottom'].set_color(Estilo.COR_EIXOS)
        
        # Grid discreto
        self.ax.grid(True, linestyle='--', color=Estilo.COR_LINHA_GRID, alpha=0.5)

        # Rótulos e Títulos
        self.ax.set_title(título, fontname=Estilo.FONTE_TITULO, fontsize=12, fontweight='bold', color=Estilo.COR_TEXTO_GRAFICO, pad=20)
        self.ax.set_xlabel("TAXA SOFR NO VENCIMENTO (%)", fontname=Estilo.FONTE_CORPO, fontsize=10, color=Estilo.COR_TEXTO_GRAFICO)
        self.ax.set_ylabel("PAYOFF (MILHÕES USD)", fontname=Estilo.FONTE_CORPO, fontsize=10, color=Estilo.COR_TEXTO_GRAFICO)
        
        # Formatação de Ticks
        self.ax.tick_params(axis='both', colors=Estilo.COR_EIXOS, labelsize=9)
        self.ax.set_xticks(np.arange(2.0, 9.0, 1.0))
        self.ax.set_xticklabels([f"{x:.0f}%" for x in np.arange(2.0, 9.0, 1.0)], fontname=Estilo.FONTE_CORPO)
        self.ax.set_yticks(np.arange(-100, 201, 50))
        self.ax.set_yticklabels([f"{y:+.0f}M" if y!=0 else "0" for y in np.arange(-100, 201, 50)], fontname=Estilo.FONTE_CORPO)

        # Linha do Strike
        self.ax.axvline(x=strike, color=Estilo.COR_TEXTO_GRAFICO, linestyle='--', linewidth=1, alpha=0.8)
        self.ax.text(strike + 0.1, 150, f"GREVE DE TETO\n(STRIKE): {strike:.1f}%", color=Estilo.COR_TEXTO_GRAFICO, fontname=Estilo.FONTE_CORPO, fontsize=8, verticalalignment='center')
        
        # Ajuste de layout
        self.figure.tight_layout()

class DashboardSwaption(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CSD-4: AEROLOG SWAPTION ANALYSIS DASHBOARD")
        self.setGeometry(100, 100, 1200, 800)
        self.set_dark_palette()
        self.setup_ui()

    def set_dark_palette(self):
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor("#121212"))
        palette.setColor(QPalette.WindowText, Qt.white)
        palette.setColor(QPalette.Base, QColor("#1E1E1E"))
        palette.setColor(QPalette.AlternateBase, QColor("#2A2A2A"))
        palette.setColor(QPalette.ToolTipBase, Qt.white)
        palette.setColor(QPalette.ToolTipText, Qt.white)
        palette.setColor(QPalette.Text, Qt.white)
        palette.setColor(QPalette.Button, QColor("#333333"))
        palette.setColor(QPalette.ButtonText, Qt.white)
        palette.setColor(QPalette.BrightText, Qt.red)
        palette.setColor(QPalette.Link, QColor(Estilo.COR_SECUNDARIA))
        palette.setColor(QPalette.Highlight, QColor(Estilo.COR_SECUNDARIA))
        palette.setColor(QPalette.HighlightedText, Qt.black)
        self.setPalette(palette)

    def setup_ui(self):
        # Widget Central e Layout Principal
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(15, 15, 15, 15)
        main_layout.setSpacing(10)

        # --- Header ---
        header_frame = QFrame()
        header_frame.setFrameShape(QFrame.StyledPanel)
        header_frame.setStyleSheet(f"background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 {Estilo.COR_PRIMARIA}, stop:1 #102030); border-radius: 8px; border: 1px solid #3A3A3A;")
        header_layout = QHBoxLayout(header_frame)
        header_layout.setContentsMargins(20, 10, 20, 10)

        # Título do Programa
        app_title = QLabel("CSD-4: AEROLOG SWAPTION ANALYSIS DASHBOARD")
        app_title.setFont(QFont(Estilo.FONTE_TITULO, 16, QFont.Bold))
        app_title.setStyleSheet("color: white; border: none;")
        header_layout.addWidget(app_title, alignment=Qt.AlignVCenter)

        # Ícones de controle simulados (sem função)
        controls_label = QLabel("Min | Max | Fechar")
        controls_label.setFont(QFont(Estilo.FONTE_CORPO, 9))
        controls_label.setStyleSheet("color: #888888; border: none;")
        header_layout.addWidget(controls_label, alignment=Qt.AlignVCenter | Qt.AlignRight)

        main_layout.addWidget(header_frame, 1)

        # --- Área de Gráficos ---
        charts_layout = QHBoxLayout()
        charts_layout.setSpacing(15)

        # Painel Payer Swaption
        payer_panel = QFrame()
        payer_panel.setFrameShape(QFrame.StyledPanel)
        payer_panel.setStyleSheet(f"background-color: {Estilo.COR_PRIMARIA}; border-radius: 8px; border: 1px solid #3A3A3A;")
        payer_layout = QVBoxLayout(payer_panel)
        payer_chart = GraficoSwaption(self, is_payer=True)
        payer_layout.addWidget(payer_chart)
        charts_layout.addWidget(payer_panel, 1)

        # Painel Receiver Swaption
        receiver_panel = QFrame()
        receiver_panel.setFrameShape(QFrame.StyledPanel)
        receiver_panel.setStyleSheet(f"background-color: #1A1A2A; border-radius: 8px; border: 1px solid #3A3A3A;")
        receiver_layout = QVBoxLayout(receiver_panel)
        receiver_chart = GraficoSwaption(self, is_payer=False)
        receiver_layout.addWidget(receiver_chart)
        charts_layout.addWidget(receiver_panel, 1)

        main_layout.addLayout(charts_layout, 10) # Peso maior para os gráficos

        # --- Status Bar ---
        status_frame = QFrame()
        status_frame.setStyleSheet(f"background-color: {Estilo.COR_PRIMARIA}; border-radius: 8px; border: 1px solid #3A3A3A;")
        status_layout = QHBoxLayout(status_frame)
        status_layout.setContentsMargins(15, 5, 15, 5)

        # Dados da Simulação
        info_label = QLabel("Status: Simulação Completa  |  Dados: Baseados em captação de USD 500M  |  Tenor da opção: 1 ano  |  Data de Vencimento: 12/2027  |  Prêmio estimado: +0.5% a.a.")
        info_label.setFont(QFont(Estilo.FONTE_CORPO, 9))
        info_label.setStyleSheet("color: #CCCCCC; border: none;")
        status_layout.addWidget(info_label, alignment=Qt.AlignVCenter)

        # Logo simulada
        logo_label = QLabel("AEROLOG")
        logo_label.setFont(QFont(Estilo.FONTE_TITULO, 10, QFont.Bold))
        logo_label.setStyleSheet("color: white; border: none; letter-spacing: 2px;")
        status_layout.addWidget(logo_label, alignment=Qt.AlignVCenter | Qt.AlignRight)

        main_layout.addWidget(status_frame, 1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DashboardSwaption()
    window.show()
    sys.exit(app.exec_())