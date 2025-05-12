from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from source.apps.level.utils import create_glucose_records


class GlucoseLevelView(APIView):
    def get(self, request, user_id=None):
        if user_id:
            pass
        else:
            pass

    def post(self, request):
        una_file = request.FILES.get("file")
        if not una_file:
            return Response(
                data={"error": "No file founded"}, status=status.HTTP_400_BAD_REQUEST
            )

        if not una_file.name.endswith(".csv"):
            return Response(
                data={"error": "File type not supported. Please upload a CSV file."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        records_created = create_glucose_records(una_file=una_file)
        return Response(
            data={"message": f"{records_created} records created"},
            status=status.HTTP_201_CREATED,
        )
