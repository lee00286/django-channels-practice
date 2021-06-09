from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import chat.routing

application = ProtocolTypeRouter({ # 어떤 타입의 연결인지 구분
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack( # WebSocket 연결일 경우
        URLRouter(
            chat.routing.websocket_urlpatterns # chat/routing.py와 연결
        )
    ),
})