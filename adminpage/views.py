# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Faq, Log
from .forms import FaqForm
from django.urls import reverse_lazy
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from bootstrap_modal_forms.generic import BSModalCreateView, BSModalUpdateView, BSModalDeleteView
from django.shortcuts import render
from django.db.models import Q, DateTimeField, DateField, Count
from django.db.models.functions import TruncMonth, TruncDate
import simplejson as json

def chart(request):
    stats = Log.objects \
        .annotate(stat_date=TruncDate('log_date')) \
        .values('stat_date') \
        .annotate(stat_count=Count('log_userid')
                  ).values('stat_date', 'stat_count')

    date_list = [];
    date_count = [];
    for stat in stats:
        print(stat['stat_date'])
        date_list.append(str(stat['stat_date']))
        date_count.append(str(stat['stat_count']))
    print(date_list)
    context = {'stats': stats, 'date_list': json.dumps(date_list), 'date_count' : json.dumps(date_count)}
    return render(request, 'adminpage/column-with-data-labels.html', context)


def index(request):
    faqs = Faq.objects.all()
    context = {'faqs': faqs}
    return render(request, 'adminpage/index.html', context)


def listfaqs(request):
    search_type = request.GET.get('search_type')
    search_keyword = request.GET.get('search_keyword')
    if search_keyword is None:
        search_keyword = ""

    if len(search_keyword) > 0:
        if search_type == '1':
            faq_list = Faq.objects.order_by('pk').filter(faq_question__contains=search_keyword)
        elif search_type == '2':
            faq_list = Faq.objects.order_by('pk').filter(faq_answer__contains=search_keyword)
        elif search_type == '3':
            faq_list = Faq.objects.order_by('pk').filter(Q(faq_question__contains=search_keyword)
                                                         | Q(faq_answer__contains=search_keyword))

    else:
        search_type = '1'
        search_keyword = ''
        faq_list = Faq.objects.all()

    paginator = Paginator(faq_list, 5)  # "5" 한페이지에서 보여줄 갯수를 정한다.
    page = request.GET.get('page')
    faqs = paginator.get_page(page)
    return render(request, 'adminpage/list_faqs.html', {'faqs': faqs, 'type': search_type, 'keyword': search_keyword})


def listlogs(request):
    search_type = request.GET.get('search_type')
    search_keyword = request.GET.get('search_keyword')
    stat_gbn = request.GET.get('optionRadios')
    to_date = request.GET.get('to_date')
    from_date = request.GET.get('from_date')
    if to_date is None:
        to_date = '2999-01-01'
    if from_date is None:
        from_date = '2010-01-01'
    if search_keyword is None:
        search_keyword = ""

    if len(search_keyword) > 0:
        if search_type == '1':
            log_list = Log.objects.order_by('pk')\
                .filter(log_date__range=[from_date, to_date])\
                .filter(Log_question__contains=search_keyword)
        elif search_type == '2':
            log_list = Log.objects.order_by('pk')\
                .filter(log_date__range=[from_date, to_date])\
                .filter(Log_answer__contains=search_keyword)
        elif search_type == '3':
            log_list = Log.objects.order_by('pk')\
                .filter(log_date__range=[from_date, to_date])\
                .filter(Q(Log_question__contains=search_keyword)
                                                         | Q(Log_answer__contains=search_keyword))

    else:
        search_type = '1'
        search_keyword = ''
        log_list = Log.objects.filter(log_date__range=[from_date, to_date])

    paginator = Paginator(log_list, 5)  # "5" 한페이지에서 보여줄 갯수를 정한다.
    page = request.GET.get('page')
    logs = paginator.get_page(page)
    return render(request, 'adminpage/list_logs.html', {'logs': logs,
                                                        'type': search_type,
                                                        'keyword': search_keyword,
                                                        'optionRadios': stat_gbn,
                                                        'to_date': to_date,
                                                        'from_date': from_date
                                                        })


def statisticslogs(request):
    stat_type = request.GET.get('stat_type')
    stat_gbn = request.GET.get('optionRadios')
    to_date = request.GET.get('to_date')
    from_date = request.GET.get('from_date')
    if stat_type == 'M':
        if stat_gbn == 'period':
            stats = Log.objects \
                .filter(log_date__range=[from_date, to_date]) \
                .annotate(stat_date=TruncMonth('log_date')) \
                .order_by('-stat_date') \
                .values('stat_date') \
                .annotate(stat_count=Count('log_userid')
                          ).values('stat_date', 'stat_count')
        else:
            stats = Log.objects \
                .annotate(stat_date=TruncMonth('log_date')) \
                .order_by('-stat_date') \
                .values('stat_date') \
                .annotate(stat_count=Count('log_userid')
                          ).values('stat_date', 'stat_count')
    else:
        if stat_gbn == 'period':
            stats = Log.objects \
                .filter(log_date__range=[from_date, to_date])\
                .annotate(stat_date=TruncDate('log_date')) \
                .order_by('-stat_date') \
                .values('stat_date') \
                .annotate(stat_count=Count('log_userid')
                          ).values('stat_date', 'stat_count')
        else:
            stats = Log.objects \
                .annotate(stat_date=TruncDate('log_date')) \
                .order_by('-stat_date')\
                .values('stat_date') \
                .annotate(stat_count=Count('log_userid')
                          ).values('stat_date', 'stat_count')

    date_list = [];
    date_count = [];
    for stat in stats:
        date_list.append(str(stat['stat_date']))
        date_count.append(str(stat['stat_count']))

    date_list.reverse()
    date_count.reverse()

    context = {'stats': stats,
               'stat_type': stat_type,
               'optionRadios': stat_gbn,
               'to_date': to_date,
               'from_date': from_date,
               'date_list': json.dumps(date_list),
               'date_count': json.dumps(date_count)}
    return render(request, 'adminpage/statistics_logs.html', context)


class FaqCreateView(BSModalCreateView):
    template_name = 'adminpage/create_faq.html'
    form_class = FaqForm
    success_message = 'Sucess: Faq was created'
    success_url = reverse_lazy('index_faq')


class FaqUpdateView(BSModalUpdateView):
    model = Faq
    template_name = 'adminpage/update_faq.html'
    form_class = FaqForm
    success_message = 'Sucess: Faq was update'
    success_url = reverse_lazy('index_faq')


class FaqDeleteView(BSModalDeleteView):
    model = Faq
    template_name = 'adminpage/delete_faq.html'
    success_message = 'Sucess: Faq was created'
    success_url = reverse_lazy('index_faq')
