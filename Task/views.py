from rest_framework.views import APIView
from rest_framework.response import Response

class View(APIView):
    def get(self, *args, **kwargs):
        data={"slackUsername":'Goodness Mbakara',
        'backend':True,
        'age': 19,
        'bio':'a futuristic software engineer'}
        return Response(data)
