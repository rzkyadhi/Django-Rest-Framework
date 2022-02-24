from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer

def drink_list(request):
    # Get all drinks
    drinks = Drink.objects.all()

    # Serialize the data
    serializer = DrinkSerializer(drinks, many=True)

    # Create a JsonResponse using the serialized list
    return JsonResponse({"drinks": serializer.data}, safe=False)
    #return JsonResponse(serializer.data, safe=False)