from django.contrib import admin
from .models import Usuario, Filial, Status, Setor, Cargo, Role, UsuarioRole, TipoSenha, TipoOperacaoFrete, SolicitacaoTipo, Solicitacao, SolicitacaoSenha, SolicitacaoSenhaChave, Aprovacao, RegraAprovacao


class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'filial')
    search_fields = ('nome', 'email')
    list_filter = ('filial',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(fn_filial_id=request.user.fn_filial_id)

class FilialAdmin(admin.ModelAdmin):
    list_display = ('sigla', 'nome')
    search_fields = ('nome',)

# Personalizados
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Filial, FilialAdmin)

# Modelos

admin.site.register(Status)
admin.site.register(Setor)
admin.site.register(Cargo)
admin.site.register(Role)
admin.site.register(UsuarioRole)
admin.site.register(TipoSenha)
admin.site.register(TipoOperacaoFrete)
admin.site.register(SolicitacaoTipo)
admin.site.register(Solicitacao)
admin.site.register(SolicitacaoSenha)
admin.site.register(SolicitacaoSenhaChave)
admin.site.register(Aprovacao)
admin.site.register(RegraAprovacao)