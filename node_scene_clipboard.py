class SceneClipboard():
    def __init__(self, scene):
        self.scene = scene

    def serializeSelected(self, delete=False):
        return {}

    def deserializeFromClipboard(self, data):
        print("Deserializating from clipboard, data:", data)
