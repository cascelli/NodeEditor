import sys
from PyQt5.QtWidgets import *

from node_editor_window import NodeEditorWindow

if __name__ == '__main__':

    app = QApplication(sys.argv)

    # label = QLabel("Hello PyQt5 !")
    # label.show()

    wnd = NodeEditorWindow()

    sys.exit(app.exec_())
