from rest_framework import viewsets, generics
from escola.models import Curso,Aluno, Matricula
from escola.serializer import AlunoSerializer, AlunoSerializerV2, CursoSerializer, MatriculaSerializer, ListaMatriculasAlunoSerializer, ListaAlunosMatriculadosSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions


# Create your views here.

class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos e alunas"""
    queryset = Aluno.objects.all()

    def get_serializer_class(self):
        if self.request.version == 'V2':
            return AlunoSerializerV2
        else:
            return AlunoSerializer

    
    authentication_class = [BasicAuthentication]
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    authentication_class = [BasicAuthentication]
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

class MatriculasViewSet(viewsets.ModelViewSet):
    """Exibindo todas as Matriculas"""
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    authentication_class = [BasicAuthentication]
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

class ListaMatriculasAluno(generics.ListAPIView):
    """Listando as matriculas de um aluno"""
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id =self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasAlunoSerializer
    authentication_class = [BasicAuthentication]
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

class ListaAlunosMatriculados(generics.ListAPIView):
    """Listando os alunos matriculados em um curso"""
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id =self.kwargs['pk'])
        return queryset
    serializer_class = ListaAlunosMatriculadosSerializer
    authentication_class = [BasicAuthentication]
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
