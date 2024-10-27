import os
from django.core.wsgi import get_wsgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server_project.settings')

application = get_wsgi_application()

# Start gRPC server
from core.grpc_server import serve
import threading
grpc_thread = threading.Thread(target=serve, daemon=True)
grpc_thread.start()