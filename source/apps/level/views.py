from rest_framework.views import APIView


class GlucoseLevelView(APIView):
    def get(self, request, user_id=None):
        if user_id:
            pass
        else:
            pass

    def post(self, request):
        pass
