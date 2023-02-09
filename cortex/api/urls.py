from django.urls import path
from .views import ArtistCatalogView
from .views import ArtistCreateView
from .views import SongCreateView
from .views import AlbumCreateView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="Api",
        default_version='v1',
        description="test api description",
    ),
    public=True
)

urlpatterns = [
    path('catalog/', ArtistCatalogView.as_view()),
    path('artist/create/', ArtistCreateView.as_view()),
    path('song/create/', SongCreateView.as_view()),
    path('album/create/', AlbumCreateView.as_view()),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]