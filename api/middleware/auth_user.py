from rest_framework_simplejwt.tokens import RefreshToken
from ..models import UsuarioRole

class TokenMiddleware:
    
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def create_token(self, usuario):
        refresh = RefreshToken.for_user(usuario)
        
        # Busca as roles associadas ao usuário
        roles = UsuarioRole.objects.filter(usuario=usuario).select_related('role')

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'id': usuario.id,
            'nome': usuario.nome,
            'sobrenome': usuario.sobrenome,
            'cargo': usuario.cargo.descricao,  # Ajuste conforme o modelo
            'setor': usuario.setor.descricao,    # Ajuste conforme o modelo
            'roles': [usuario_role.role.descricao for usuario_role in roles]  # Obtém as descrições das roles
        }