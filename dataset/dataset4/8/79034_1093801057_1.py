class GroupList(generics.ListCreateAPIView):
    queryset = pGroups.objects.all()
    serializer_class = GroupSerializer