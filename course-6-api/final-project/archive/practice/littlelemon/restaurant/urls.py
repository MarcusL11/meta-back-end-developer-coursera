from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from django.conf.urls import include



urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('book/', views.book, name="book"),
    path('menu/', views.menu, name='menu'),
    path('menu_item/<int:pk>/', views.display_menu_items, name='menu_item'),
    
    # User registration and token generation endpoints 
    path('api/users', views.create_user, name='create_user'),
    path('api/users/all', views.show_all_users, name='show_all_users'),
    path('api/users/users/me', views.show_user, name='show_user'),
    
    # Menu-items endpoints
    path('api/menu-items', views.menu_items, name='menu_items'),
    path('api/menu-items/<int:menu_id>', views.single_menu_item, name='single_items'),

    # User group management endpoints
    path('api/groups/manager/users', views.manager_set, name='get_assign_user_to_manager_group'),
    path('api/groups/manager/users/<int:user_id>', views.manage_delete, name='delete_user_from_manager_group'),
    path('api/groups/delivery-crew/users', views.delivery_crew_set, name='get_assign_user_to_delivery_crew_group'),
    path('api/groups/delivery-crew/users/<int:user_id>', views.delivery_crew_delete, name='delete_user_from_delivery_crew_group'),
 
    # Cart management endpoints
    path('api/cart/menu-items', views.cart_set, name='cart_items'),
    
    # Order Management endpoints
    path('api/orders', views.order_set, name='order_items'),
    path('api/orders/<int:order_id>', views.order_item, name='order_item'),
    
    # Other URLS
    path('api/category-items/', views.category_items, name='category_items'),
    path('api/menu-of-the-day/<int:menu_id>', views.menu_of_day, name='menu_of_the_day'),

    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),



    # path('api/menu-items/', views.MenuView.as_view(), name='menu_items'), # if using CLASS BASED VIEW
    # path('api/menu-items/<int:pk>/', views.SingleMenuView.as_view(), name='single_items'), # if using CLASS BASED VIEW
]