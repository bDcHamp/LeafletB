from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.template.response import TemplateResponse
from django.http import HttpRequest
from typing import Optional, Any, cast
from django.db.models.query import QuerySet
from django.db.models import QuerySet as DjangoQuerySet

from wagtail.models import Page
from wagtail.contrib.search_promotions.models import Query
from wagtail.search.backends import get_search_backend


def search(request: HttpRequest) -> TemplateResponse:
    search_query: Optional[str] = request.GET.get('query', None)
    page: str = request.GET.get('page', '1')

    # Search
    search_results: DjangoQuerySet[Page]
    if search_query:
        # Search in specific page types that contain relevant content
        base_qs = cast(Any, Page.objects.all())  # Cast to Any to bypass type checking
        search_qs = base_qs.live().search(search_query)  
        search_results = cast(DjangoQuerySet[Page], search_qs)
        
        # Record the query
        query = Query.get(search_query)
        query.add_hit()
    else:
        search_results = Page.objects.none()

    # Pagination
    paginator = Paginator(search_results, 10)
    try:
        paginated_results = paginator.page(page)
    except PageNotAnInteger:
        paginated_results = paginator.page(1)
    except EmptyPage:
        paginated_results = paginator.page(paginator.num_pages)

    return TemplateResponse(request, 'search/search.html', {
        'search_query': search_query,
        'search_results': paginated_results,
    })
