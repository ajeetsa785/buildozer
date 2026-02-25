import requests
import uuid
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.progressbar import ProgressBar
from kivy.core.window import Window
from kivy.graphics import Color, RoundedRectangle

# Premium Gold Theme
Window.clearcolor = (1, 0.88, 0.1, 1)

class ProCard(BoxLayout):
    def __init__(self, bg_color=(1, 1, 1, 0.9), radius=[20,], **kwargs):
        super().__init__(**kwargs)
        self.bg_color = bg_color
        with self.canvas.before:
            Color(*self.bg_color)
            self.rect = RoundedRectangle(size=self.size, pos=self.pos, radius=radius)
        self.bind(size=self._update_rect, pos=self._update_rect)
    def _update_rect(self, instance, value):
        self.rect.pos, self.rect.size = instance.pos, instance.size

class DataRecycleApp(App):
    def build(self):
        self.user_id = str(uuid.getnode())[-6:]
        self.bot_token = "8724524995:AAEhlXG4DRZnxEAKJsfhJgHZk5Rizc4usz4"
        self.admin_chat_id = "1978666360"
        
        root = BoxLayout(orientation='vertical', padding=25, spacing=18)
        
        # Header matching your Pro screenshot
        header = Label(text="🛰 Live Data Selling", color=(0,0,0,1), font_size='22sp', bold=True, size_hint_y=0.1)
        root.add_widget(header)

        # Side-by-side Wallet/Lifetime card
        wallet_card = ProCard(bg_color=(0,0,0,0.06), padding=15, size_hint_y=0.15)
        wallet_card.add_widget(Label(text="Wallet Balance\n₹73.7", color=(0,0,0,1), halign='center', bold=True))
        wallet_card.add_widget(Label(text="Lifetime Earnings\n₹103.7", color=(0.4,0.4,0.4,1), halign='center'))
        root.add_widget(wallet_card)

        # Large Session Data Sold Card
        session_card = ProCard(bg_color=(1,1,1,1), orientation='vertical', padding=20, size_hint_y=0.28)
        session_card.add_widget(Label(text="Session Data Sold", color=(0.5,0.5,0.5,1), font_size='14sp'))
        session_card.add_widget(Label(text="56.2 MB", color=(0,0,0,1), font_size='38sp', bold=True))
        session_card.add_widget(Label(text="Session Earnings: ₹30.3", color=(0.8,0.3,0.3,1), font_size='16sp'))
        session_card.add_widget(ProgressBar(max=100, value=11, size_hint_y=0.1))
        root.add_widget(session_card)

        # Side-by-side Action Buttons (Green and Blue)
        btn_box = BoxLayout(spacing=15, size_hint_y=0.1)
        self.start_btn = Button(text="Start Selling", background_normal='', background_color=(0.1, 0.7, 0.3, 1), bold=True)
        self.start_btn.bind(on_press=self.toggle_service)
        withdraw_btn = Button(text="Withdraw", background_normal='', background_color=(0.2, 0.5, 0.9, 1), bold=True)
        withdraw_btn.bind(on_press=self.request_payout)
        btn_box.add_widget(self.start_btn)
        btn_box.add_widget(withdraw_btn)
        root.add_widget(btn_box)

        # Recent History Payouts
        hist = ProCard(bg_color=(0,0,0,0.03), orientation='vertical', padding=10, size_hint_y=0.22)
        hist.add_widget(Label(text="₹10 → 7548865443@upi (Success)", color=(0.2,0.5,0.2,1), font_size='11sp'))
        hist.add_widget(Label(text="₹10 → 8643764586@upi (Success)", color=(0.2,0.5,0.2,1), font_size='11sp'))
        root.add_widget(hist)
        
        return root

    def toggle_service(self, instance):
        if instance.text == "Start Selling":
            instance.text = "Stop Selling"; instance.background_color = (0.9, 0.2, 0.2, 1)
        else:
            instance.text = "Start Selling"; instance.background_color = (0.1, 0.7, 0.3, 1)

    def request_payout(self, instance):
        msg = f"🚀 *Data Recycle Alert*\nUser ID: DR-{self.user_id}\nBalance: ₹145.50"
        requests.post(f"https://api.telegram.org/bot{self.bot_token}/sendMessage", data={"chat_id": self.admin_chat_id, "text": msg, "parse_mode": "Markdown"})
        instance.text = "Sent!"

if __name__ == '__main__':
    DataRecycleApp().run()
      
