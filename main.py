import arcade
#متابخانه بازی سازس را ایمپورت کردیم
class Game(arcade.Window):
    #یک کلاس که زیر مجموعه ویندو در arcade است را ایجاد کردیم
    def __init__(self):
        #یک تابع فعال در کلاس ساختیم
        super().__init__(width=600,height=600,title="game")
        #مشخصات یک پنجره را داده ایم
        arcade.set_background_color(arcade.color.BLUE)
        #رنگ س زمینه را انتخاب کردیم
        self.background=arcade.load_texture("BG.png")
        #بک گراند را تنظیم کردم
    def on_draw(self):
        #حالا یک تابع جدید ساختیم
        arcade.start_render()
        #استارت کردیم رندر گرفتم را
        arcade.draw_lrwh_rectangle_textured(0,0,self.width,self.height,self.background)
        #مشخصات پنجره را دادیم
        arcade.finish_render()
        #ان را تمام کردیم

if __name__ == "__main__":
    #یک شرط گذاشتیم
    window=Game()
    #و ویندو را مساوی با کلاس گیم کردیم
    arcade.run()
    #حالا ان را ران کردین
