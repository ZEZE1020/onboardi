from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import AgentRequestSerializer, AgentResponseSerializer
from agent.planner import plan

class AgentAPIView(APIView):
    def post(self, request):
        serializer = AgentRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        goal = serializer.validated_data["goal"]

        steps = plan(goal)
        results = []
        for step in steps:
            # deferred import
            from agent.executor import execute
            results.append(execute(step, {}))

        out = AgentResponseSerializer({"steps": results})
        return Response(out.data, status=status.HTTP_200_OK)
