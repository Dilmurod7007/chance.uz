from rest_framework import  status
from rest_framework import generics
from .models import University

from .serializers import AddSponsorSerializer, SponsorSerializer, StudentsSerializer, TokenObtainSerializer
from .models import PERSONAL_CHOICES, STATUS_CHOICES, STUDENT_CHOICES, Contract, Sponsor, Student
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView as TokenObtainView





class StudentsView(generics.ListAPIView):
    serializer_class = StudentsSerializer
    queryset = Student.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['degree', 'university']  


class StudentCreateView(generics.CreateAPIView):
    serializer_class = StudentsSerializer
    queryset = Student.objects.all()
    permission_classes = [IsAuthenticated]


class StudentEditView(generics.UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentsSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'
    


class StudentDetailView(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentsSerializer
    permission_classes = [IsAuthenticated]
    lookup_filed = "pk"



class SponsorsView(generics.ListAPIView):
    serializer_class = SponsorSerializer
    queryset = Sponsor.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['amount', 'status', 'created']


class SponsorCreateView(generics.CreateAPIView):
    serializer_class = SponsorSerializer
    queryset = Sponsor.objects.all()

        
class SponsorEditView(generics.UpdateAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def put(self, request, pk):
        sponsor = Sponsor.objects.get(pk=pk)
        serializer = SponsorSerializer(sponsor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            if sponsor.status != 'Declained':
                sponsor.status = "Approved"
                sponsor.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SponsorDetailView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        sponsor = Sponsor.objects.get(pk=pk)
        serializer = SponsorSerializer(sponsor)
        if sponsor.status == "New":
            sponsor.status = "Moderated"
            sponsor.save()
        return Response(serializer.data)
        


class DashboardView(APIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [JSONRenderer]
    def get(self, request, format=None):
        students = Student.objects.all()
        sponsors = Sponsor.objects.all()
        money_needed = 0
        money_gained = 0
        for i in students:
            money_needed += i.money_needed
            money_gained += i.money_gained

        money_required = money_needed - money_gained

        statistics = {}
        sponsors_number = 0
        students_number = 0

        for i in range(12):
            statistic_arr = []
            sponsors_number = 0
            students_number = 0
            for k in sponsors:
                if k.created.month <= i+1:
                    sponsors_number += 1

            for j in students:
                if j.created.month <= i+1:
                    students_number += 1

            statistic_arr.append(sponsors_number)
            statistic_arr.append(students_number)

            statistics[i+1] = statistic_arr

        content = {
                    'money_neede': money_needed,
                    'money_gained': money_gained,
                    'money_required': money_required,
                    'month: [number_of_sponsors, number_of_studant]': statistics
        }
        return Response(content)


class LstView(APIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [JSONRenderer]
    def get(self, request, format=None):
        university = University.objects.all()
        university_list = []
   
        for i in university:
            university_list.append(i.name)

        print(university_list)

        money_arr = [1000000, 5000000, 7000000, 30000000]
        content = {'Universities': university_list,
                    'Degree_choices': STUDENT_CHOICES,
                    'Personal_choices': PERSONAL_CHOICES,
                    'Status_choices': STATUS_CHOICES,
                    'Money_choices': money_arr,
        }
        return Response(content)



class AddSponsorView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AddSponsorSerializer
    queryset = Contract.objects.all()

    def post(self, request, id):
        serializer = AddSponsorSerializer(data=request.data)
        student = Student.objects.get(id=id)
        if serializer.is_valid():
            sponsor = serializer.validated_data['sponsor']
            money = serializer.validated_data['money']
            if (int(sponsor.amount) - int(sponsor.paid)) >= money:
                if money <= (student.money_needed - student.money_gained):
                    student.money_gained += money
                    sponsor.paid += money
                    student.save()
                    sponsor.save()
                    serializer.validated_data['student'] = student
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                else:
                    return Response("Student needs only "+str(student.money_needed-student.money_gained), status=status.HTTP_406_NOT_ACCEPTABLE)
            return Response("Not Enough Money", status=status.HTTP_406_NOT_ACCEPTABLE)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class MyObtainTokePairListApiView(TokenObtainView):
    permission_classes = [AllowAny,]
    serializer_class = TokenObtainSerializer


