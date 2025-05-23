from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from source.apps.level.models import GlucoseRecord, UnaUser
from source.apps.level.pagination import CustomPageNumberPagination
from source.apps.level.serializers import GlucoseRecordSerializer
from source.apps.level.utils import create_glucose_records, glucose_records_filtered


class GlucoseLevelView(APIView):
    serializer_class = GlucoseRecordSerializer

    def get(self, request, user_id=None, id=None):
        if id:
            glucose_record = GlucoseRecord.objects.filter(id=id).first()
            if not glucose_record:
                return Response(data={"Error": "Glucose record not found"})
            glucose_record_data = GlucoseRecordSerializer(glucose_record).data
            return Response(data=glucose_record_data, status=status.HTTP_200_OK)

        una_user = UnaUser.objects.filter(una_id=user_id).first()
        if not una_user:
            return Response(data={"Error": "User not found"})

        glucose_records = una_user.glucose_records.all()
        params = request.query_params
        glucose_records = glucose_records_filtered(
            glucose_records=glucose_records, params=params
        )

        paginator = CustomPageNumberPagination()
        paginated_queryset = paginator.paginate_queryset(glucose_records, request)

        glucose_records_data = GlucoseRecordSerializer(
            paginated_queryset, many=True
        ).data
        return Response(data=glucose_records_data, status=status.HTTP_200_OK)

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
