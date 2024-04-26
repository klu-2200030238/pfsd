from django.urls import path
from .views import *

urlpatterns = [
    path("mainpage/", mymainpage, name='mainpage'),
    path("signup/", signup_view, name='signup'),
    path("signin/",login_view,name="signin"),
    path("about/",myabout,name="about"),
    path("contact/",mycontact,name="contact"),
    path("festivals/",myfestivals,name="festivals"),
    path("cultures/",mycultures,name="cultures"),
    path("traditions/",mytraditions,name="traditions"),
    path("unsolvedmysteries/",myunsolvedmysteries,name="unsolvedmysteries"),
    path("hangingpillars/", myhangingpillars, name="hangingpillars"),
    path("magnetichill/", mymagnetichill, name="magnetichill"),
    path("padmanabhaswamytemple/", mypadmanabhaswamytemple, name="padmanabhaswamytemple"),
    path("roopkundskeletonlake/", myroopkundskeletonlake, name="roopkundskeletonlake"),
    path("ganeshchaturthi/",myganeshchaturthi,name="ganeshchaturthi"),
    path("diwali",mydiwali,name="diwali"),
    path("ramadan",myramadan,name="ramadan"),
    path("christmas",mychristmas,name="christmas"),
    path("traditions",mytraditions,name="traditions"),
    path("north/",mynorth,name="north"),
    path("south/",mysouth,name="south"),
    path("east/",myeast,name="east"),
    path("west/",mywest,name="west"),
    path("joint/",myjoint,name="joint"),
    path("kathakali/",mykathakali,name="kathakali"),
    path("kerala/",mykerala,name="kerala"),
    path("manipur/",mymanipur,name="manipur"),
    path("historical/", myhistorical, name="historical"),
    path("agra/", myagra, name="agra"),
    path("ellora/", myellora, name="ellora"),
    path("redfort/", myredfort, name="redfort"),
    path("gateway/", mygateway, name="gateway"),


]
