class MyApp(App):
 def build(self): # Создание и размещение виджетов в приложении
 # Экран приложения
 self.screen = CustomWidget(color_bg=FIRST_DARK_COLOR, size=(1280, 800), pos=(0, 0))
 # Инициализация страницв приложении
 self.initialization_startup()
 def initialization_startup(self):
 ##############################################################################
 # #
 # СТАРТОВАЯ ПЕРВАЯ СТРАНИЦА, РАЗМЕР: 1280x750, #
 # РАЗМЕР РАМКИ: 5 px #
 # #
 ##############################################################################
 # Основа стартового окна при открытий приложения
 self.startup = CustomWidgetPng(bg_img=os.path.join(BASE_DIR, 'media', "bg_startup.png"),
color_bg=WHITE_COLOR, size_hint=(None, None), size=(1270, 745), pos_hint=(None, None), pos=(5, 5))
 def show_startup(self):
 self.screen.add_widget(self.startup)
 self.previous_page = "startup"
 def hide_startup(self):
 self.screen.remove_widget(self.startup)
# Запуск приложения
if __name__ == '__main__':
 my_app = MyApp()
 my_app.run()