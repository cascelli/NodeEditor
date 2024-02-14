from PyQt5.QtWidgets import *


class QDMNodeContentWidget(QWidget):
    def __init__(self, node, parent=None):
        self.node = node
        super().__init__(parent)

        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        self.wdg_label = QLabel("Some Title")
        self.layout.addWidget(self.wdg_label)
        self.layout.addWidget(QDMTextEdit("Foo"))

    def setEditingFlag(self, value):
        self.node.scene.grScene.views()[0].editingFlag = value


class QDMTextEdit(QTextEdit):
    # def keyPressEvent(self, event):
    #     print("QDMTextEdit -- KEY PRESS")
    #     # event.ignore()  # to stop propagation event from bottom to top objects
    #     super().keyPressEvent(event)

    def focusInEvent(self, event):
        # print("Focus In")
        self.parentWidget().setEditingFlag(True)
        super().focusInEvent(event)

    def focusOutEvent(self, event):
        # print("Focus Out")
        self.parentWidget().setEditingFlag(False)
        super().focusOutEvent(event)
