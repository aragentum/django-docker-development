from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK


@csrf_exempt
@api_view(["GET"])
def sample_api(request):
    data = {"sample_data": 123}
    return Response(data, status=HTTP_200_OK)
