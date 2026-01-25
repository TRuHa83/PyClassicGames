from PySide6.QtCore    import Qt
from PySide6.QtGui     import QPixmap, QFont, QCursor
from PySide6.QtWidgets import QPushButton, QVBoxLayout, QLabel


class GameButton(QPushButton):
    def __init__(self, name, description, icon_path):
        super().__init__()
        self._name = name
        self._description = description
        self._icon_path = icon_path

        self.setObjectName("button_" + self._name.replace(" ", "_").lower())

        self.style()
        self.content()

    def style(self):
        self.setFixedSize(320, 140)
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.setStyleSheet(
            """
            QPushButton {
                color: #374151;
                background-color: #ffffff;
                border: 1px solid #d1d5db;
                border-radius: 8px;
            }
            
            QPushButton:hover {
                background-color: #f3f4f6;
                border: 1px solid #9ca3af;
            }
            
            QPushButton:pressed {
                background-color: #e5e7eb;
                border: 1px solid #9ca3af;
            }
            """
        )

    def content(self):
        # Layout
        layout = QVBoxLayout(self)

        # 1. Icono
        label_icon = QLabel()
        label_icon.setFixedSize(60, 60)
        pixmap = QPixmap(self._icon_path)
        label_icon.setPixmap(QPixmap(pixmap))
        label_icon.setScaledContents(True)


        # 2. Título
        label_name = QLabel(self._name)
        font_name = QFont()
        font_name.setPointSize(12)
        font_name.setBold(True)
        label_name.setFont(font_name)
        label_name.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # 3. Descripción
        label_desc = QLabel(self._description)
        font_desc = QFont()
        font_desc.setPointSize(9)
        label_desc.setFont(font_desc)
        label_desc.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Añadir al layout
        layout.addWidget(label_icon, 0, Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(label_name)
        layout.addWidget(label_desc)