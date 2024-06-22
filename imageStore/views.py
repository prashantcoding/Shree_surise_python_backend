from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import cloudinary
import cloudinary.uploader

# Replace with your actual Cloudinary configuration
cloudinary.config(
    cloud_name="derkfut8m",
    api_key="248344878914255",
    api_secret="NG_TuC4vMwKajqCnp73SUE4WLh8"
)
from django.http import JsonResponse
@csrf_exempt
def index(request):
    try:
        if request.method == 'POST' and request.FILES.get('image'):
            image = request.FILES['image']
            
            # Upload image to Cloudinary
            upload_result = cloudinary.uploader.upload(image)
            image_url = upload_result['url']
            
            return JsonResponse({"url":image_url})
        
        return HttpResponse("Invalid request. POST method with 'image' file is required.")
    
    except Exception as e:
        return HttpResponse(f"Error uploading image: {str(e)}")
