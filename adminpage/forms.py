from .models import Faq
from bootstrap_modal_forms.forms import BSModalForm

class FaqForm(BSModalForm):
    class Meta:
        model = Faq
        fields = ['faq_id', 'faq_type', 'faq_question', 'faq_answer']