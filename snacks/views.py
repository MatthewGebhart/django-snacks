from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['snacks'] = [
            {
                "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/Pistachio_macro_whitebackground_NS.jpg/320px-Pistachio_macro_whitebackground_NS.jpg",
                "title": "Pistachio",
                "description": "a member of the cashew family, is a small tree originating from Central Asia to Afghanistan. The tree produces seeds that are widely consumed as food.",
                "reference_url": "https://en.wikipedia.org/wiki/Pistachio"
            }, {
                "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Watermelon_cross_BNC.jpg/320px-Watermelon_cross_BNC.jpg",
                "title": "Watermelon",
                "description": "a flowering plant species of the Cucurbitaceae family and the name of its edible fruit. A scrambling and trailing vine-like plant, it is a highly cultivated fruit worldwide, with more than 1,000 varieties.",
                "reference_url": "https://en.wikipedia.org/wiki/Watermelon"
            }, {
                "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Nachos-cheese.jpg/159px-Nachos-cheese.jpg",
                "title": "Nachos",
                "description": "a Mexican culinary dish consisting of fried tortilla chips or totopos covered with melted cheese or cheese sauce, as well as a variety of other toppings and garnishes",
                "reference_url": "https://en.wikipedia.org/wiki/Nachos"
            },

        ]
        return context

class AboutPageView(TemplateView):
    template_name = "about.html"