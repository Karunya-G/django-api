from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from django.conf.urls.static import static
from django.conf import settings


    ## define a router variable
router = DefaultRouter()

    ## register here
# router.register('annoteapi',views.AnnoteViewSet, basename='anno')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('listget/',views.AnnoteListCreate.as_view()),
    path('putpatch/<int:pk>',views.AnnoteRetrieveUpdateDestroy.as_view()),
    path('imglistget/',views.ImageListCreate.as_view()),
    path('imgputpatch/<int:pk>',views.ImageRetrieveUpdateDestroy.as_view()),
    # path('',include(router.urls)),
    path('gettoken/',TokenObtainPairView.as_view(), name= 'token_pair'),
    path('refreshtoken/', TokenRefreshView.as_view(), name= 'token_resfresh'),
    path('verifytoken/',TokenVerifyView.as_view(), name= 'token_verify'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)