from snippets.serializers import FLIPSerializer



class FlipView(generics.GenericAPIView):
    serializer_class = FLIPSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                        IsOwnerOrReadOnly,
                        IsAuthenticated]
    def post(self, request, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        code = request.data['code']
        from .thinker import go
        categories_dict = asyncio.run(go(code))
        categories = categories_dict[0],
        sentences = categories_dict[1],
        title = categories_dict[2]
        nlp_returned = {"title" : title, "categories" : categories, "sentences" : sentences}
        return Response(nlp_returned)
