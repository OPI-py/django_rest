from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from snippets.views import SnippetViewSet, UserViewSet, api_root
from rest_framework import renderers
from snippets import views
from rest_framework.routers import DefaultRouter


snippet_list = SnippetViewSet.as_view({
	'get': 'list',
	'post': 'create'
	})

snippet_detail = SnippetViewSet.as_view({
	'get': 'retrieve',
	'put': 'update',
	'patch': 'partial_update',
	'delete': 'destroy'
	})

user_list = UserViewSet.as_view({
	'get': 'list'
	})

user_detail = UserViewSet.as_view({
	'get': 'retrieve'
	})


router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns = format_suffix_patterns([
    path('', api_root),
    path('snippets/', snippet_list,	name='snippet-list'),
    path('snippets/<int:pk>/', snippet_detail, name='snippet-detail'),
    path('users/', user_list, name='user-list'),
    path('users/<int:pk>/', user_detail, name='user-detail'),
])