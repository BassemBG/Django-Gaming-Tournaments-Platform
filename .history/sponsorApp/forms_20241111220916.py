from django import forms
from .models import Sponsor, Sponsorship, SponsorshipStatus

"""class SponsorForm(forms.ModelForm):
    class Meta:
        model = Sponsor
        fields = ['identifier', 'email', 'responsible', 'address', 'website', 'type']
        widgets = {
            'type': forms.Select(attrs={
                'class': 'scrollable-dropdown'
            }),
        }
"""


{% if user.is_authenticated and user.role == 'Sponsor' %}
				<div class="login-form-container">
					<h1>Sponsor a tournament</h1>
					<form method="POST"  action="{% url 'register_sponsor' %}">
						{% csrf_token %}
						<div class="textbox">
							<select name="tournament">
								{% for tournament in tournaments %}
									<option value="{{ tournament.id }}">{{ tournament.name }}</option>
								{% endfor %}
							</select>
							{% if form.tournament.errors %}
							<span class="check-message">{{ form.tournament.errors.0 }}</span>
							{% endif %}
						</div>
						<div class="textbox">
							<input type="text" name="sponsor" placeholder="Sponsor" value="{{ form.sponsor.value|default:user.cin }}" hidden>
							{% if form.sponsor.errors %}
							<span class="check-message">{{ form.sponsor.errors.0 }}</span>
							{% endif %}
						</div>
						<div class="textbox">
							<input type="text" name="amount" placeholder="Amount" value="{{ form.amount.value|default:'' }}">
							{% if form.amount.errors %}
							<span class="check-message">{{ form.amount.errors.0 }}</span>
							{% endif %}
						</div>
						<div class="textbox">
							<input type="date" name="startdate" placeholder="Start Date" value="{{ form.startdate.value|default:'' }}">
							{% if form.startdate.errors %}
							<span class="check-message">{{ form.startdate.errors.0 }}</span>
							{% endif %}
						</div>
						<div class="textbox">
							<input type="date" name="enddate" placeholder="End Date" value="{{ form.enddate.value|default:'' }}">
							{% if form.enddate.errors %}
							<span class="check-message">{{ form.enddate.errors.0 }}</span>
							{% endif %}
						</div>
						<div class="textbox">
							<select name="status">
								<option value="Pending">Pending</option>
								<option value="Approved">Approved</option>
								<option value="Rejected">Rejected</option>
								<option value="Terminated">Terminated</option>
							</select>
							{% if form.status.errors %}
							<span class="check-message">{{ form.status.errors.0 }}</span>
							{% endif %}
						</div>
						<input type="submit" value="Register" class="btn_1 d-none d-sm-block">
					</form>
				</div>
			{% endif %}	
class SponsorshipForm(forms.ModelForm):
    class Meta:
        model = Sponsorship
        fields = ['sponsorship_amount', 'start_date', 'end_date']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

        