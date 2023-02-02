from rest_framework import generics, status, permissions
from adminapp.serializer.appaddserializer import ApplicationSerializer
from adminapp.models import Application
from rest_framework.response import Response
from api.permissionclass.permission import IsR3orR1User, IsR2orR1User
from datetime import datetime
from django.http import HttpResponse
import xlwt
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

class Dashboard(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, IsR2orR1User]
    def get(self, request):
        data = request.data
        if 'fromdate' in data and 'todate' in data:
            fromdate = data['fromdate']
            todate = data['todate']
            items = Application.objects.filter(app_status = 'Approved', dateapplied__gte = fromdate, dateapplied__lte = todate).order_by('-dateapplied')
            count = Application.objects.filter(app_status = 'Approved', dateapplied__gte = fromdate, dateapplied__lte = todate).count()
            serializer = ApplicationSerializer(instance=items, many=True)
            context = {
                'items' : serializer.data,
                'count' : count,
                'datefrom':fromdate,
                'dateto':todate
            }
            return Response(context, status=status.HTTP_200_OK)
        else:
            items = Application.objects.filter(app_status = 'Approved').order_by('-dateapplied')
            count = Application.objects.filter(app_status = 'Approved').count()
            serializer = ApplicationSerializer(instance=items, many=True)
            context = {
                'items' : serializer.data,
                'count' : count
            }
            return Response(context, status=status.HTTP_200_OK)

class DownloadReport(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, IsR2orR1User]
    def get(self, request, fromdate, todate):
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment;filename=SalesReport' +\
            str(datetime.now())+'.xls'
        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('SalesReport')
        row_num = 0
        font_style = xlwt.XFStyle()
        font_style.font.bold = True
        columns = ['first_name','phone', 'address', 'country']
        for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], font_style)
        font_style = xlwt.XFStyle()

        if fromdate != 'none' and todate != 'none':
            rows = Application.objects.filter(app_status = 'Approved', dateapplied__gte = fromdate, dateapplied__lte = todate).values_list('first_name','phone', 'address', 'country').order_by('-dateapplied')
        else:
            rows = Application.objects.filter(app_status = 'Approved').values_list('first_name','phone', 'address', 'country').order_by('-dateapplied')
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                    ws.write(row_num, col_num, row[col_num], font_style)
        
        wb.save(response)
        return response

class UserApplication(generics.CreateAPIView):
    serializer_class = ApplicationSerializer

class getUserApplication(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, IsR2orR1User]
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

    def get(self, request, **kwargs):
        queryset = self.get_queryset()
        serializer_class = ApplicationSerializer(queryset, many=True)
        for key in kwargs:
            if key == 'pk':
                queryset = Application.objects.get(id=kwargs[key])
                serializer_class = ApplicationSerializer(instance=queryset)
                return Response(serializer_class.data, status=status.HTTP_200_OK)
            elif key == 'value':
                if kwargs[key] == 'approved' or kwargs[key] == 'denied':
                    queryset = Application.objects.filter(app_status__icontains=kwargs[key])
                    serializer_class = ApplicationSerializer(instance=queryset, many=True)
                    return Response(serializer_class.data, status=status.HTTP_200_OK)
                else:
                    return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(serializer_class.data, status=status.HTTP_200_OK)


class getPendingApps(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, IsR3orR1User]
    def get(self, request):
        queryset = Application.objects.filter(app_status__icontains='Pending')
        serializer_class = ApplicationSerializer(instance=queryset, many=True)
        return Response(serializer_class.data, status=status.HTTP_200_OK)


class ChangeStatus(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsR3orR1User]
    def put(self, request, value, pk):
        self.queryset = Application.objects.get(id=pk)
        if value == 'approved':
            self.queryset.app_status = 'Approved'
            subject = f'Approval of Marriage application'
            message = f'Hello, Your application got approved {self.queryset.first_name} ({self.queryset.id})'
            recipient = self.queryset.email
            send_mail(subject, 
              message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
        elif value == 'denied':
            self.queryset.app_status = 'Denied'
            subject = f'Denied of Marriage application'
            message = f'Hello, Your application got denied {self.queryset.first_name} ({self.queryset.id}) sorry for the inconvinence'
            recipient = self.queryset.email
            send_mail(subject, 
              message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
        self.queryset.save()
        serializer = ApplicationSerializer(instance=self.queryset)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)





