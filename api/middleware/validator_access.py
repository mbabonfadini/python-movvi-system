from django.http import JsonResponse
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed

class AccessTokenMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        auth_header = request.headers.get('Authorization')
        print("Middleware AccessTokenMiddleware chamado")

        if auth_header and auth_header.startswith('Bearer '):
            token = auth_header.split(' ')[1]
            print(f"Token encontrado: {token}")  # Aqui você imprime o token encontrado
            
            try:
                # Valida o token e obtém o usuário
                user, _ = JWTAuthentication().authenticate(request)
                if user is None:
                    return JsonResponse({'detail': 'Token inválido ou expirado.'}, status=401)
            except AuthenticationFailed:
                return JsonResponse({'detail': 'Token inválido ou expirado.'}, status=401)

        # Processa a requisição
        response = self.get_response(request)
        return response