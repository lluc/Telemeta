# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Cooperative Artefacts <artefacts.lle@gmail.com>

import django.forms as forms
from django.forms import ModelForm
from telemeta.models import Authority
from django.utils.translation import ugettext_lazy as _

from markdownx.fields import MarkdownxFormField
from bootstrap_datepicker.widgets import DatePicker

class AuthorityForm(ModelForm):

    role = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=Authority._meta.get_field('roles').choices)

    def __init__(self, *args, **kwargs):
        super(AuthorityForm, self).__init__(*args, **kwargs)
        self.fields["biography"] = MarkdownxFormField(label="Biographie")
        self.fields["biography"].required = False
        self.fields["birth_date"] = forms.DateField(
            widget=DatePicker(
                options={
                    "format": "mm/dd/yyyy",
                    "autoclose": True
                }
            )
        )
        if self.instance and self.instance.pk:
            self.fields['role'].initial = self.instance.roles.split(',')

        translations = [
            ["civilite","Civilité"],
            ["birth_date","Date de naissance"],
            ["birth_location","Lieu de naissance"],
            ["death_date","Date de décès"],
            ["death_location","Lieu de décès"]
        ]

        for t in translations :
            self.fields[t[0]].label=t[1]

        # if you want to do it to all of them
        for field in self.fields.values():
            field.error_messages = {'required':'Le champ {fieldname} est obligatoire'.format(fieldname=field.label),'blank':'Le champ {fieldname} est vide'.format(fieldname=field.label), 'null':'Le champ {fieldname} est de valeur null'.format(fieldname=field.label)}

    def save(self, commit=True):
        authority = super(AuthorityForm,self).save(commit=False)
        authority.roles = ','.join(self.cleaned_data['role'])
        if commit:
            authority.save()
        return authority

    class Meta:
        model = Authority
        exclude = []
