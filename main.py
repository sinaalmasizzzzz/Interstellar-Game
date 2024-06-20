import arcade
#همپورت کردم کتابخانه را
class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=600,height=600,title="game")
        #یک پنجره باز کردم
        arcade.set_background_color(arcade.color.BLUE)
        self.background=arcade.load_texture("BG.png")
        #بک گراند را تنظیم کردم
    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0,0,self.width,self.height,self.background)
        arcade.finish_render()
    #حالا بازش کردم
if __name__ == "__main__":
    window=Game()
    arcade.run()
#پنجره را ران کردم