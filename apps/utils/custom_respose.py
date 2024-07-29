
from rest_framework.response import Response


def response(status, data):
    return Response({"status":status, "data":data})