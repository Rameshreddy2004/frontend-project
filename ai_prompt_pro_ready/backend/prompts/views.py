from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Prompt
from .redis_client import redis_client
import json


@csrf_exempt
def prompt_list(request):
    if request.method == 'GET':
        data = list(Prompt.objects.values())
        return JsonResponse(data, safe=False)

    elif request.method == 'POST':
        try:
            body = json.loads(request.body)

            prompt = Prompt.objects.create(
                title=body.get('title'),
                content=body.get('content'),
                complexity=body.get('complexity')
            )

            return JsonResponse({
                "id": str(prompt.id),
                "title": prompt.title,
                "content": prompt.content,
                "complexity": prompt.complexity,
                "created_at": prompt.created_at
            })

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)


def prompt_detail(request, id):
    try:
        prompt = Prompt.objects.get(id=id)

        # 🔥 Redis view counter
        redis_client.incr(f"prompt:{id}:views")
        views = redis_client.get(f"prompt:{id}:views")

        return JsonResponse({
            "id": str(prompt.id),
            "title": prompt.title,
            "content": prompt.content,
            "complexity": prompt.complexity,
            "created_at": prompt.created_at,
            "views": int(views) if views else 0
        })

    except Prompt.DoesNotExist:
        return JsonResponse({"error": "Not found"}, status=404)


@csrf_exempt
def delete_prompt(request, id):
    if request.method == 'DELETE':
        try:
            prompt = Prompt.objects.get(id=id)
            prompt.delete()

            # 🔥 also delete Redis views
            redis_client.delete(f"prompt:{id}:views")

            return JsonResponse({"message": "Deleted successfully"})

        except Prompt.DoesNotExist:
            return JsonResponse({"error": "Not found"}, status=404)

    return JsonResponse({"error": "Invalid method"}, status=405)