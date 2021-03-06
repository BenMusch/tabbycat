import logging

from django.contrib import messages
from django.forms import modelformset_factory
from django.http import HttpResponseRedirect
from django.utils.translation import ugettext as _
from django.views.generic import TemplateView

from formtools.wizard.views import SessionWizardView

from participants.emoji import set_emoji
from participants.models import Adjudicator, Institution, Team
from tournaments.mixins import TournamentMixin
from utils.mixins import SuperuserRequiredMixin
from venues.models import Venue

from .forms import (AdjudicatorDetailsForm, ImportInstitutionsRawForm,
                    ImportVenuesRawForm, NumberForEachInstitutionForm,
                    TeamDetailsForm, TeamDetailsFormSet, VenueDetailsForm)

logger = logging.getLogger(__name__)


# TODO: add log actions for all of these?

class ImporterSimpleIndexView(SuperuserRequiredMixin, TournamentMixin, TemplateView):
    template_name = 'simple_import_index.html'


class BaseImportWizardView(SuperuserRequiredMixin, TournamentMixin, SessionWizardView):
    """Common functionality for the import wizard views. In particular, this
    class implements functionality for a "details" step that is initialized
    with data from the previous step. The details step shows a ModelFormSet
    associated with a specified model."""

    DETAILS_STEP = 'details'
    tournament_redirect_pattern_name = 'importer-simple-index'

    model = None  # must be specified by subclass

    def get_details_form_initial(self):
        raise NotImplementedError

    def get_template_names(self):
        return ['simple_import_%(model)ss_%(step)s.html' % {
            'model': self.model._meta.model_name,
            'step': self.steps.current
        }]

    def get_form_initial(self, step):
        """Overridden to initialize the 'details' step with data from a previous
        step."""
        if step == self.DETAILS_STEP and step == self.steps.next:
            return self.get_details_form_initial()
        else:
            return super().get_form_initial(step)

    def get_form_instance(self, step):
        if step == self.DETAILS_STEP:
            return self.model.objects.none()
        else:
            return super().get_form_instance(step)

    def get_form(self, step=None, **kwargs):
        form = super().get_form(step, **kwargs)
        if step == self.DETAILS_STEP:
            form.extra = len(form.initial_extra)
            form.save_as_new = True
        return form

    def done(self, form_list, form_dict, **kwargs):
        self.instances = form_dict[self.DETAILS_STEP].save()
        messages.success(self.request, _("Added %(count)d %(model_plural)s.") % {
                'count': len(self.instances), 'model_plural': self.model._meta.verbose_name_plural})
        return HttpResponseRedirect(self.get_redirect_url())


class ImportInstitutionsWizardView(BaseImportWizardView):
    model = Institution
    form_list = [
        ('raw', ImportInstitutionsRawForm),
        ('details', modelformset_factory(Institution, fields=('name', 'code'), extra=0)),
    ]

    def get_details_form_initial(self):
        return self.get_cleaned_data_for_step('raw')['institutions_raw']


class ImportVenuesWizardView(BaseImportWizardView):
    model = Venue
    form_list = [
        ('raw', ImportVenuesRawForm),
        ('details', modelformset_factory(Venue, form=VenueDetailsForm, extra=0))
    ]

    def get_form_kwargs(self, step):
        if step == 'details':
            return {'form_kwargs': {'tournament': self.get_tournament()}}
        else:
            return super().get_form_kwargs(step)

    def get_details_form_initial(self):
        return self.get_cleaned_data_for_step('raw')['venues_raw']


class BaseImportByInstitutionWizardView(BaseImportWizardView):
    """Common functionality in teams and institutions wizards."""

    def get_form_kwargs(self, step):
        if step == 'numbers':
            return {'institutions': Institution.objects.all()}
        elif step == 'details':
            return {'form_kwargs': {'tournament': self.get_tournament()}}

    def add_details(self, number, institution):
        initial_list = []
        for i in range(1, number+1):
            initial = {'institution': institution}
            initial.update(self.get_details_instance_initial(i))
            initial_list.append(initial)
        return initial_list

    def get_details_form_initial(self):
        data = self.get_cleaned_data_for_step('numbers')
        initial_list = []

        institutionless = data.get('no_institution')
        if institutionless is not None: # field left blank
            initial_list.extend(self.add_details(institutionless, None))

        for institution in Institution.objects.order_by('name'):
            number = data.get('number_institution_%d' % institution.id, 0)
            if number is None: # field left blank
                continue
            initial_list.extend(self.add_details(number, institution.id))

        return initial_list

    def get_details_instance_initial(self):
        raise NotImplementedError


class ImportTeamsWizardView(BaseImportByInstitutionWizardView):
    model = Team
    form_list = [
        ('numbers', NumberForEachInstitutionForm),
        ('details', modelformset_factory(Team, form=TeamDetailsForm, formset=TeamDetailsFormSet, extra=0)),
    ]

    def get_details_instance_initial(self, i):
        return {'reference': str(i), 'use_institution_prefix': True}

    def done(self, form_list, form_dict, **kwargs):
        # Also set emoji on teams
        redirect = super().done(form_list, form_dict, **kwargs)
        set_emoji(self.instances, self.get_tournament())
        return redirect


class ImportAdjudicatorsWizardView(BaseImportByInstitutionWizardView):
    model = Adjudicator
    form_list = [
        ('numbers', NumberForEachInstitutionForm),
        ('details', modelformset_factory(Adjudicator, form=AdjudicatorDetailsForm, extra=0)),
    ]

    def get_details_instance_initial(self, i):
        return {'name': _("Adjudicator %(number)d") % {'number': i}, 'test_score': 2.5}
