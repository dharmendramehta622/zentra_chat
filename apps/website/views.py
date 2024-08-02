from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework import status
from django.shortcuts import render,redirect
from .forms import OnboardForm
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import get_user_model
import uuid

User = get_user_model()

class UserViewSet(viewsets.ViewSet):
    
    permission_classes = [AllowAny]
    
    def list(self, request):
        # This can handle the default route
        return   render(request, 'index.html')

    @action(detail=True, methods=['get'])
    def onboard(self, request, pk=None):
        user_id = pk
        try:
            # Validate the UUID format
            uuid.UUID(user_id)
            user = User.objects.get(id=user_id)
            user.is_active = True 
            user.save()
        except ValueError:
            return Response({"error": "Invalid user ID format"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Process the user_id here as needed
        # For example, fetch user data, perform onboarding steps, etc.
        return Response({"message": f"Onboarding user with ID: {user_id}"}, status=status.HTTP_200_OK)
    
class OnboardView(View):
    def get(self, request, user_id):
        try:
            # Validate the UUID format
            user = User.objects.get(id=user_id) 
            if not user.is_active:
                form = OnboardForm(instance=user, initial={'username': user.username})
                form.fields['username'].disabled = True  # Disable the username field
                
                return render(request, 'onboard_form.html', {'form': form})
            else:
                return   HttpResponse("User is already active", status=400)
            
        except (ValueError, User.DoesNotExist):
                return Response({"error": "Invalid user ID format or user not found"}, status=status.HTTP_400_BAD_REQUEST)
          
                
#E4DOJ309#ESF
    def post(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
            form = OnboardForm(request.POST, instance=user)
             
            if form.is_valid():
                # Debug information

                if not user.is_active:
                    user.set_password(form.cleaned_data['new_password'])
                    user.is_active = True
                    user.email_verified = True
                    user.save()
                    # Redirect after saving
                    return redirect('https://hamrokk.com')  # Use a valid URL or named URL pattern

                return   HttpResponse("User is already active", status=400)
            # Debug information
            print("Form errors:", form.errors)

            form.fields['username'].disabled = True  # Keep the username field disabled
            return render(request, 'onboard_form.html', {'form': form})
        except (ValueError, User.DoesNotExist):
            return HttpResponse("Invalid user ID format or user not found", status=400)