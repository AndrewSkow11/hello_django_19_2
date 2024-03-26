from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse, reverse_lazy

from catalog.models import Product, Version, Category
from django.views.generic import (
    ListView,
    DetailView,
    View,
    CreateView,
    UpdateView,
    DeleteView,
)
from catalog.forms import ProductForm, VersionForm, ProductModeratorForm
from django.forms import inlineformset_factory
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
)

from catalog.services import get_categories_cache


class ProductView(LoginRequiredMixin, ListView):
    model = Product

    def get_queryset(self):
        queryset = super().get_queryset()

        if not self.request.user.is_staff:
            queryset = queryset.filter(is_published=True)

        return queryset

    @staticmethod
    def versions():
        return Version.objects.all()


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product

    # permission_required = "catalog.view_product"

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)

        if (self.object.author != self.request.user and
                not self.request.user.is_staff):
            raise Http404

        return self.object


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:home")
    permission_required = "catalog.add_product"

    def form_valid(self, form):
        self.object = form.save()
        self.object.author = self.request.user
        self.object.save()

        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    permission_required = "catalog.change_product"
    form_class = ProductForm

    def get_form_class(self):
        if self.request.user.is_staff:
            return ProductModeratorForm
        else:
            return ProductForm

    def test_func(self):
        user = self.request.user
        instance: Product = self.get_object()
        custom_perms: tuple = (
            "catalog.set_publication",
            "catalog.set_category",
            "catalog.set_description",
        )

        if user == instance.user:
            return True
        elif (user.groups.filter(name="moderator") and
              user.has_perms(custom_perms)):
            return True

        return self.handle_no_permission()

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)

        if (self.object.author != self.request.user and
                not self.request.user.is_staff):
            raise Http404("Доступ закрыт")

        return self.object

    def get_success_url(self, *args, **kwargs):
        return reverse("catalog:update_product",
                       args=[self.get_object().pk])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        # Формирование формсета
        VersionFormset = inlineformset_factory(
            Product, Version, form=VersionForm, extra=1
        )
        if self.request.method == "POST":
            context_data["formset"] = VersionFormset(
                self.request.POST, instance=self.object
            )
        else:
            context_data["formset"] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data["formset"]
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:home")
    # permission_required = "catalog.change_product"


class ContactView(View):
    template_name = "catalog/contacts.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        return render(request, "catalog/not_available.html")


def categories(request):
    context = {
        "object_list": get_categories_cache(),
        "title": "Все категории продуктов",
    }
    return render(request, "catalog/categories.html", context)


@login_required
def category_products(request, pk):
    category_item = Category.objects.get(pk=pk)
    context = {
        "object_list": Product.objects.filter(category_id=pk),
        "title": f"Продкуты категории {category_item.nomination}",
    }

    return render(request, "catalog/product_list.html", context)
