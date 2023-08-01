from django.shortcuts import get_object_or_404, redirect,render
from rest_framework import generics 
from .models import Book
from .serializers import BookSerializer

class BookListCreateView(generics.ListCreateAPIView):
    
    serializer_class = BookSerializer
    template_name = 'api/book_list.html'

    def get_queryset(self):
        return Book.objects.all()
    
    def get(self, request, *args, **kwargs):
        books =self.get_queryset
        return render(request,self.template_name,{'books':books})

    def post(self, request, *args, **kwargs):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('book-list')
        return render(request, self.template_name, {'serializer': serializer})

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    template_name = 'api/book_create.html'

    def post(self, request, *args, **kwargs):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('book-detail', pk=serializer.data['id'])
        return render(request, self.template_name, {'serializer': serializer})

class BookRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    template_name = 'api/book_detail.html'

    def get(self, request, *args, **kwargs):
        # Retrieve the book and render the template with the book data
        book = get_object_or_404(self.queryset, pk=kwargs['pk'])
        return render(request, self.template_name, {'book': book})

    def put(self, request, *args, **kwargs):
        # Update the book and redirect to the book detail page
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        # Delete the book and redirect to the book list
        return self.destroy(request, *args, **kwargs)
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    template_name = 'api/book_update.html'

    def get(self, request, *args, **kwargs):
        book = get_object_or_404(self.queryset, pk=kwargs['pk'])
        serializer = BookSerializer(instance=book)
        return render(request, self.template_name, {'serializer': serializer, 'book': book})

    def post(self, request, *args, **kwargs):
        book = get_object_or_404(self.queryset, pk=kwargs['pk'])
        serializer = BookSerializer(instance=book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('book-detail', pk=book.pk)
        return render(request, self.template_name, {'serializer': serializer, 'book': book})

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    template_name = 'api/book_delete.html'

    def get(self, request, *args, **kwargs):
        book = get_object_or_404(self.queryset, pk=kwargs['pk'])
        return render(request, self.template_name, {'book': book})

    def post(self, request, *args, **kwargs):
        book = get_object_or_404(self.queryset, pk=kwargs['pk'])
        book.delete()
        return redirect('book-list')  # Redirect to the book list page after deletion
class BookRetrieveView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    template_name = 'api/book_detail.html'

    def get(self, request, *args, **kwargs):
        book = get_object_or_404(self.queryset, pk=kwargs['pk'])
        serializer = BookSerializer(instance=book)
        return render(request, self.template_name, {'serializer': serializer, 'book': book})