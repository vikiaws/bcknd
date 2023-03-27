from django.shortcuts import render
from .models import Beeline,Profile
from rest_framework import generics 
from book.serializers import BeelineSerializer,ProfileSerializer,UserSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser,FormParser
import json 
from django.http import HttpResponse,Http404
from django.core.mail import BadHeaderError,send_mail
from django.contrib.auth import authenticate
from rest_framework import viewsets
from django.contrib.auth.models import User
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BeelineListView(generics.ListCreateAPIView):
    queryset = Beeline.objects.all()
    serializer_class = BeelineSerializer

    parser_classes = [MultiPartParser,FormParser]
    def post(self,request):
        if request.data['file']=="undefined":
            data1=request.data['User']
            data = json.loads(data1)
            # data = {'beeLine_Request_Number':data2['beeLine_Request_Number'],'job_description':data2['job_description'],'department':data2['department'],'no_of_positions':data2['no_of_positions'],'priority':data2['priority'],'cv_DeadLine':data2['cv_DeadLine'],'billing_Rate':data2['billing_Rate'],'hours_per_week':data2['hours_per_week'],'contact_person':data2['contact_person'],'date_request':data2['date_request'],'file':data3}
        else:
            data1 = request.data['User']
            data3 = request.data['file']
            print(data3)
            data2 = json.loads(data1)
            print(data2['beeLine_Request_Number'])
            data = {'beeLine_Request_Number':data2['beeLine_Request_Number'],'job_description':data2['job_description'],'department':data2['department'],'no_of_positions':data2['no_of_positions'],'priority':data2['priority'],'status':data2['status'],'cv_DeadLine':data2['cv_DeadLine'],'billing_Rate':data2['billing_Rate'],'hours_per_week':data2['hours_per_week'],'contact_person':data2['contact_person'],'date_request':data2['date_request'],'file':data3}
        #print(data)
        serializer = BeelineSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
            




class BeelineDetailListView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Beeline.objects.all()
    serializer_class = BeelineSerializer
    parser_classes = [MultiPartParser,FormParser]

    





class ProfileListView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileDetailListView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class UpdataBeelineView(APIView):
    
    """def get(self,request):
        beeline = Beeline.objects.all()
        serializer = BeelineSerializer(beeline,many=True)
        data= serializer.data
        return Response(data)"""

    def get_object(self,pk):
        try:
            return Beeline.objects.get(pk=pk)
        except Beeline.DoesNotExist:
            raise Http404
    def patch(self,request,pk):
        beeline=self.get_object(pk)
        if(request.data['file']=="undefined"):
            data1 = request.data['User']
            dict1 = json.loads(data1)
            #print(data2)
            #data = {'file':""}
            data2 = BeelineSerializer(beeline)
            data3 = data2.data
            dict2 = dict(data3)
            if dict2['file'] is None:
                print("yes")
                new = {}
                for item in dict1.keys():
                    if dict1[item]!=dict2[item]:
                        new[item] = dict1[item]
    
            else:

                new = {}
                for item in dict1.keys():
                    if dict1[item]!=dict2[item]:
                        new[item] = dict1[item]
                # print(new)
                new.__delitem__('file')
            #print(new)
           
        else:
            data1 = request.data['User']
            data3 = request.data['file']
            data2 = json.loads(data1)
            new ={'beeLine_Request_Number':data2['beeLine_Request_Number'],'job_description':data2['job_description'],'department':data2['department'],'no_of_positions':data2['no_of_positions'],'priority':data2['priority'],'status':data2['status'],'cv_DeadLine':data2['cv_DeadLine'],'billing_Rate':data2['billing_Rate'],'hours_per_week':data2['hours_per_week'],'contact_person':data2['contact_person'],'date_request':data2['date_request'],'file':data3}

           
        
        serializer=BeelineSerializer(beeline,data=new,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class ProfileUploadView(APIView):
    parser_classes = [MultiPartParser,FormParser]
    def post(self,request):
        if request.data['file']=="undefined":
            data1 = request.data['User']
            #data3 = request.data['file']
            #print(data3)
            data = json.loads(data1)
        else:
            data1=request.data["User"]
            data3=request.data["file"]
            data2=json.loads(data1)
            data = {'name_of_candidate':data2['name_of_candidate'],'prodapt_practice':data2['prodapt_practice'],'prodapt_POC':data2['prodapt_POC'],'current_Status':data2['current_Status'],'next_step':data2['next_step'],'dutch_Language':data2['dutch_Language'],'location_relocation':data2['location_relocation'],'experience':data2['experience'],'client_Interview':data2['client_Interview'],'comments':data2['comments'],'beeline':data2['beeline'],'cv_Attachment':data3}
        #print(data)
        serializer = ProfileSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    def get(self,request):
        profile = Profile.objects.all()
        serializer = ProfileSerializer(profile,many=True)
        data= serializer.data
        return Response(data)



class UpdataProfileView(APIView):
    
    

    def get_object(self,pk):
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            raise Http404
    def patch(self,request,pk):
        profile=self.get_object(pk)
        if(request.data['file']=="undefined"):
            data1 = request.data['User']
            dict1 = json.loads(data1)
            #print(data2)
            #data = {'file':""}
            data2 = ProfileSerializer(profile)
            data3 = data2.data
            dict2 = dict(data3)
            if dict2['cv_Attachment'] is None:

                new = {}
                for item in dict1.keys():
                    if dict1[item]!=dict2[item]:
                        new[item] = dict1[item]
            else:
                new = {}
                for item in dict1.keys():
                    if dict1[item]!=dict2[item]:
                        new[item] = dict1[item]
                del new['cv_Attachment']
            #print(new)
           
        else:
            data1 = request.data['User']
            data3 = request.data['file']
            data2 = json.loads(data1)
            #new ={'beeLine_Request_Number':data2['beeLine_Request_Number'],'job_description':data2['job_description'],'department':data2['department'],'no_of_positions':data2['no_of_positions'],'priority':data2['priority'],'cv_DeadLine':data2['cv_DeadLine'],'billing_Rate':data2['billing_Rate'],'hours_per_week':data2['hours_per_week'],'contact_person':data2['contact_person'],'date_request':data2['date_request'],'file':data3}
            new ={'name_of_candidate':data2['name_of_candidate'],'prodapt_practice':data2['prodapt_practice'],'prodapt_POC':data2['prodapt_POC'],'current_Status':data2['current_Status'],'next_step':data2['next_step'],'dutch_Language':data2['dutch_Language'],'location_relocation':data2['location_relocation'],'experience':data2['experience'],'client_Interview':data2['client_Interview'],'comments':data2['comments'],'beeline':data2['beeline'],'cv_Attachment':data3}
        """profile=self.get_object(pk)
        data1 = request.data['User']
        data3 = request.data['file']
        data2 = json.loads(data1)
        print(data2)
        #data = {'file':""}
        data ={'name_of_candidate':data2['name_of_candidate'],'prodapt_practice':data2['prodapt_practice'],'prodapt_POC':data2['prodapt_POC'],'current_Status':data2['current_Status'],'next_step':data2['next_step'],'dutch_Language':data2['dutch_Language'],'location_relocation':data2['location_relocation'],'experience':data2['experience'],'resume_Shared':data2['resume_Shared'],'client_Interview':data2['client_Interview'],'comments':data2['comments'],'beeline':data2['beeline'],'cv_Attachment':data3}"""
        serializer=ProfileSerializer(profile,data=new,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)




"""class UploadView(APIView):
    
    def post(self,request):
        data1 = request.data
        print(data1)
        #data = {'beeLine_Request_Number':data1[0]['beeLine_Request_Number'],'job_description':data1[0]['job_description'],'department':data1[0]['department'],'no_of_positions':data1[0]['no_of_positions'],'priority':data1[0]['priority'],'cv_DeadLine':data1[0]['cv_DeadLine'],'billing_Rate':data1[0]['billing_Rate'],'hours_per_week':data1[0]['hours_per_week'],'contact_person':data1[0]['contact_person'],'date_request':data1[0]['date_request'],'name':data1['file']}
        #print(data)
        #data={'name':data1['file']}
        serializer = UploadSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    def get(self,request):
        upload =Upload.objects.all()
        serializer = UploadSerializer(upload,many=True)
        data= serializer.data
        return Response(data)"""




"""class LostCountView(APIView):
     def get(self,request):
        final_dict = {}
        beeline_status_lost1 = Beeline.objects.filter(status='Lost').count()
        if beeline_status_lost1==0:
            print("yes")
            dict1 = [0,0,0,0,0,0,0,0,0]
            return Response(dict1)
        else:
            list1 = Beeline.objects.filter(status='Lost').all()
            l1=[]
            for i in range(beeline_status_lost1):
                item = BeelineSerializer(list1[i])
                item2 = item.data
                index = item2['id']
                obj1 = Beeline.objects.get(pk=index)
                obj2 = BeelineSerializer(obj1)
                obj3 = obj2.data
                obj4 = json.loads(json.dumps(obj3))
                print(len(obj4['beeline']))
                if len(obj4['beeline'])>=1:
                    print("came to second else")
                    length = len(obj4['beeline'])
                    var = obj4['beeline']
                    print(var)
                    for i in range(length):
                        obj5 = var[i]
                        print(obj5)
                        l1.append(obj5['current_Status'])
                    print(l1)
                else:
                    #dict1 = {'beeline_status_lost':int(beeline_status_lost1),'open_count':0,'fullfilled_count':0,'closed_count':0,'onhold_count':0,'Profile_Shared_count':0,'Pending_Client_Interview_count':0,'POCs_Contacted_count':0,'Awaiting_Interview_Results_count':0}
                    pass
            new_count1 = l1.count('New')
            on_hold_count1 = l1.count('Onhold')
            profile_Rejected_count1 = l1.count('Profile Rejected')
            closed_count1 = l1.count('Closed')
            Profile_Shared_count1 = l1.count('Profile Shared')
            POCs_Contacted_count1 = l1.count("POC Contacted")
            Pending_Client_Interview_count1 = l1.count('Pending Client Interview')
            Awaiting_Interview_Results_count1 = l1.count('Awaiting Interview Results')
            dict1 = [int(new_count1),int(profile_Rejected_count1),int(closed_count1),int(on_hold_count1),int(Profile_Shared_count1),int(Pending_Client_Interview_count1),int(POCs_Contacted_count1),int(Awaiting_Interview_Results_count1)]
            total_Profiles=sum(dict1)
            dict2 = [int(beeline_status_lost1),int(total_Profiles),int(new_count1),int(profile_Rejected_count1),int(closed_count1),int(on_hold_count1),int(Profile_Shared_count1),int(Pending_Client_Interview_count1),int(POCs_Contacted_count1),int(Awaiting_Interview_Results_count1)]
            return Response(dict2)


class CloseCountView(APIView):
    def get(self,request):
        final_dict = {}
        beeline_status_close1 = Beeline.objects.filter(status='Closed').count()
        if beeline_status_close1==0:
            print("yes")
            dict1 =[0,0,0,0,0,0,0,0,0]
            return Response(dict1)
        else:
            list1 = Beeline.objects.filter(status='Closed').all()
            l1=[]
            for i in range(beeline_status_close1):
                item = BeelineSerializer(list1[i])
                item2 = item.data
                index = item2['id']
                obj1 = Beeline.objects.get(pk=index)
                obj2 = BeelineSerializer(obj1)
                obj3 = obj2.data
                obj4 = json.loads(json.dumps(obj3))
                print(len(obj4['beeline']))
                if len(obj4['beeline'])>=1:
                    print("came to second else")
                    length = len(obj4['beeline'])
                    var = obj4['beeline']
                    print(var)
                    for i in range(length):
                        obj5 = var[i]
                        print(obj5)
                        l1.append(obj5['current_Status'])
                    print(l1)
                else:
                    #dict1 = {'beeline_status_lost':int(beeline_status_lost1),'open_count':0,'fullfilled_count':0,'closed_count':0,'onhold_count':0,'Profile_Shared_count':0,'Pending_Client_Interview_count':0,'POCs_Contacted_count':0,'Awaiting_Interview_Results_count':0}
                    pass
            new_count1 = l1.count('New')
            on_hold_count1 = l1.count('Onhold')
            profile_Rejected_count1 = l1.count('Profile Rejected')
            closed_count1 = l1.count('Closed')
            Profile_Shared_count1 = l1.count('Profile Shared')
            POCs_Contacted_count1 = l1.count("POC Contacted")
            Pending_Client_Interview_count1 = l1.count('Pending Client Interview')
            Awaiting_Interview_Results_count1 = l1.count('Awaiting Interview Results')
            dict1 = [int(new_count1),int(profile_Rejected_count1),int(closed_count1),int(on_hold_count1),int(Profile_Shared_count1),int(Pending_Client_Interview_count1),int(POCs_Contacted_count1),int(Awaiting_Interview_Results_count1)]
            total_Profiles=sum(dict1)
            dict2 = [int(beeline_status_close1),int(total_Profiles),int(new_count1),int(profile_Rejected_count1),int(closed_count1),int(on_hold_count1),int(Profile_Shared_count1),int(Pending_Client_Interview_count1),int(POCs_Contacted_count1),int(Awaiting_Interview_Results_count1)]
            return Response(dict2)



class FullfilledCountView(APIView):
    def get(self,request):
        final_dict = {}
        beeline_status_fulfilled1 = Beeline.objects.filter(status='Fulfilled').count()
        print(beeline_status_fulfilled1)
        if beeline_status_fulfilled1==0:
            print("yes")
            dict1 =[0,0,0,0,0,0,0,0,0] 
            return Response(dict1)
        else:
            list1 = Beeline.objects.filter(status='Fulfilled').all()
            l1=[]
            for i in range(beeline_status_fulfilled1):
                item = BeelineSerializer(list1[i])
                item2 = item.data
                index = item2['id']
                obj1 = Beeline.objects.get(pk=index)
                obj2 = BeelineSerializer(obj1)
                obj3 = obj2.data
                obj4 = json.loads(json.dumps(obj3))
                print(len(obj4['beeline']))
                if len(obj4['beeline'])>=1:
                    print("came to second else")
                    length = len(obj4['beeline'])
                    var = obj4['beeline']
                    print(var)
                    for i in range(length):
                        obj5 = var[i]
                        print(obj5)
                        l1.append(obj5['current_Status'])
                    print(l1)
                    #print(dict1)
                else:
                    #dict1 = {'beeline_status_lost':int(beeline_status_lost1),'open_count':0,'fullfilled_count':0,'closed_count':0,'onhold_count':0,'Profile_Shared_count':0,'Pending_Client_Interview_count':0,'POCs_Contacted_count':0,'Awaiting_Interview_Results_count':0}
                    pass
            new_count1 = l1.count('New')
            on_hold_count1 = l1.count('Onhold')
            profile_Rejected_count1 = l1.count('Profile Rejected')
            closed_count1 = l1.count('Closed')
            Profile_Shared_count1 = l1.count('Profile Shared')
            POCs_Contacted_count1 = l1.count("POC Contacted")
            Pending_Client_Interview_count1 = l1.count('Pending Client Interview')
            Awaiting_Interview_Results_count1 = l1.count('Awaiting Interview Results')
            dict1 = [int(new_count1),int(profile_Rejected_count1),int(closed_count1),int(on_hold_count1),int(Profile_Shared_count1),int(Pending_Client_Interview_count1),int(POCs_Contacted_count1),int(Awaiting_Interview_Results_count1)]
            total_Profiles=sum(dict1)
            dict2 = [int(beeline_status_fulfilled1),int(total_Profiles),int(new_count1),int(profile_Rejected_count1),int(closed_count1),int(on_hold_count1),int(Profile_Shared_count1),int(Pending_Client_Interview_count1),int(POCs_Contacted_count1),int(Awaiting_Interview_Results_count1)]
            return Response(dict2)"""

"""class OpenCountView(APIView):
    def get(self,request):
        final_dict = {}
        beeline_status_open1 = Beeline.objects.filter(status='Open').count()
        print(beeline_status_open1)
        if beeline_status_open1==0:
            print("yes")
            dict1 =[0,0,0,0,0,0,0,0,0] 
            return Response(dict1)
        else:
            list1 = Beeline.objects.filter(status='Open').all()
            l1=[]
            for i in range(beeline_status_open1):
                item = BeelineSerializer(list1[i])
                item2 = item.data
                index = item2['id']
                obj1 = Beeline.objects.get(pk=index)
                obj2 = BeelineSerializer(obj1)
                obj3 = obj2.data
                obj4 = json.loads(json.dumps(obj3))
                print(len(obj4['beeline']))
                if len(obj4['beeline'])>=1:
                    print("came to second else")
                    length = len(obj4['beeline'])
                    var = obj4['beeline']
                    print(var)
                    for i in range(length):
                        obj5 = var[i]
                        print(obj5)
                        l1.append(obj5['current_Status'])
                    print(l1)
                    #print(dict1)
                else:
                    #dict1 = {'beeline_status_lost':int(beeline_status_lost1),'open_count':0,'fullfilled_count':0,'closed_count':0,'onhold_count':0,'Profile_Shared_count':0,'Pending_Client_Interview_count':0,'POCs_Contacted_count':0,'Awaiting_Interview_Results_count':0}
                    pass
            new_count1 = l1.count('New')
            on_hold_count1 = l1.count('Onhold')
            profile_Rejected_count1 = l1.count('Profile Rejected')
            closed_count1 = l1.count('Closed')
            Profile_Shared_count1 = l1.count('Profile Shared')
            POCs_Contacted_count1 = l1.count("POC Contacted")
            Pending_Client_Interview_count1 = l1.count('Pending Client Interview')
            Awaiting_Interview_Results_count1 = l1.count('Awaiting Interview Results')
            dict1 = [int(new_count1),int(profile_Rejected_count1),int(closed_count1),int(on_hold_count1),int(Profile_Shared_count1),int(Pending_Client_Interview_count1),int(POCs_Contacted_count1),int(Awaiting_Interview_Results_count1)]
            total_Profiles=sum(dict1)
            dict2 = [int(beeline_status_open1),int(total_Profiles),int(new_count1),int(profile_Rejected_count1),int(closed_count1),int(on_hold_count1),int(Profile_Shared_count1),int(Pending_Client_Interview_count1),int(POCs_Contacted_count1),int(Awaiting_Interview_Results_count1)]
            return Response(dict2)"""

class OverallCount(APIView):
    def get(self,request):
        beeline_status_lost1 = Beeline.objects.filter(status='Lost').count()
        beeline_status_close1 = Beeline.objects.filter(status='Closed').count()
        beeline_status_fulfilled1 = Beeline.objects.filter(status='Fulfilled').count()
        beeline_status_open1 = Beeline.objects.filter(status='Open').count()
        dict1 = [(beeline_status_open1),(beeline_status_fulfilled1),(beeline_status_close1),(beeline_status_lost1)]
        return Response(dict1)

class LoginView(APIView):
    permission_classes=[]
    def post(self,request):
       
        email = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=email,password=password)
        if user is not None:
            #response = {"message":"Login succes"}
            if(user.is_superuser):
                userName = User.objects.get(username=email)
                data1 = UserSerializer(userName)
            
                user = data1.data['username']
                
                return Response(["Admin",user])
            else:
                userName = User.objects.get(username=email)
                data1 = UserSerializer(userName)
                
                #user = json.loads(json.dumps(data1))
                print(data1.data)
                user = data1.data['username']
                return Response(["User",user])
            
        else:
            return Response("not valid")
        


class OverallProfileCount(APIView):
    def get(self,request):
        profile_status_new = Profile.objects.filter(current_Status='New').count()
        profile_status_onhold = Profile.objects.filter(current_Status='Onhold').count()
        profile_status_profileshared = Profile.objects.filter(current_Status='Profile Shared').count()
        profile_status_profilerejected = Profile.objects.filter(current_Status='Profile Rejected').count()
        profile_status_pocontacted = Profile.objects.filter(current_Status='POC Contacted').count()
        profile_status_pedclientint=Profile.objects.filter(current_Status='Pending Client Interview').count()
        profile_status_awaitintresults=Profile.objects.filter(current_Status='Awaiting Interview Results').count()
        profile_status_closed=Profile.objects.filter(current_Status='Closed').count()
        #print(profile_status_pedclientint)
        dict1 = [int(profile_status_new),int(profile_status_onhold),int(profile_status_profileshared),int(profile_status_profilerejected),int(profile_status_pocontacted),int(profile_status_pedclientint),int(profile_status_awaitintresults),int(profile_status_closed)]
        #print(dict1)
        total=sum(dict1)
        #print(total)
        dict1.insert(0,total)
        return Response(dict1)


class LostCountView(APIView):
     def get(self,request):
        final_dict = []
        beeline_status_lost1 = Beeline.objects.filter(status='Lost').count()
        if beeline_status_lost1==0:
            print("yes")
            #dict1 = {'beeline_status_lost':0,'open_count':0,'fullfilled_count':0,'closed_count':0,'onhold_count':0,'Profile_Shared_count':0,'Pending_Client_Interview_count':0,'POCs_Contacted_count':0,'Awaiting_Interview_Results_count':0}
            dict1 = [0, [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],0]
            return Response(dict1)
        else:
            list1 = Beeline.objects.filter(status='Lost').all()
            l1=[]
            l2=[]
            for i in range(beeline_status_lost1):
                item = BeelineSerializer(list1[i])
                item2 = item.data
                index = item2['id']
                obj1 = Beeline.objects.get(pk=index)
                obj2 = BeelineSerializer(obj1)
                obj3 = obj2.data
                obj4 = json.loads(json.dumps(obj3))
                print(len(obj4['beeline']))
                if len(obj4['beeline'])>=1:
                    print("came to second else")
                    length = len(obj4['beeline'])
                    var = obj4['beeline']
                    print(var)
                    for i in range(length):
                        obj5 = var[i]
                        print(obj5)
                        l1.append(obj5['current_Status'])
                        l2.append(obj5['prodapt_practice'])
                    print(l1)
                    print(l2)
                    sf_count = []
                    cad_count = []
                    nw_count = []
                    infra_count = []
                    asm_count = []
                    coo_count=[]
                    final = list(zip(l1,l2))
                    for i in final:
                        if i[1]=="SF Practice":
                            sf_count.append(i)
                        elif i[1]=="CAD":
                            cad_count.append(i)
                        elif i[1]=="NW Practice":
                            nw_count.append(i)
                        elif i[1]=="Infra Practice":
                            infra_count.append(i)  
                        elif i[1]=="ASM Practice":
                            asm_count.append(i)
                        elif i[1]=="COO-TOPS Practice":
                            coo_count.append(i)                          
                    sf = []
                    for i in sf_count:
                        sf.append(i[0])
                    print(sf)
                    cad = []
                    for i in cad_count:
                        cad.append(i[0])
                    print(cad)
                    nw = []
                    for i in nw_count:
                        nw.append(i[0])
                    print(nw)
                    infra = []
                    for i in infra_count:
                        infra.append(i[0])
                    print(infra)
                    asm = []
                    for i in asm_count:
                        asm.append(i[0])
                    print(asm)
                    coo = []
                    for i in coo_count:
                        coo.append(i[0])
                    print(coo)
        open_count1 = sf.count('New')
        on_hold_count1 = sf.count('Onhold')
        fullfilled_count1 = sf.count('Profile Rejected')
        closed_count1 = sf.count('Closed')
        Profile_Shared_count1 = sf.count('Profile Shared')
        POCs_Contacted_count1 =sf.count("POC Contacted")
        Pending_Client_Interview_count1 = sf.count('Pending Client Interview')
        Awaiting_Interview_Results_count1 = sf.count('Awaiting Interview Results')
        dict1 = [open_count1,on_hold_count1,fullfilled_count1,closed_count1,Profile_Shared_count1,POCs_Contacted_count1,Pending_Client_Interview_count1,Awaiting_Interview_Results_count1]
        final_dict.append(dict1)
        open_count1 = cad.count('New')
        on_hold_count1 =cad.count('Onhold')
        fullfilled_count1 = cad.count('Profile Rejected')
        closed_count1 = cad.count('Closed')
        Profile_Shared_count1 = cad.count('Profile Shared')
        POCs_Contacted_count1 =cad.count("POC Contacted")
        Pending_Client_Interview_count1 = cad.count('Pending Client Interview')
        Awaiting_Interview_Results_count1 = cad.count('Awaiting Interview Results')
        dict1 = [open_count1,on_hold_count1,fullfilled_count1,closed_count1,Profile_Shared_count1,POCs_Contacted_count1,Pending_Client_Interview_count1,Awaiting_Interview_Results_count1]
        final_dict.append(dict1)

        open_count1 = nw.count('New')
        on_hold_count1 = nw.count('Onhold')
        fullfilled_count1 = nw.count('Profile Rejected')
        closed_count1 = nw.count('Closed')
        Profile_Shared_count1 = nw.count('Profile Shared')
        POCs_Contacted_count1 =nw.count("POC Contacted")
        Pending_Client_Interview_count1 = nw.count('Pending Client Interview')
        Awaiting_Interview_Results_count1 = nw.count('Awaiting Interview Results')
        dict1 = [open_count1,on_hold_count1,fullfilled_count1,closed_count1,Profile_Shared_count1,POCs_Contacted_count1,Pending_Client_Interview_count1,Awaiting_Interview_Results_count1]
        final_dict.append(dict1)

        open_count1 = infra.count('New')
        on_hold_count1 = infra.count('Onhold')
        fullfilled_count1 = infra.count('Profile Rejected')
        closed_count1 = infra.count('Closed')
        Profile_Shared_count1 = infra.count('Profile Shared')
        POCs_Contacted_count1 =infra.count("POC Contacted")
        Pending_Client_Interview_count1 = infra.count('Pending Client Interview')
        Awaiting_Interview_Results_count1 = infra.count('Awaiting Interview Results')
        dict1 = [open_count1,on_hold_count1,fullfilled_count1,closed_count1,Profile_Shared_count1,POCs_Contacted_count1,Pending_Client_Interview_count1,Awaiting_Interview_Results_count1]
        final_dict.append(dict1)
        open_count1 = asm.count('New')
        on_hold_count1 = asm.count('Onhold')
        fullfilled_count1 = asm.count('Profile Rejected')
        closed_count1 = asm.count('Closed')
        Profile_Shared_count1 = asm.count('Profile Shared')
        POCs_Contacted_count1 =asm.count("POC Contacted")
        Pending_Client_Interview_count1 = asm.count('Pending Client Interview')
        Awaiting_Interview_Results_count1 = asm.count('Awaiting Interview Results')
        dict1 = [open_count1,on_hold_count1,fullfilled_count1,closed_count1,Profile_Shared_count1,POCs_Contacted_count1,Pending_Client_Interview_count1,Awaiting_Interview_Results_count1]
        final_dict.append(dict1)
        open_count1 = coo.count('New')
        on_hold_count1 = coo.count('Onhold')
        fullfilled_count1 = coo.count('Profile Rejected')
        closed_count1 = coo.count('Closed')
        Profile_Shared_count1 = coo.count('Profile Shared')
        POCs_Contacted_count1 =coo.count("POC Contacted")
        Pending_Client_Interview_count1 = coo.count('Pending Client Interview')
        Awaiting_Interview_Results_count1 = coo.count('Awaiting Interview Results')
        dict1 = [open_count1,on_hold_count1,fullfilled_count1,closed_count1,Profile_Shared_count1,POCs_Contacted_count1,Pending_Client_Interview_count1,Awaiting_Interview_Results_count1]
        final_dict.append(dict1)
        count=0
        for i in final_dict:
            for j in range(len(i)):
                if i[j]!=0:
                    count += int(i[j])
        final_dict.insert(0,beeline_status_lost1)
        final_dict.insert(1,count)
        return Response(final_dict)



class ClosedCountView(APIView):
     def get(self,request):
        final_dict = []
        beeline_status_close1 = Beeline.objects.filter(status='Closed').count()
        if beeline_status_close1==0:
            print("yes")
            #dict1 = {'beeline_status_lost':0,'open_count':0,'fullfilled_count':0,'closed_count':0,'onhold_count':0,'Profile_Shared_count':0,'Pending_Client_Interview_count':0,'POCs_Contacted_count':0,'Awaiting_Interview_Results_count':0}
            dict1 = [0, [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
            return Response(dict1)
        else:
            sf = []
            cad = []
            nw = []
            infra=[]
            asm=[]
            coo=[]
            list1 = Beeline.objects.filter(status='Closed').all()
            l1=[]
            l2=[]
            for i in range(beeline_status_close1):
                item = BeelineSerializer(list1[i])
                item2 = item.data
                index = item2['id']
                obj1 = Beeline.objects.get(pk=index)
                obj2 = BeelineSerializer(obj1)
                obj3 = obj2.data
                obj4 = json.loads(json.dumps(obj3))
                print(len(obj4['beeline']))
                if len(obj4['beeline'])>=1:
                    print("came to second else")
                    length = len(obj4['beeline'])
                    var = obj4['beeline']
                    print(var)
                    for i in range(length):
                        obj5 = var[i]
                        print(obj5)
                        l1.append(obj5['current_Status'])
                        l2.append(obj5['prodapt_practice'])
                    print(l1)
                    print(l2)
                    sf_count = []
                    cad_count = []
                    nw_count = []
                    infra_count = []
                    asm_count = []
                    coo_count=[]
                    final = list(zip(l1,l2))
                    for i in final:
                        if i[1]=="SF Practice":
                            sf_count.append(i)
                        elif i[1]=="CAD":
                            cad_count.append(i)
                        elif i[1]=="NW Practice":
                            nw_count.append(i)
                        elif i[1]=="Infra Practice":
                            infra_count.append(i)  
                        elif i[1]=="ASM Practice":
                            asm_count.append(i)
                        elif i[1]=="COO-TOPS Practice":
                            coo_count.append(i)                          
                    
                    for i in sf_count:
                        sf.append(i[0])
                    print(sf)
                    
                    for i in cad_count:
                        cad.append(i[0])
                    print(cad)
                    
                    for i in nw_count:
                        nw.append(i[0])
                    print(nw)
                    infra = []
                    for i in infra_count:
                        infra.append(i[0])
                    print(infra)
                    asm = []
                    for i in asm_count:
                        asm.append(i[0])
                    print(asm)
                    coo = []
                    for i in coo_count:
                        coo.append(i[0])
                    print(coo)
        open_count1 = sf.count('New')
        on_hold_count1 = sf.count('Onhold')
        fullfilled_count1 = sf.count('Profile Rejected')
        closed_count1 = sf.count('Closed')
        Profile_Shared_count1 = sf.count('Profile Shared')
        POCs_Contacted_count1 =sf.count("POC Contacted")
        Pending_Client_Interview_count1 = sf.count('Pending Client Interview')
        Awaiting_Interview_Results_count1 = sf.count('Awaiting Interview Results')
        dict1 = [open_count1,on_hold_count1,fullfilled_count1,closed_count1,Profile_Shared_count1,POCs_Contacted_count1,Pending_Client_Interview_count1,Awaiting_Interview_Results_count1]
        final_dict.append(dict1)
        open_count1 = cad.count('New')
        on_hold_count1 =cad.count('Onhold')
        fullfilled_count1 = cad.count('Profile Rejected')
        closed_count1 = cad.count('Closed')
        Profile_Shared_count1 = cad.count('Profile Shared')
        POCs_Contacted_count1 =cad.count("POC Contacted")
        Pending_Client_Interview_count1 = cad.count('Pending Client Interview')
        Awaiting_Interview_Results_count1 = cad.count('Awaiting Interview Results')
        dict1 = [open_count1,on_hold_count1,fullfilled_count1,closed_count1,Profile_Shared_count1,POCs_Contacted_count1,Pending_Client_Interview_count1,Awaiting_Interview_Results_count1]
        final_dict.append(dict1)

        open_count1 = nw.count('New')
        on_hold_count1 = nw.count('Onhold')
        fullfilled_count1 = nw.count('Profile Rejected')
        closed_count1 = nw.count('Closed')
        Profile_Shared_count1 = nw.count('Profile Shared')
        POCs_Contacted_count1 =nw.count("POC Contacted")
        Pending_Client_Interview_count1 = nw.count('Pending Client Interview')
        Awaiting_Interview_Results_count1 = nw.count('Awaiting Interview Results')
        dict1 = [open_count1,on_hold_count1,fullfilled_count1,closed_count1,Profile_Shared_count1,POCs_Contacted_count1,Pending_Client_Interview_count1,Awaiting_Interview_Results_count1]
        final_dict.append(dict1)

        open_count1 = infra.count('New')
        on_hold_count1 = infra.count('Onhold')
        fullfilled_count1 = infra.count('Profile Rejected')
        closed_count1 = infra.count('Closed')
        Profile_Shared_count1 = infra.count('Profile Shared')
        POCs_Contacted_count1 =infra.count("POC Contacted")
        Pending_Client_Interview_count1 = infra.count('Pending Client Interview')
        Awaiting_Interview_Results_count1 = infra.count('Awaiting Interview Results')
        dict1 = [open_count1,on_hold_count1,fullfilled_count1,closed_count1,Profile_Shared_count1,POCs_Contacted_count1,Pending_Client_Interview_count1,Awaiting_Interview_Results_count1]
        final_dict.append(dict1)
        open_count1 = asm.count('New')
        on_hold_count1 = asm.count('Onhold')
        fullfilled_count1 = asm.count('Profile Rejected')
        closed_count1 = asm.count('Closed')
        Profile_Shared_count1 = asm.count('Profile Shared')
        POCs_Contacted_count1 =asm.count("POC Contacted")
        Pending_Client_Interview_count1 = asm.count('Pending Client Interview')
        Awaiting_Interview_Results_count1 = asm.count('Awaiting Interview Results')
        dict1 = [open_count1,on_hold_count1,fullfilled_count1,closed_count1,Profile_Shared_count1,POCs_Contacted_count1,Pending_Client_Interview_count1,Awaiting_Interview_Results_count1]
        final_dict.append(dict1)
        open_count1 = coo.count('New')
        on_hold_count1 = coo.count('Onhold')
        fullfilled_count1 = coo.count('profile Rejected')
        closed_count1 = coo.count('Closed')
        Profile_Shared_count1 = coo.count('Profile Shared')
        POCs_Contacted_count1 =coo.count("POC Contacted")
        Pending_Client_Interview_count1 = coo.count('Pending Client Interview')
        Awaiting_Interview_Results_count1 = coo.count('Awaiting Interview Results')
        dict1 = [open_count1,on_hold_count1,fullfilled_count1,closed_count1,Profile_Shared_count1,POCs_Contacted_count1,Pending_Client_Interview_count1,Awaiting_Interview_Results_count1]
        final_dict.append(dict1)
        count=0
        for i in final_dict:
            for j in range(len(i)):
                if i[j]!=0:
                    count += int(i[j])
        final_dict.insert(0,beeline_status_close1)
        final_dict.insert(1,count)
        return Response(final_dict)







class FulFilledCountView(APIView):
     def get(self,request):
        final_dict = []
        beeline_status_full1 = Beeline.objects.filter(status='Fulfilled').count()
        if beeline_status_full1==0:
            #print("yes")
            #dict1 = {'beeline_status_lost':0,'open_count':0,'fullfilled_count':0,'closed_count':0,'onhold_count':0,'Profile_Shared_count':0,'Pending_Client_Interview_count':0,'POCs_Contacted_count':0,'Awaiting_Interview_Results_count':0}
            dict1 = [0, [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
            return Response(dict1)
        else:
            sf = []
            cad = []   
            nw = []
            infra=[]
            asm=[]
            coo=[]
            list1 = Beeline.objects.filter(status='Fulfilled').all()
            l1=[]
            l2=[]
            for i in range(beeline_status_full1):
                item = BeelineSerializer(list1[i])
                item2 = item.data
                index = item2['id']
                obj1 = Beeline.objects.get(pk=index)
                obj2 = BeelineSerializer(obj1)
                obj3 = obj2.data
                obj4 = json.loads(json.dumps(obj3))
                #print(len(obj4['beeline']))
                if len(obj4['beeline'])>=1:
                    #print("came to second else")
                    length = len(obj4['beeline'])
                    var = obj4['beeline']
                    #print(var)
                    for i in range(length):
                        obj5 = var[i]
                        #print(obj5)
                        l1.append(obj5['current_Status'])
                        l2.append(obj5['prodapt_practice'])
                    #print(l1)
                    #print(l2)
                    sf_count = []
                    cad_count = []
                    nw_count = []
                    infra_count = []
                    asm_count = []
                    coo_count=[]
                    final = list(zip(l1,l2))
                    for i in final:
                        if i[1]=="SF Practice":
                            sf_count.append(i)
                        elif i[1]=="CAD":
                            cad_count.append(i)
                        elif i[1]=="NW Practice":
                            nw_count.append(i)
                        elif i[1]=="Infra Practice":
                            infra_count.append(i)  
                        elif i[1]=="ASM Practice":
                            asm_count.append(i)
                        elif i[1]=="COO-TOPS Practice":
                            coo_count.append(i)                          
                    
                    for i in sf_count:
                        sf.append(i[0])
                    print(sf)
                    
                    for i in cad_count:
                        cad.append(i[0])
                    print(cad)
                    
                    for i in nw_count:
                        nw.append(i[0])
                    print(nw)
                    infra = []
                    for i in infra_count:
                        infra.append(i[0])
                    print(infra)
                    asm = []
                    for i in asm_count:
                        asm.append(i[0])
                    print(asm)
                    coo = []
                    for i in coo_count:
                        coo.append(i[0])
                    print(coo)
        open_count1 = sf.count('New')
        on_hold_count1 = sf.count('Onhold')
        fullfilled_count1 = sf.count('Profile Rejeceted')
        closed_count1 = sf.count('Closed')
        Profile_Shared_count1 = sf.count('Profile Shared')
        POCs_Contacted_count1 =sf.count("POC Contacted")
        Pending_Client_Interview_count1 = sf.count('Pending Client Interview')
        Awaiting_Interview_Results_count1 = sf.count('Awaiting Interview Results')
        dict1 = [open_count1,on_hold_count1,fullfilled_count1,closed_count1,Profile_Shared_count1,POCs_Contacted_count1,Pending_Client_Interview_count1,Awaiting_Interview_Results_count1]
        final_dict.append(dict1)
        open_count1 = cad.count('New')
        on_hold_count1 =cad.count('Onhold')
        fullfilled_count1 = cad.count('Profile Rejected')
        closed_count1 = cad.count('Closed')
        Profile_Shared_count1 = cad.count('Profile Shared')
        POCs_Contacted_count1 =cad.count("POC Contacted")
        Pending_Client_Interview_count1 = cad.count('Pending Client Interview')
        Awaiting_Interview_Results_count1 = cad.count('Awaiting Interview Results')
        dict1 = [open_count1,on_hold_count1,fullfilled_count1,closed_count1,Profile_Shared_count1,POCs_Contacted_count1,Pending_Client_Interview_count1,Awaiting_Interview_Results_count1]
        final_dict.append(dict1)

        open_count1 = nw.count('New')
        on_hold_count1 = nw.count('Onhold')
        fullfilled_count1 = nw.count('Profile Rejected')
        closed_count1 = nw.count('Closed')
        Profile_Shared_count1 = nw.count('Profile Shared')
        POCs_Contacted_count1 =nw.count("POC Contacted")
        Pending_Client_Interview_count1 = nw.count('Pending Client Interview')
        Awaiting_Interview_Results_count1 = nw.count('Awaiting Interview Results')
        dict1 = [open_count1,on_hold_count1,fullfilled_count1,closed_count1,Profile_Shared_count1,POCs_Contacted_count1,Pending_Client_Interview_count1,Awaiting_Interview_Results_count1]
        final_dict.append(dict1)

        open_count1 = infra.count('New')
        on_hold_count1 = infra.count('Onhold')
        fullfilled_count1 = infra.count('Profile Rejected')
        closed_count1 = infra.count('Closed')
        Profile_Shared_count1 = infra.count('Profile Shared')
        POCs_Contacted_count1 =infra.count("POC Contacted")
        Pending_Client_Interview_count1 = infra.count('Pending Client Interview')
        Awaiting_Interview_Results_count1 = infra.count('Awaiting Interview Results')
        dict1 = [open_count1,on_hold_count1,fullfilled_count1,closed_count1,Profile_Shared_count1,POCs_Contacted_count1,Pending_Client_Interview_count1,Awaiting_Interview_Results_count1]
        final_dict.append(dict1)
        open_count1 = asm.count('New')
        on_hold_count1 = asm.count('Onhold')
        fullfilled_count1 = asm.count('Profile Rejected')
        closed_count1 = asm.count('Closed')
        Profile_Shared_count1 = asm.count('Profile Shared')
        POCs_Contacted_count1 =asm.count("POC Contacted")
        Pending_Client_Interview_count1 = asm.count('Pending Client Interview')
        Awaiting_Interview_Results_count1 = asm.count('Awaiting Interview Results')
        dict1 = [open_count1,on_hold_count1,fullfilled_count1,closed_count1,Profile_Shared_count1,POCs_Contacted_count1,Pending_Client_Interview_count1,Awaiting_Interview_Results_count1]
        final_dict.append(dict1)
        open_count1 = coo.count('New')
        on_hold_count1 = coo.count('Onhold')
        fullfilled_count1 = coo.count('Profile Rejected')
        closed_count1 = coo.count('Closed')
        Profile_Shared_count1 = coo.count('Profile Shared')
        POCs_Contacted_count1 =coo.count("POC Contacted")
        Pending_Client_Interview_count1 = coo.count('Pending Client Interview')
        Awaiting_Interview_Results_count1 = coo.count('Awaiting Interview Results')
        dict1 = [open_count1,on_hold_count1,fullfilled_count1,closed_count1,Profile_Shared_count1,POCs_Contacted_count1,Pending_Client_Interview_count1,Awaiting_Interview_Results_count1]
        final_dict.append(dict1)
        count=0
        for i in final_dict:
            for j in range(len(i)):
                if i[j]!=0:
                    count += int(i[j])
        final_dict.insert(0,beeline_status_full1)
        final_dict.insert(1,count)
        return Response(final_dict)


class OpenCountView(APIView):
     def get(self,request):
        final_dict = []
        beeline_status_open1 = Beeline.objects.filter(status='Open').count()
        if beeline_status_open1==0:
            print("yes")
            #dict1 = {'beeline_status_lost':0,'open_count':0,'fullfilled_count':0,'closed_count':0,'onhold_count':0,'Profile_Shared_count':0,'Pending_Client_Interview_count':0,'POCs_Contacted_count':0,'Awaiting_Interview_Results_count':0}
            dict1 = [0, [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
            return Response(dict1)
        else:
            list1 = Beeline.objects.filter(status='Open').all()
            l1=[]
            l2=[]
            for i in range(beeline_status_open1):
                item = BeelineSerializer(list1[i])
                item2 = item.data
                index = item2['id']
                obj1 = Beeline.objects.get(pk=index)
                obj2 = BeelineSerializer(obj1)
                obj3 = obj2.data
                obj4 = json.loads(json.dumps(obj3))
                print(len(obj4['beeline']))
                if len(obj4['beeline'])>=1:
                    print("came to second else")
                    length = len(obj4['beeline'])
                    var = obj4['beeline']
                    print(var)
                    for i in range(length):
                        obj5 = var[i]
                        print(obj5)
                        l1.append(obj5['current_Status'])
                        l2.append(obj5['prodapt_practice'])
                    print(l1)
                    print(l2)
                    sf_count = []
                    cad_count = []
                    nw_count = []
                    infra_count = []
                    asm_count = []
                    coo_count=[]
                    final = list(zip(l1,l2))
                    for i in final:
                        if i[1]=="SF Practice":
                            sf_count.append(i)
                        elif i[1]=="CAD":
                            cad_count.append(i)
                        elif i[1]=="NW Practice":
                            nw_count.append(i)
                        elif i[1]=="Infra Practice":
                            infra_count.append(i)  
                        elif i[1]=="ASM Practice":
                            asm_count.append(i)
                        elif i[1]=="COO-TOPS Practice":
                            coo_count.append(i)                          
                    sf = []
                    for i in sf_count:
                        sf.append(i[0])
                    print(sf)
                    cad = []
                    for i in cad_count:
                        cad.append(i[0])
                    print(cad)
                    nw = []
                    for i in nw_count:
                        nw.append(i[0])
                    print(nw)
                    infra = []
                    for i in infra_count:
                        infra.append(i[0])
                    print(infra)
                    asm = []
                    for i in asm_count:
                        asm.append(i[0])
                    print(asm)
                    coo = []
                    for i in coo_count:
                        coo.append(i[0])
                    print(coo)
        open_count1 = sf.count('New')
        on_hold_count1 = sf.count('Onhold')
        fullfilled_count1 = sf.count('Profile Rejected')
        closed_count1 = sf.count('Closed')
        Profile_Shared_count1 = sf.count('Profile Shared')
        POCs_Contacted_count1 =sf.count("POC Contacted")
        Pending_Client_Interview_count1 = sf.count('Pending Client Interview')
        Awaiting_Interview_Results_count1 = sf.count('Awaiting Interview Results')
        dict1 = [open_count1,on_hold_count1,fullfilled_count1,closed_count1,Profile_Shared_count1,POCs_Contacted_count1,Pending_Client_Interview_count1,Awaiting_Interview_Results_count1]
        final_dict.append(dict1)
        open_count1 = cad.count('New')
        on_hold_count1 =cad.count('Onhold')
        fullfilled_count1 = cad.count('Profile Rejected')
        closed_count1 = cad.count('Closed')
        Profile_Shared_count1 = cad.count('Profile Shared')
        POCs_Contacted_count1 =cad.count("POC Contacted")
        Pending_Client_Interview_count1 = cad.count('Pending Client Interview')
        Awaiting_Interview_Results_count1 = cad.count('Awaiting Interview Results')
        dict1 = [open_count1,on_hold_count1,fullfilled_count1,closed_count1,Profile_Shared_count1,POCs_Contacted_count1,Pending_Client_Interview_count1,Awaiting_Interview_Results_count1]
        final_dict.append(dict1)

        open_count1 = nw.count('New')
        on_hold_count1 = nw.count('Onhold')
        fullfilled_count1 = nw.count('Profile Rejected')
        closed_count1 = nw.count('Closed')
        Profile_Shared_count1 = nw.count('Profile Shared')
        POCs_Contacted_count1 =nw.count("POC Contacted")
        Pending_Client_Interview_count1 = nw.count('Pending Client Interview')
        Awaiting_Interview_Results_count1 = nw.count('Awaiting Interview Results')
        dict1 = [open_count1,on_hold_count1,fullfilled_count1,closed_count1,Profile_Shared_count1,POCs_Contacted_count1,Pending_Client_Interview_count1,Awaiting_Interview_Results_count1]
        final_dict.append(dict1)

        open_count1 = infra.count('New')
        on_hold_count1 = infra.count('Onhold')
        fullfilled_count1 = infra.count('Profile Rejected')
        closed_count1 = infra.count('Closed')
        Profile_Shared_count1 = infra.count('Profile Shared')
        POCs_Contacted_count1 =infra.count("POC Contacted")
        Pending_Client_Interview_count1 = infra.count('Pending Client Interview')
        Awaiting_Interview_Results_count1 = infra.count('Awaiting Interview Results')
        dict1 = [open_count1,on_hold_count1,fullfilled_count1,closed_count1,Profile_Shared_count1,POCs_Contacted_count1,Pending_Client_Interview_count1,Awaiting_Interview_Results_count1]
        final_dict.append(dict1)
        open_count1 = asm.count('New')
        on_hold_count1 = asm.count('Onhold')
        fullfilled_count1 = asm.count('Profile Rejected')
        closed_count1 = asm.count('Closed')
        Profile_Shared_count1 = asm.count('Profile Shared')
        POCs_Contacted_count1 =asm.count("POC Contacted")
        Pending_Client_Interview_count1 = asm.count('Pending Client Interview')
        Awaiting_Interview_Results_count1 = asm.count('Awaiting Interview Results')
        dict1 = [open_count1,on_hold_count1,fullfilled_count1,closed_count1,Profile_Shared_count1,POCs_Contacted_count1,Pending_Client_Interview_count1,Awaiting_Interview_Results_count1]
        final_dict.append(dict1)
        open_count1 = coo.count('New')
        on_hold_count1 = coo.count('Onhold')
        fullfilled_count1 = coo.count('Profile Rejected')
        closed_count1 = coo.count('Closed')
        Profile_Shared_count1 = coo.count('Profile Shared')
        POCs_Contacted_count1 =coo.count("POC Contacted")
        Pending_Client_Interview_count1 = coo.count('Pending Client Interview')
        Awaiting_Interview_Results_count1 = coo.count('Awaiting Interview Results')
        dict1 = [open_count1,on_hold_count1,fullfilled_count1,closed_count1,Profile_Shared_count1,POCs_Contacted_count1,Pending_Client_Interview_count1,Awaiting_Interview_Results_count1]
        final_dict.append(dict1)
        count=0
        for i in final_dict:
            for j in range(len(i)):
                if i[j]!=0:
                    count += int(i[j])

        final_dict.insert(0,beeline_status_open1)
        final_dict.insert(1,count)

        return Response(final_dict)
class PracticeCount(APIView):
    def get(self,request):
        status_list = ['Open','Fulfilled','Closed','Lost']
        inc=0
        final_dict = []
        total_dict = []
        for item in status_list:
            beeline_status = Beeline.objects.filter(status=item).count()
            if beeline_status==0:
                print("came to if part")
                #print("yes")
                #dict1 = {'beeline_status_lost':0,'open_count':0,'fullfilled_count':0,'closed_count':0,'onhold_count':0,'Profile_Shared_count':0,'Pending_Client_Interview_count':0,'POCs_Contacted_count':0,'Awaiting_Interview_Results_count':0}
                final_dict = [0,[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
                total_dict.append(final_dict)
                final_dict = []
            else:
                print("came to else part")
                list1 = Beeline.objects.filter(status=item).all()
                l1=[]
                l2=[]
                for i in range(beeline_status):
                    item = BeelineSerializer(list1[i])
                    item2 = item.data
                    index = item2['id']
                    obj1 = Beeline.objects.get(pk=index)
                    obj2 = BeelineSerializer(obj1)
                    obj3 = obj2.data
                    obj4 = json.loads(json.dumps(obj3))
                    #print(len(obj4['beeline']))
                    if len(obj4['beeline'])>=1:
                        #print("came to second else")
                        length = len(obj4['beeline'])
                        var = obj4['beeline']
                        #print(var)
                        for i in range(length):
                            obj5 = var[i]
                            #print(obj5)
                            l1.append(obj5['current_Status'])
                            l2.append(obj5['prodapt_practice'])
                        #print(l1)
                        #print(l2)
                        sf_count = []
                        cad_count = []
                        nw_count = []
                        infra_count = []
                        asm_count = []
                        coo_count=[]
                        final = list(zip(l1,l2))
                        for i in final:
                            if i[1]=="SF Practice":
                                sf_count.append(i)
                            elif i[1]=="CAD":
                                cad_count.append(i)
                            elif i[1]=="NW Practice":
                                nw_count.append(i)
                            elif i[1]=="Infra Practice":
                                infra_count.append(i)  
                            elif i[1]=="ASM Practice":
                                asm_count.append(i)
                            elif i[1]=="COO-TOPS Practice":
                                coo_count.append(i)                          
                        sf = []
                        for i in sf_count:
                            sf.append(i[0])
                        #print(sf)
                        cad = []
                        for i in cad_count:
                            cad.append(i[0])
                        #print(cad)
                        nw = []
                        for i in nw_count:
                            nw.append(i[0])
                        #print(nw)
                        infra = []
                        for i in infra_count:
                            infra.append(i[0])
                        #print(infra)
                        asm = []
                        for i in asm_count:
                            asm.append(i[0])
                        #print(asm)
                        coo = []
                        for i in coo_count:
                            coo.append(i[0])
                        #print(coo)
                open_count1 = sf.count('New')
                on_hold_count1 = sf.count('Onhold')
                fullfilled_count1 = sf.count('Profile Rejected')
                closed_count1 = sf.count('Closed')
                Profile_Shared_count1 = sf.count('Profile Shared')
                POCs_Contacted_count1 =sf.count("POC Contacted")
                Pending_Client_Interview_count1 = sf.count('Pending Client Interview')
                Awaiting_Interview_Results_count1 = sf.count('Awaiting Interview Results')
                dict1 = [open_count1,on_hold_count1,fullfilled_count1,closed_count1,Profile_Shared_count1,POCs_Contacted_count1,Pending_Client_Interview_count1,Awaiting_Interview_Results_count1]
                final_dict.append(dict1)
                open_count1 = cad.count('New')
                on_hold_count1 =cad.count('Onhold')
                fullfilled_count1 = cad.count('Profile Rejected')
                closed_count1 = cad.count('Closed')
                Profile_Shared_count1 = cad.count('Profile Shared')
                POCs_Contacted_count1 =cad.count("POC Contacted")
                Pending_Client_Interview_count1 = cad.count('Pending Client Interview')
                Awaiting_Interview_Results_count1 = cad.count('Awaiting Interview Results')
                dict1 = [open_count1,on_hold_count1,fullfilled_count1,closed_count1,Profile_Shared_count1,POCs_Contacted_count1,Pending_Client_Interview_count1,Awaiting_Interview_Results_count1]
                final_dict.append(dict1)
                open_count1 = nw.count('New')
                on_hold_count1 = nw.count('Onhold')
                fullfilled_count1 = nw.count('Profile Rejected')
                closed_count1 = nw.count('Closed')
                Profile_Shared_count1 = nw.count('Profile Shared')
                POCs_Contacted_count1 =nw.count("POC Contacted")
                Pending_Client_Interview_count1 = nw.count('Pending Client Interview')
                Awaiting_Interview_Results_count1 = nw.count('Awaiting Interview Results')
                dict1 = [open_count1,on_hold_count1,fullfilled_count1,closed_count1,Profile_Shared_count1,POCs_Contacted_count1,Pending_Client_Interview_count1,Awaiting_Interview_Results_count1]
                final_dict.append(dict1)
                open_count1 = infra.count('New')
                on_hold_count1 = infra.count('Onhold')
                fullfilled_count1 = infra.count('Profile Rejected')
                closed_count1 = infra.count('Closed')
                Profile_Shared_count1 = infra.count('Profile Shared')
                POCs_Contacted_count1 =infra.count("POC Contacted")
                Pending_Client_Interview_count1 = infra.count('Pending Client Interview')
                Awaiting_Interview_Results_count1 = infra.count('Awaiting Interview Results')
                dict1 = [open_count1,on_hold_count1,fullfilled_count1,closed_count1,Profile_Shared_count1,POCs_Contacted_count1,Pending_Client_Interview_count1,Awaiting_Interview_Results_count1]
                final_dict.append(dict1)
                open_count1 = asm.count('New')
                on_hold_count1 = asm.count('Onhold')
                fullfilled_count1 = asm.count('Profile Rejected')
                closed_count1 = asm.count('Closed')
                Profile_Shared_count1 = asm.count('Profile Shared')
                POCs_Contacted_count1 =asm.count("POC Contacted")
                Pending_Client_Interview_count1 = asm.count('Pending Client Interview')
                Awaiting_Interview_Results_count1 = asm.count('Awaiting Interview Results')
                dict1 = [open_count1,on_hold_count1,fullfilled_count1,closed_count1,Profile_Shared_count1,POCs_Contacted_count1,Pending_Client_Interview_count1,Awaiting_Interview_Results_count1]
                final_dict.append(dict1)
                open_count1 = coo.count('New')
                on_hold_count1 = coo.count('Onhold')
                fullfilled_count1 = coo.count('Profile Rejected')
                closed_count1 = coo.count('Closed')
                Profile_Shared_count1 = coo.count('Profile Shared')
                POCs_Contacted_count1 =coo.count("POC Contacted")
                Pending_Client_Interview_count1 = coo.count('Pending Client Interview')
                Awaiting_Interview_Results_count1 = coo.count('Awaiting Interview Results')
                dict1 = [open_count1,on_hold_count1,fullfilled_count1,closed_count1,Profile_Shared_count1,POCs_Contacted_count1,Pending_Client_Interview_count1,Awaiting_Interview_Results_count1]
                final_dict.append(dict1)
                count=0
                for value in final_dict:
                    for value1 in value:
                        if int(value1)>=1:
                            count+=int(value1)
                final_dict.insert(0,count)
                final_dict.insert(7,beeline_status)
                total_dict.append(final_dict)
                final_dict = []
        #print(total_dict[0][0])
        return Response(total_dict)

class Register(APIView):
    def post(self,request):
        username = request.data['username']
        email = request.data['email']
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        password=request.data['password1']
        password2 = request.data['password2']
        if password==password2:
            try:
                user = User.objects.create_user(username=username,
                                 email=email,
                                 password=password,first_name=first_name,last_name=last_name
                                 )
                user.save()
                return Response("success")
            except:
                return Response("user already exist")
        else:
            return Response("password doesn't match")
class PasswordReset(APIView):
    def post(self,request):
        data1 = request.data 
        username=data1["Username"]
        pass_data = data1["password"]
        pass_data1 = json.loads(pass_data)
        print(pass_data1)
        password = pass_data1["password1"]
        password2 = pass_data1["password2"]
        
        if password==password2:
            try:
                obj = User.objects.get(username=username)
                obj.set_password(password)
                obj.save()
                return Response("password created successfully")
            except:
                return Response("user doesn't exist")
        else:
            return Response("password doesn't match")

class New_beeline_Mail(APIView):
    def post(self,request):
        data1=request.data['User']
        context = json.loads(data1)
        file = request.FILES['file']
        attachment = (file.name, file.read(), file.content_type)
        html_content = render_to_string("new_beeline.html",context)
        text_content = strip_tags(html_content)
        email = EmailMultiAlternatives(
        "New Beeline Added",
        text_content,
        settings.EMAIL_HOST_USER ,
        ['gopi.y@prodapt.com']
        )
        email.attach(*attachment)
        email.attach_alternative(html_content, 'text/html')
        email.send()
        return Response({"status":"mail sent successfully"},status=status.HTTP_200_OK)

class New_profile_Mail(APIView):
    def post(self,request):
        data1=request.data['User']
        context = json.loads(data1)
        
        data_1 = Beeline.objects.get(id=context['beeline'])
        data_2 = BeelineSerializer(data_1)
        context['beeline']=data_2.data['beeLine_Request_Number']
        html_content = render_to_string("new_profile.html",context)
        text_content = strip_tags(html_content)
        email = EmailMultiAlternatives(
        "New Profile Added",
        text_content,
        settings.EMAIL_HOST_USER ,
        ['gopi.y@prodapt.com']
        )
        if request.data['file']=="undefined":
            pass
        else:
            file = request.FILES['file']
            attachment = (file.name, file.read(), file.content_type)

            email.attach(*attachment)
        email.attach_alternative(html_content, 'text/html')
        email.send()
        return Response({"status":"mail sent successfully"},status=status.HTTP_200_OK)

class Update_Beeline_Mail(APIView):
    def post(self,request):
        data1=request.data['User']
        context = json.loads(data1)
        html_content = render_to_string("updated_beeline.html",context)
        text_content = strip_tags(html_content)
        email = EmailMultiAlternatives(
        "Existing Beeline Updated",
        text_content,
        settings.EMAIL_HOST_USER ,
        ['gopi.y@prodapt.com']
        )
        if request.data['file']=="undefined":
            pass
        else:
            file = request.FILES['file']
            attachment = (file.name, file.read(), file.content_type)

            email.attach(*attachment)
        email.attach_alternative(html_content, 'text/html')
        email.send()
        return Response({"status":"mail sent successfully"},status=status.HTTP_200_OK)
        
class Updated_profile_Mail(APIView):
    def post(self,request):
        data1=request.data['User']
        context = json.loads(data1)
        
        data_1 = Beeline.objects.get(id=context['beeline'])
        data_2 = BeelineSerializer(data_1)
        context['beeline']=data_2.data['beeLine_Request_Number']
        html_content = render_to_string("updated_profile.html",context)
        text_content = strip_tags(html_content)
        email = EmailMultiAlternatives(
        "Existing Profile Updated",
        text_content,
        settings.EMAIL_HOST_USER ,
        ['gopi.y@prodapt.com']
        )
        if request.data['file']=="undefined":
            pass
        else:
            file = request.FILES['file']
            attachment = (file.name, file.read(), file.content_type)

            email.attach(*attachment)
        email.attach_alternative(html_content, 'text/html')
        email.send()
        return Response({"status":"mail sent successfully"},status=status.HTTP_200_OK)
    
class Profile_delete_Mail(APIView):
    def get_object(self,pk):
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            raise Http404
    def post(self,request,pk):
        profile=self.get_object(pk)
        data2 = ProfileSerializer(profile)
        data3 = data2.data
        context = dict(data3)
        data_1 = Beeline.objects.get(id=context['beeline'])
        data_2 = BeelineSerializer(data_1)
        context['beeline']=data_2.data['beeLine_Request_Number']
        html_content = render_to_string("profile_delete.html",context)
        text_content = strip_tags(html_content)
        email = EmailMultiAlternatives(
        "Existing Profile deleted",
        text_content,
        settings.EMAIL_HOST_USER ,
        ['gopi.y@prodapt.com']
        )
        email.attach_alternative(html_content, 'text/html')
        email.send()
        return Response({"status":"mail sent successfully"},status=status.HTTP_200_OK)

class Beeline_delete_Mail(APIView):
    def get_object(self,pk):
        try:
            return Beeline.objects.get(pk=pk)
        except Beeline.DoesNotExist:
            raise Http404
    def post(self,request,pk):
        beeline=self.get_object(pk)
        data2 = BeelineSerializer(beeline)
        data3 = data2.data
        context = dict(data3)
        html_content = render_to_string("beeline_delete.html",context)
        text_content = strip_tags(html_content)
        email = EmailMultiAlternatives(
        "Existing Beeline deleted",
        text_content,
        settings.EMAIL_HOST_USER ,
        ['gopi.y@prodapt.com']
        )
        email.attach_alternative(html_content, 'text/html')
        email.send()
        return Response({"status":"mail sent successfully"},status=status.HTTP_200_OK)
    
class Contact_Us_Mail(APIView):
    def post(self,request):
        context=request.data
        html_content = render_to_string("contact_us.html",context)
        text_content = strip_tags(html_content)
        email = EmailMultiAlternatives(
        "Service Request",
        text_content,
        settings.EMAIL_HOST_USER ,
        ['gopi.y@prodapt.com']
        )
        email.attach_alternative(html_content, 'text/html')
        email.send()
        return Response({"status":"mail sent successfully"},status=status.HTTP_200_OK)

import time as tm
from datetime import time,timedelta,datetime
import pandas as pd
class AlertMail(APIView):
    def get(self,request):
        obj1 = Beeline.objects.all().count()
        if obj1>=1:
            obj2 = Beeline.objects.all()
            l1=[]
            for i in range(obj1):
                item = BeelineSerializer(obj2[i])
                item2 = item.data
                    #index = item2['id']
                    #index = item2['beeline']
                    #obj3 = Beeline.objects.get(pk=index)
                    #obj4 = BeelineSerializer(obj3)
                    #print(obj4.data)
                    #obj5 = obj4.data
                obj6 = json.loads(json.dumps(item2))
                #print(obj6)
                    #print(obj6)
                deadline_date = obj6['cv_DeadLine']
                request_date = obj6['date_request']
                beeline_request_num = obj6['beeLine_Request_Number']
                    #format = request_date.strftime("%d/%m/%Y")
                    #print(type(request_date))
                    #datetime_str = '09/19/22 13:55:26'
                datetime_object = datetime.strptime(deadline_date, "%Y-%m-%d")
                    #print(type(datetime_object))
                    #print(datetime_object)  # printed in default format
                    #2023-01-20
                current_time = datetime.now()
                duration = datetime_object-current_time
                    #print(type(duration))
                timedelta = pd.Timedelta(duration)
                left_days = (timedelta.days)+1
                #print(str(left_days)+" days")
                if left_days<=14 and left_days>=1:
                    l2 = []
                    l2 = [beeline_request_num,left_days]
                    l1.append(l2)
            if len(l1)>=1:
                context={}
                context['info'] = l1
                html_content = render_to_string("automatic_mail.html",context)
                text_content = strip_tags(html_content)
                email = EmailMultiAlternatives(
                "Beeline Expiry Alert",
                text_content,
                settings.EMAIL_HOST_USER ,
                ['tejaswini.s@prodapt.com','gopi.y@prodapt.com']
                )
                email.attach_alternative(html_content, 'text/html')
                email.send()
                return Response("mail sent successfully")
            else:
                return Response("None")
class SendCrendentials(APIView):
    def post(self,request):
        from io import BytesIO
        from django.core.mail import EmailMessage
        from reportlab.pdfgen import canvas
        from PyPDF2 import PdfFileWriter, PdfFileReader,PdfWriter,PdfReader
        from django.contrib.auth.hashers import make_password
        import random
        import string
        import secrets
        user=request.data["username"]
        pass1 =request.data["password1"]
        first = request.data['first_name']
        last = request.data['last_name']
        email = request.data["email"]
        pdf_buffer = BytesIO()
        c = canvas.Canvas(pdf_buffer)
        c.setFont("Helvetica", 8)
        c.drawString(100, 750,"Username:{}".format(user))
        c.drawString(100, 740,"FirstName:{}".format(first))
        c.drawString(100, 730,"LastName:{}".format(last))
        c.drawString(100, 720, "Password:{}".format(pass1))
        c.save()
        pdf_bytes = pdf_buffer.getvalue()
        pdf_writer = PdfWriter()
        pdf_reader = PdfReader(BytesIO(pdf_bytes))
        for page_num in range(len(pdf_reader.pages)):    
            pdf_writer.add_page(pdf_reader.pages[page_num])
        pdf_password = secrets.token_urlsafe(12)
        pdf_writer.encrypt(pdf_password)
        encrypted_pdf_buffer = BytesIO()
        pdf_writer.write(encrypted_pdf_buffer)
        encrypted_pdf_bytes = encrypted_pdf_buffer.getvalue()


        context=request.data
        context["pdfPassword"]=pdf_password
        html_content = render_to_string("credentials.html",context)
        text_content = strip_tags(html_content)
        email = EmailMultiAlternatives(
        "User account created",
        text_content,
        settings.EMAIL_HOST_USER ,
        [email]
        )
        email.attach_alternative(html_content, 'text/html')
        


        email.attach('encrypted_file.pdf', encrypted_pdf_bytes, 'application/pdf')
        email.send()
        return Response({"status":"mail sent successfully"})

class ResetPasswordMail(APIView):
    def post(self,request):
        context = request.data
        data1=request.data["Username"]
        userName = User.objects.get(username=data1)
        data1 = UserSerializer(userName)
        to_mail =   data1.data['email']
        html_content = render_to_string("passwordreset_mail.html",context)
        text_content = strip_tags(html_content)
        email = EmailMultiAlternatives(
        "Service Request",
        text_content,
        settings.EMAIL_HOST_USER ,
        [to_mail]
        )
        email.attach_alternative(html_content, 'text/html')
        email.send()
        return Response({"status":"mail sent successfully"},status=status.HTTP_200_OK)

class EditUserInfo(APIView):
    def get(self,request,pk):
        #data1 = request.data['']
        data2 = User.objects.get(pk=pk)
        data3 = UserSerializer(data2)
        data4 = data3.data
        print(data4)
        l1 = {"id":data4['id'] ,"username":data4['username'],"first_name":data4["first_name"],"last_name":data4["last_name"],"email":data4["email"]}
        return Response(l1,status=status.HTTP_201_CREATED)
    def patch(self,request,pk):
        user = User.objects.get(pk=pk)
        # username = request.data['User']
        details = request.data
        new={"username":details['username'],"first_name":details["first_name"],"last_name":details["last_name"],"email":details["email"]}
        serializer=UserSerializer(user,data=new,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_200_OK)