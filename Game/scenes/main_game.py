import pytweening, pygame, sys, os

import engine.libs.Formatter as formatter
import engine.libs.Utils as utils
import engine.libs.EntityService as EntityService 
import engine.libs.SceneService as SceneService 
import engine.libs.GuiService as GuiService 
import engine.libs.TweenService as TweenService

import cctd.scripts.map_loader as map_loader

class Main_Game(SceneService.Scene):
    def __init__(self, scene_name, app):
        super().__init__(scene_name, app)
        self.app = app
    
      

    def on_enter(self):
        super().on_enter()    
        self.map = self.extra_data[0]


        GuiService.SurfaceElement((formatter.get_center(1280, 720)), self.map.map_image) # Background

     
    def update(self):
        pass
        
    def draw(self):
        self.app.get_screen().fill((0))  
      
