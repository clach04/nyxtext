# Workspace : 

from text_Area import textarea
from framework.tab_View import TabView

class Workspace:
    def __init__(self,tab_view):
        self.workspace_init = tab_view.add("Workspace")
        self.tab_view = tab_view
        self.Textarea = textarea(self.workspace_init)